
# 📊 Smart Data Analyzer

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-app-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Smart Data Analyzer is a **Python-based data exploration and reporting tool**.  
It allows users to upload CSV/Excel datasets, analyze data, generate statistics, create visualizations, and export PDF reports.  
The project provides both a **Command-Line Interface (CLI)** and an **interactive Streamlit dashboard**.

---

## 🚀 Features
- 📂 Load CSV and Excel datasets  
- 🔍 Summarize datasets (shape, types, missing values)  
- 📊 Generate statistics (mean, median, std, etc.)  
- 📉 Create visualizations (histogram, scatter, correlation heatmap)  
- 📝 Export PDF reports with charts  
- 🎛 Interactive Streamlit web dashboard  

---

## ⚡ Quickstart
```bash
git clone https://github.com/<your-username>/smart-data-analyzer.git
cd smart-data-analyzer
pip install -r requirements.txt
```

Run CLI:
```bash
python -m src.cli --file data/sample_sales.csv --report
```

Run Streamlit:
```bash
streamlit run src/app.py
```

---

## 🛠 Tech Stack
- Python 3.9+
- Pandas & NumPy
- Matplotlib & Seaborn
- Streamlit
- ReportLab

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).
