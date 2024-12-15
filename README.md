# SFADA-UWF-SLO
Advancing UWF-SLO Vessel Segmentation with Source-Free Active Domain Adaptation and a Novel Multi-Center Dataset (MICCAI 2024 Early accept 🎉)

# Introduction 📑

This project introduces a new setting in medical image segmentation, termed **Source-Free Active Domain Adaptation (SFADA)**. SFADA aims to facilitate cross-center medical image segmentation while protecting data privacy and reducing the workload on medical professionals. By requiring only minimal labeling effort, SFADA achieves effective model transfer and results comparable to those of fully supervised approaches.

Fig. 1. Visual comparison of traditional training and our Source-Free Active Domain Adaptation (SFADA) training.
<img width="833" alt="1727953214369" src="https://github.com/user-attachments/assets/897352e9-78e1-4ba5-ab2d-8ca610a33599">

# How to Run the Code 🛠
### Environment Installation
### 1. Training source models in the source center
For setting up the environment and training the source model, please refer to the [[STDR]](https://github.com/whq-xxh/SFADA-GTV-Seg) project. Please note that some hyperparameters, such as the image input resolution, may need to be adjusted.

### 2. CUP selection strategy


# Dataset 📊
<img width="1396" alt="data" src="https://github.com/user-attachments/assets/585243ea-4da6-403a-b831-9b504af9ae1f">

For PRIME-FP20: please refer to this [IEEE article](https://ieeexplore.ieee.org/abstract/document/9208757) and [dataset link](https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset).

For Center A: please contact Hongqiu (hongqiuwang16@gmail.com) for the dataset. One step is needed to download the dataset: **1) Use your google email to apply for the download permission ([OneDrive](https://hkustgz-my.sharepoint.com/my?id=%2Fpersonal%2Fhwang007%5Fconnect%5Fhkust%2Dgz%5Fedu%5Fcn%2FDocuments%2F24MICCAI%2DSFADA%2DUWF&sortField=FileLeafRef&isAscending=true) [BaiduPan](https://pan.baidu.com/s/1ESNR_tAFWhK6tfWzcMZuHg)). We just handle the **real-name email** and **your email suffix must match your affiliation**. The email should contain the following information:

For Center B, organizing and releasing soon.


    Name/Homepage/Google Scholar: (Tell us who you are.)
    Primary Affiliation: (The name of your institution or university, etc.)
    Job Title: (E.g., Professor, Associate Professor, Ph.D., etc.)
    Affiliation Email: (the password will be sent to this email, we just reply to the email which is the end of "edu".)
    How to use: (Only for academic research, not for commercial use or second-development.)
**The data provided cannot be forwarded to others, and only individuals with approved applications are authorized to use them.**

**Thanks for understanding and cooperation!**



# Citation 📖

If you find our work useful or relevant to your research, please consider citing:
```
@inproceedings{wang2024advancing,
  title={Advancing uwf-slo vessel segmentation with source-free active domain adaptation and a novel multi-center dataset},
  author={Wang, Hongqiu and Luo, Xiangde and Chen, Wu and Tang, Qingqing and Xin, Mei and Wang, Qiong and Zhu, Lei},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={75--85},
  year={2024},
  organization={Springer}
}
```

# Comparison with Other Methods 📈

We acknowledge the developers of the comparative methods in **ADA4MIA** [here](https://github.com/whq-xxh/ADA4MIA).
