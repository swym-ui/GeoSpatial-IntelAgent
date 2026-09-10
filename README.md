# 🛰️ Geospatial Intelligence Agent

> AI + GIS pipeline for **satellite-based change detection, retrieval, and intelligent querying**.  
> Built with **PyTorch, LangChain, FAISS, rasterio, and geopandas**.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Tests](https://github.com/msmasood/Geospatial-Intelligence-Agent/actions/workflows/python-app.yml/badge.svg)
[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-blue)](https://www.kaggle.com/isaqibmasood)

---

## 🎯 What It Does
- Ingests **satellite imagery** (Sentinel/Landsat)  
- Runs **preprocessing**: reprojection, NDVI, tiling  
- Detects **changes** (forest loss, urban expansion, flooding, etc.)  
- Stores embeddings in **FAISS** for **retrieval-augmented querying**  
- Exposes results via **FastAPI** + **Streamlit demo**  
- Provides **Kaggle Notebook** for reproducibility  

---

## 🚀 Quickstart (Local Demo)

```bash
# clone repo
git clone https://github.com/msmasood/Geospatial-Intelligence-Agent.git
cd Geospatial-Intelligence-Agent

# create virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run notebooks
jupyter notebook notebooks/01_EDA.ipynb

# run Streamlit demo
streamlit run streamlit_app.py
