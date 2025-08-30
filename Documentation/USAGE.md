# Usage Examples

## CLI
Generate a PDF report with histogram:
```bash
python -m src.cli --file data/sample_sales.csv --hist Quantity --report
```

Generate correlation heatmap:
```bash
python -m src.cli --file data/sample_sales.csv --heatmap --report
```

## Streamlit Dashboard
1. Run the app:
   ```bash
   streamlit run src/app.py
   ```
2. Upload CSV/Excel file.
3. View:
   - Dataset summary
   - Statistics
   - Charts (histogram, scatter, heatmap)
4. Generate a **PDF Report** from UI.