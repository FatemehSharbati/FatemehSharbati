<div align="center">
  <img src="assets/header.svg" width="100%" alt="Fatemeh Sharbati — Neuroimaging, Medical Imaging AI"/>
</div>

**Radiology graduate building open tools for neuroimaging — from DICOM to deep learning.**

Brain MRI preprocessing · Tumor segmentation · Medical vision-language models · Reproducible research

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![MONAI](https://img.shields.io/badge/MONAI-00A0E9?style=flat-square)
![nnU-Net](https://img.shields.io/badge/nnU--Net-7B1FA2?style=flat-square)
![nibabel](https://img.shields.io/badge/nibabel-444444?style=flat-square)
![SimpleITK](https://img.shields.io/badge/SimpleITK-8BC34A?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=2800&pause=900&color=22d3ee&center=true&vCenter=true&width=760&lines=Brain+MRI+preprocessing+%E2%86%92+QC;Tumor+segmentation+on+BraTS;From+DICOM+to+deep+learning;Open+neuroimaging+tools" alt="Brain MRI preprocessing, tumor segmentation, open neuroimaging tools"/>
</div>

---

## What I'm building

- **Brain MRI preprocessing pipelines.** N4 bias correction, intensity normalization, registration and QC reports — reproducible, tested, documented.
- **Segmentation, benchmarked honestly.** Tumor segmentation on BraTS and anatomical segmentation benchmarks with Dice / HD95 and visual QC.
- **Unsupervised anomaly detection.** Autoencoder-based lesion highlighting in brain MRI — no labels required.
- **Vision-language models for radiology.** CLIP-style image–text retrieval demos plus subgroup fairness audits, because medical AI must be audited, not just trained.

---

**Capabilities, and the proof**

| Capability | Proof |
| --- | --- |
| Brain MRI preprocessing (N4, normalization, registration, QC) | [brain-mri-preprocessing-pipeline](https://github.com/FatemehSharbati/brain-mri-preprocessing-pipeline) |
| Segmentation benchmarking (Dice, HD95, TotalSegmentator / SynthSeg) | [anatomical-seg-benchmark-qc](https://github.com/FatemehSharbati/anatomical-seg-benchmark-qc) |
| Brain tumor segmentation (nnU-Net, MONAI, BraTS WT/TC/ET) | [brats-tumor-segmentation-nnunet](https://github.com/FatemehSharbati/brats-tumor-segmentation-nnunet) |
| Unsupervised anomaly detection (autoencoders, brain MRI) | [unsupervised-mri-anomaly-detection](https://github.com/FatemehSharbati/unsupervised-mri-anomaly-detection) |
| Medical vision-language models + fairness auditing | [radiology-mini-vlm](https://github.com/FatemehSharbati/radiology-mini-vlm) |

---

## Featured projects

| Project | Project |
| --- | --- |
| **[brain-mri-preprocessing-pipeline](https://github.com/FatemehSharbati/brain-mri-preprocessing-pipeline)**<br>Reproducible T1 brain MRI preprocessing: N4 bias-field correction, z-score normalization, isotropic resampling, optional template registration — plus a slice-montage QC report.<br><br>**Python · SimpleITK · nibabel · matplotlib** | **[anatomical-seg-benchmark-qc](https://github.com/FatemehSharbati/anatomical-seg-benchmark-qc)**<br>Honest benchmarking harness for anatomical segmentation tools (TotalSegmentator, SynthSeg): per-label Dice, HD95, volume similarity and overlay visualizations.<br><br>**Python · NumPy · SciPy · nibabel** |
| **[brats-tumor-segmentation-nnunet](https://github.com/FatemehSharbati/brats-tumor-segmentation-nnunet)**<br>Brain tumor segmentation on BraTS: raw-data converter for nnU-Net v2, MONAI SegResNet training, and WT / TC / ET Dice evaluation.<br><br>**Python · PyTorch · MONAI · nnU-Net** | **[unsupervised-mri-anomaly-detection](https://github.com/FatemehSharbati/unsupervised-mri-anomaly-detection)**<br>Convolutional autoencoders trained on healthy brain MRI; lesions surface as reconstruction-error anomaly maps. No labels needed.<br><br>**Python · PyTorch · scikit-learn** |
| **[radiology-mini-vlm](https://github.com/FatemehSharbati/radiology-mini-vlm)**<br>Educational CLIP-style text-to-image retrieval for radiology, plus a subgroup fairness audit (per-group AUROC with bootstrap CIs).<br><br>**Python · open-CLIP · pandas · scikit-learn** | *More coming —* this profile is built in public, one project at a time. |

---

## GitHub stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=FatemehSharbati&show_icons=true&theme=dark" alt="GitHub stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=FatemehSharbati&layout=compact&theme=dark" alt="Top languages"/>
</div>
