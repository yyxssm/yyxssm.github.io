---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

My research interests include embodied robotics and AIGC in autonomous driving. I have published papers at top international AI conferences.


# 🔥 News
- *2026.10*: 🏅 I was recognized as a **NeurIPS 2026 Main Reviewer: Top Reviewer**.
- *2026.09*: 🎉 Three of our papers have been accepted to **NeurIPS 2026**; congratulations to **Runhe**, **Yikai**, and **Xuetong**!
- *2026.06*: 🏅 I was recognized as a **CVPR 2026 Outstanding Reviewer (Top 2%)**.
- *2026.02*: 🎉 Two of our papers have been accepted to **CVPR 2026**; congratulations to **Hengyu** and **Junpeng**!
- *2025.06*: 🎉 **Dark-ISP** is accepted by **ICCV 2025**.
- *2025.06*: 🎉 **FusionMap** is accepted by **IEEE Transactions on Artificial Intelligence**.
- *2025.06*: 🎉 [EC-SLAM](https://ui.adsabs.harvard.edu/abs/2024arXiv240413346L/abstract) is accepted by **Pattern Recognition**.
- *2025.06*: 🎉 **CasPoinTr** is accepted by **IROS 2025**.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_OrderMind/OrderMind.png' alt="OrderMind framework for spatial-aware manipulation ordering" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Spatial-Aware Manipulation Ordering](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f0b42291ddab77dcb2ef8a3488301b62-Abstract-Conference.html)

**Yuxiang Yan**\*, Zhiyuan Zhou\*, Xin Gao, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu

[**[Paper]**](https://proceedings.neurips.cc/paper_files/paper/2025/file/f0b42291ddab77dcb2ef8a3488301b62-Paper-Conference.pdf)

- OrderMind learns which object a robot should manipulate first in cluttered environments, where an improper order can cause collisions or block access. It combines spatial context understanding and temporal priority prediction to model both object-object and object-manipulator interactions. A spatial prior labeling strategy guides a vision-language model to generate training supervision. Evaluated on a Manipulation Ordering Benchmark with 163,222 samples and on real robots, OrderMind improves manipulation ordering accuracy and efficiency while supporting real-time inference.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICRA 2024 Oral</div><img src='images\2024_05_PointSSC\PointSSC.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


[PointSSC: A Cooperative Vehicle-Infrastructure Point Cloud Benchmark for Semantic Scene Completion](https://ieeexplore.ieee.org/abstract/document/10610043/)


**Yuxiang Yan**, Boda Liu, Jianfei Ai, Qinbu Li, Ru Wan, Jian Pu

[**[Paper]**](https://ieeexplore.ieee.org/abstract/document/10610043/)    [**[Code]**](https://github.com/yyxssm/PointSSC)    [**[Video]**](https://www.youtube.com/watch?v=RZrXaJsEmyM)
[![GitHub Stars](https://img.shields.io/github/stars/yyxssm/PointSSC?style=social)](https://github.com/yyxssm/PointSSC)
[![GitHub Forks](https://img.shields.io/github/forks/yyxssm/PointSSC?style=social)](https://github.com/yyxssm/PointSSC)
- Most existing Semantic Scene Completion (SSC) models focus on volumetric representations, which are memory-inefficient for large outdoor spaces. We introduce PointSSC, the first cooperative vehicle-infrastructure point cloud benchmark for SSC. These scenes exhibit long-range perception and minimal occlusion. We develop an automated annotation pipeline and propose a LiDAR-based baseline model. PointSSC provides a challenging testbed to drive advances in semantic point cloud completion for real-world navigation.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/2025_06_Dark-ISP/Dark-ISP.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


**Dark-ISP: Enhancing RAW Image Processing for Low-Light Object Detection**


Guo jiasheng\*, Xin Gao\*, **Yuxiang Yan**, Guanghao Li, Jian Pu 

- Dark-ISP is a lightweight and self-adaptive Image Signal Processing (ISP) plugin designed to improve low-light object detection. Unlike previous methods that either use RAW-RGB images with information loss or complex frameworks, Dark-ISP processes Bayer RAW images directly in dark environments. Its key innovations include deconstructing conventional ISP pipelines into linear and nonlinear sub-modules optimized for task-driven losses, and a self-boosting strategy that enhances cooperation between sub-modules.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE T-AI</div><img src='images/2024_05_FusionMap/FusionMap.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Constrained Gaussian Splatting via Implicit TSDF Hash Grid for Dense RGB-D SLAM**

Guanghao Li, Qi Chen, Sijia Hu, **Yuxiang Yan**, Jian Pu

- FusionMap is an advanced SLAM system that combines explicit 3DGS and implicit NeRF representations to improve surface reconstruction accuracy. By addressing the limitations of traditional 3DGS, FusionMap achieves up to 30 times faster processing and a 38% accuracy boost over conventional methods. This innovation sets new standards for real-time 3D mapping and localization, enabling next-generation applications in virtual environments, autonomous navigation, and dynamic scene reconstruction.
</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pattern Recognition</div><img src='images/2023_12_EC_SLAM/EC_SLAM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EC-SLAM: Real-time Dense Neural RGB-D SLAM System with Effectively Constrained Global Bundle Adjustment](https://ui.adsabs.harvard.edu/abs/2024arXiv240413346L/abstract)

Guanghao Li\*, Qi Chen\*, **Yuxiang Yan**, Jian Pu

[**Project**](https://github.com/Lightingooo/EC-SLAM)
[![GitHub Stars](https://img.shields.io/github/stars/Lightingooo/EC-SLAM?style=social)](https://github.com/Lightingooo/EC-SLAM)
[![GitHub Forks](https://img.shields.io/github/forks/Lightingooo/EC-SLAM?style=social)](https://github.com/Lightingooo/EC-SLAM)

- EC-SLAM is a real-time dense RGB-D SLAM system that leverages Neural Radiance Fields (NeRF) for enhanced pose optimization, using sparse parametric encodings, TSDF, and a globally constrained Bundle Adjustment strategy to improve tracking accuracy and reconstruction performance in real-time.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IROS 2025</div><img src='images\2025_06_CasPoinTr\caspointr.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CasPoinTr: Point Cloud Completion with Cascaded Networks and Knowledge Distillation**

Yifan Yang, **Yuxiang Yan**, Boda Liu, Jian Pu

- CasPoinTr completes highly incomplete real-world point clouds in two stages. First, Shape Reconstruction Module generates auxiliary information to guide missing-region prediction. Then, Fused Completion Module refines the output using knowledge distilled from a teacher model trained on dense clouds, improving global shape estimation and local detail recovery.
</div>
</div>

# 🎖 Honors and Awards
- *2025.05* Fudan University First Class Scholarship ($1400)
- *2022.06* Outstanding Graduate of Shanghai

# 📖 Educations
- *2022.09 - now*, Ph.D., Fudan University, China. 
- *2018.09 -2022.06*, Bachelor of Science, East China University of Science and Technology. 

# 👨‍💼 Academic Service
- Journal Reviewer: RA-L, TIV, Cognitive Neurodynamics
- Conference Reviewer: CVPR, ICCV, AAAI, NeurIPS, ICME
- Teaching assistant: Embodied Intelligence, Introduction to Autonomous Driving

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

<!-- # 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->