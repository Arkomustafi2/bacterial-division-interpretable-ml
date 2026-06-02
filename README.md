\# Interpretable ML for Bacterial Division Prediction



\*\*Paper:\*\* Early Warning Signal Features Dominate Morphological 

Predictors in Bacterial Division Prediction: An Interpretable 

Pipeline with Uncertainty Quantification



\*\*Author:\*\* Arko Mustafi, Department of EEE, University of Dhaka  

\*\*Supervisor:\*\* Dr. S. M. Mostofa Al Mamun  

\*\*Status:\*\* Submitted to PLOS Computational Biology, May 2026



\---



\## What This Repository Contains



An interpretable, uncertainty-aware machine learning pipeline for 

predicting bacterial cell division behaviour from phase-contrast 

time-lapse microscopy. The pipeline combines:



\- XGBoost + SHAP feature attribution

\- ResNet-18 + Grad-CAM spatial interpretability

\- Monte Carlo Dropout uncertainty estimation

\- Split conformal prediction with coverage guarantees

\- Cross-species morphological validation (DeepBacs)



All analysis runs on consumer CPU hardware. No GPU required.



\---



\## Data



This study uses two publicly available datasets.



\*\*DeLTA 2.0 test sequences:\*\*  

Clone from: https://gitlab.com/dunloplab/delta  

Use the test/ directory MAT files.



\*\*DeepBacs:\*\*  

\- E. coli: https://zenodo.org/record/5550935  

\- B. subtilis: https://zenodo.org/record/5550968  

\- S. aureus: included in the DeepBacs repository



Place downloaded data in the data/ directory before running notebooks.



\---



\## Reproducibility



Run notebooks in order (01 → 06). Each notebook is self-contained 

with inline explanations.



Install dependencies:

```bash

pip install -r requirements.txt

```



\---



\## Results Summary



| Model | AUROC (CV) | MCC (CV) |

|---|---|---|

| Logistic Regression | 0.774 ± 0.025 | 0.404 ± 0.047 |

| Random Forest | 0.958 ± 0.011 | 0.726 ± 0.058 |

| XGBoost | 0.974 ± 0.005 | 0.780 ± 0.047 |

| ResNet-18 (test set) | 0.828 | 0.503 |



SHAP identified lag-1 autocorrelation of growth rate as the dominant 

predictor (mean |SHAP| = 2.07 ± 0.10, top-5 in 150/150 bootstrap runs).



\---





