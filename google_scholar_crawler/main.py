from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time
import sys
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 配置代理（使用 FreeProxy）
def setup_proxy():
    try:
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        if success:
            scholarly.use_proxy(pg)
            logger.info("成功设置代理")
            return True
        else:
            logger.warning("无法设置FreeProxy代理，尝试使用Tor代理")
            success = pg.Tor_External(tor_sock_port=9050, tor_control_port=9051)
            scholarly.use_proxy(pg)
            return success
    except Exception as e:
        logger.error(f"设置代理时出错: {e}")
        return False

# 设置重试机制
def get_author_with_retry(scholar_id, max_retries=5, delay=3):
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                logger.info(f"尝试获取作者信息，第 {attempt+1} 次尝试")
            
            # 使用代理
            if attempt > 1 and not setup_proxy():
                logger.warning("无法设置代理，继续尝试不使用代理")
            
            # 获取作者信息
            author = scholarly.search_author_id(scholar_id)
            if author:
                return author
        except Exception as e:
            logger.error(f"获取作者信息时出错: {e}")
            logger.info(f"等待 {delay} 秒后重试...")
            time.sleep(delay)
            delay *= 1.5  # 指数退避
    
    logger.error(f"在 {max_retries} 次尝试后无法获取作者信息")
    return None

try:
    # 检查环境变量
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
    if not scholar_id:
        logger.error("未设置 GOOGLE_SCHOLAR_ID 环境变量")
        sys.exit(1)
    
    # 获取作者信息
    logger.info(f"开始获取 Google Scholar ID: {scholar_id} 的信息")
    author = get_author_with_retry(scholar_id)
    
    if not author:
        logger.error("无法获取作者信息，退出")
        sys.exit(1)
    
    # 填充作者信息
    try:
        logger.info("填充作者详细信息")
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    except Exception as e:
        logger.error(f"填充作者详细信息时出错: {e}")
        # 尝试只获取基本信息
        try:
            logger.info("尝试只获取基本信息")
            scholarly.fill(author, sections=['basics'])
        except Exception as e2:
            logger.error(f"获取基本信息也失败: {e2}")
            sys.exit(1)
    
    # 保存数据
    name = author.get('name', 'Unknown Author')
    author['updated'] = str(datetime.now())
    
    # 确保 publications 存在
    if 'publications' in author:
        author['publications'] = {v['author_pub_id']:v for v in author['publications']}
    else:
        author['publications'] = {}
    
    print(json.dumps(author, indent=2))
    os.makedirs('results', exist_ok=True)
    
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)
    
    # 创建引用徽章数据
    citations = author.get('citedby', 0)
    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{citations}",
    }
    
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
    
    logger.info("成功获取并保存 Google Scholar 数据")

except Exception as e:
    logger.error(f"程序执行过程中发生错误: {e}")
    sys.exit(1)
