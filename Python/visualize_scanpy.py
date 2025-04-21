import scanpy as sc
import matplotlib.pyplot as plt

# Load data
adata = sc.read_h5ad("data/tumor_data.h5ad")

# Top tumor-related genes
genes = ["EPCAM", "KRT18", "MUC1", "TP53", "CD44", "GAPDH", "ACTB", "FN1", "CDH1", "VIM"]

# Generate plots
sc.pl.violin(adata, keys=genes, rotation=90, save="_violin.png")
sc.pl.heatmap(adata, var_names=genes, groupby=None, save="_heatmap.png")
sc.pl.dotplot(adata, var_names=genes, groupby=None, save="_dotplot.png")
sc.pl.matrixplot(adata, var_names=genes, groupby=None, save="_matrixplot.png")
