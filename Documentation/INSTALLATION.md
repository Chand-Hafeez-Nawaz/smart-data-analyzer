# Installation Guide

## Requirements
- Python 3.9+
- pip package manager

## Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Chand-Hafeez-Nawaz/Smart-Data-Analyzer.git
   cd Smart-Data-Analyzer
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running
- CLI Mode:
  ```bash
  python -m src.cli --file data/sample_sales.csv --report
  ```
- Streamlit Dashboard:
  ```bash
  streamlit run src/app.py
  ```