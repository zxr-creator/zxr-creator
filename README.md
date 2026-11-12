<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="zxr-creator: efficient AI, ML systems, and recursive self-improvement">
</picture>

<p align="center">
  <a href="https://zxr-creator.github.io/"><img alt="Website" src="https://img.shields.io/badge/website-zxr--creator.github.io-0a0a0a?style=flat-square"></a>
  <a href="https://scholar.google.com/citations?user=-AMCkEIAAAAJ&hl=en"><img alt="Google Scholar" src="https://img.shields.io/badge/Google_Scholar-4285F4?style=flat-square&logo=googlescholar&logoColor=white"></a>
  <a href="https://zxr-creator.github.io/#contact"><img alt="Email" src="https://img.shields.io/badge/email-contact-2450e6?style=flat-square&logo=gmail&logoColor=white"></a>
</p>

I'm a research intern at **Carnegie Mellon University's [InfiniAI Lab](https://www.infini-ai-lab.cmu.edu/)** with Prof. Beidi Chen, and at **Rice University** with Prof. Yuke Wang. I hold an M.S. in Computer Science from Rice.

Model capability keeps scaling, and so does the cost of running it. I work on closing the gap between what a model *should* cost and what it actually costs in production, at three levels:
- **the model:** architectures that are efficient by design;
- **the system:** turning those savings into wall-clock speed on real GPUs;
- **the engineer:** whether coding agents can build and optimize that stack themselves. An agent runs on the same systems it improves, so every gain makes the next agent better.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/research-dark.svg">
  <img src="assets/research-light.svg" width="100%" alt="Research areas: efficient model architecture (RISA, 5.53x faster sparse attention at 128K); conventional ML systems (Vortex, 3.46x serving throughput); recursive self-improvement (ServerBench, agent-built server at 4.87x the vLLM reference)">
</picture>

### Selected publications

<img alt="NeurIPS 2026" src="https://img.shields.io/badge/NeurIPS-2026-2450e6?style=flat-square"> **Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents**<br>
Zhuoming Chen, **zxr-creator**, Qilong Feng, Ranajoy Sadhukhan, Yang Zhou, Michael Qizhe Shieh, Zhihao Jia, Beidi Chen<br>
[arXiv](https://arxiv.org/abs/2606.06453) · [code](https://github.com/Infini-AI-Lab/vortex_torch) · [website](https://infini-ai-lab.github.io/vortex_torch/)

<img alt="submitted to NAACL 2027" src="https://img.shields.io/badge/submitted-NAACL_2027-8f8f8f?style=flat-square"> **ServerBench: How can your coding agents design specialized LLM serving systems?**<br>
**zxr-creator**, Zhiming Wang, Yongqi Liu, Zhaohui Wang, Shanglin Yang, Zikun Li, Zhuoming Chen, Beidi Chen<br>
[arXiv](https://arxiv.org/abs/2611.06841) · [code](https://github.com/Infini-AI-Lab/Server-Bench) · [blog](https://infini-ai-lab.github.io/Server-Bench/)

<img alt="submitted to MLSys 2027" src="https://img.shields.io/badge/submitted-MLSys_2027-8f8f8f?style=flat-square"> **CompressionBench: How can your coding agents compress LLMs?**<br>
**zxr-creator**, Zhifeng Li, Zhiming Wang, Yongqi Liu, Shanglin Yang, Yang Zhou, Zikun Li, Zhuoming Chen, Beidi Chen<br>
[arXiv](https://arxiv.org/abs/2611.06858v1) · [code](https://github.com/Infini-AI-Lab/Compression-Bench) · [blog](https://infini-ai-lab.github.io/Compression-Bench/)

<img alt="submitted to ICLR 2027" src="https://img.shields.io/badge/submitted-ICLR_2027-8f8f8f?style=flat-square"> **RISA: Recoverable Sparse Attention for Block-Diffusion Language Models**<br>
**zxr-creator**, Fanjiang Ye, Yuke Wang

<img alt="submitted to MLSys 2027" src="https://img.shields.io/badge/submitted-MLSys_2027-8f8f8f?style=flat-square"> **An Efficient and Adaptive Watermark Detection System with Tile-based Error Correction**<br>
**zxr-creator**, Xinze Feng, Jingwei Zuo, Fanjiang Ye, Yi Mu, Junfeng Guo, Heng Huang, Myungjin Lee, Yuke Wang<br>
[arXiv](https://arxiv.org/abs/2509.02447)

<details>
<summary><b>More papers</b> (SparSP, GenServe, R²-dLLM)</summary>
<br>

<img alt="submitted to EuroSys 2027" src="https://img.shields.io/badge/submitted-EuroSys_2027-8f8f8f?style=flat-square"> **SparSP: Exploiting Communication Sparsity for Sequence-Parallel Video DiTs**<br>
Desen Sun, **zxr-creator**, Yuke Wang, Sihang Liu<br>
[arXiv](https://arxiv.org/abs/2609.32197)

<img alt="submitted to MLSys 2027" src="https://img.shields.io/badge/submitted-MLSys_2027-8f8f8f?style=flat-square"> **GENSERVE: Efficient Co-Serving of Heterogeneous Diffusion Model Workloads**<br>
Fanjiang Ye, Zhangke Li, **zxr-creator**, Ethan Ma, Russell Chen, Kaijian Wang, Jingwei Zuo, Desen Sun, Ye Cao, Triston Cao, Myungjin Lee, Arvind Krishnamurthy, Yuke Wang<br>
[arXiv](https://arxiv.org/abs/2604.04335)

<img alt="submitted to NAACL 2027" src="https://img.shields.io/badge/submitted-NAACL_2027-8f8f8f?style=flat-square"> **R²-dLLM: Accelerating Diffusion Large Language Models via Spatio-Temporal Redundancy Reduction**<br>
Zhenbang Du, Kejing Xia, **zxr-creator**, Yonggan Fu, Nicolai Oswald, Binfei Ji, Brucek Khailany, Pavlo Molchanov, Yingyan (Celine) Lin<br>
[arXiv](https://arxiv.org/abs/2604.18995) · [code](https://github.com/GATECH-EIC/R2-dLLM)

</details>

Full list on [Google Scholar](https://scholar.google.com/citations?user=-AMCkEIAAAAJ&hl=en).

### Open source

| Project | What it is | Role | Stars |
|---|---|---|---|
| [**Vortex**](https://github.com/Infini-AI-Lab/vortex_torch) | Programmable sparse attention on SGLang + FlashInfer, with a workspace where agents write and benchmark new attention algorithms | co-developer | ![stars](https://img.shields.io/github/stars/Infini-AI-Lab/vortex_torch?style=flat-square&label=%E2%98%85&color=2450e6) |
| [**ServerBench**](https://github.com/Infini-AI-Lab/Server-Bench) | Agents evolve a minimal server into a specialized LLM serving system, graded by session replay and a hidden verifier | lead | ![stars](https://img.shields.io/github/stars/Infini-AI-Lab/Server-Bench?style=flat-square&label=%E2%98%85&color=2450e6) |
| [**CompressionBench**](https://github.com/Infini-AI-Lab/Compression-Bench) | Agents compress Qwen and Gemma checkpoints under 8–32 GiB budgets, judged once by a hidden verifier | lead | ![stars](https://img.shields.io/github/stars/Infini-AI-Lab/Compression-Bench?style=flat-square&label=%E2%98%85&color=2450e6) |
| [**LTSM-Bundle**](https://github.com/datamllab/ltsm) | Toolbox and benchmark for training LLMs on time-series forecasting | contributor | ![stars](https://img.shields.io/github/stars/datamllab/ltsm?style=flat-square&label=%E2%98%85&color=2450e6) |

### Experience & education

| | |
|---|---|
| `2026.02 – now` | **Carnegie Mellon University**, InfiniAI Lab · Research Intern with Prof. Beidi Chen |
| `2025.01 – now` | **Rice University**, Yuke's Lab · Research Intern with Prof. Yuke Wang |
| `2024.09 – 2024.12` | **Rice University**, DATA Lab · Research Intern with Prof. Xia Hu |
| `2024 – 2025` | **Rice University** · M.S. in Computer Science |
| `2020 – 2024` | **Sichuan University** · B.Eng. in Computer Science and Technology |

**Service:** Artifact Evaluation Committee, SOSP 2026 · MLSys 2026 · PPoPP 2026

<p align="center"><sub>off the clock: StarCraft II and Hearthstone</sub></p>
