# Gene Expression Analysis of Tumor Cells Using Single-Cell RNA-seq

This project explores gene expression patterns in lung adenocarcinoma tumor cells using publicly available single-cell RNA sequencing data (GSE131907). The workflow involves preprocessing with **Seurat (R)** and visualizing expression trends using **Scanpy (Python)**.

## 🧪 Technologies Used
- Seurat (R)
- Scanpy (Python)
- Matplotlib, Seaborn
- NCBI GEO Data

## 📂 Folder Structure
- `R/`: Preprocessing scripts in R
- `Python/`: Visualization scripts in Python
- `data/`: Contains raw matrix files and converted data
- `outputs/plots/`: Final plots generated from the analysis

## 🧬 Key Genes Identified
- EPCAM, KRT18, MUC1, TP53, CD44, GAPDH, ACTB, FN1, CDH1, VIM

## 🚀 How to Run
```bash
# R preprocessing
Rscript R/preprocess_seurat.R

# Python visualization
python Python/visualize_scanpy.py
