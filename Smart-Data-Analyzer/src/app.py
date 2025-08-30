
import streamlit as st
from analyzer import SmartDataAnalyzer
from visualization import plot_histogram, plot_scatter, plot_correlation_heatmap
from report_generator import generate_pdf_report

st.set_page_config(page_title="Smart Data Analyzer", layout="wide")
st.title("📊 Smart Data Analyzer")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx", "xls"])

if uploaded_file:
    analyzer = SmartDataAnalyzer(uploaded_file)

    st.subheader("🔍 Basic Information")
    st.json(analyzer.basic_info())

    st.subheader("📈 Statistics (describe)")
    st.json(analyzer.statistics())

    numeric_cols = analyzer.numeric_columns()
    if numeric_cols:
        st.subheader("📉 Visualizations")
        col1, col2, col3 = st.columns(3)

        with col1:
            hist_col = st.selectbox("Histogram column", options=numeric_cols, key="hist")
            if st.button("Create Histogram"):
                img = plot_histogram(analyzer.data, hist_col)
                st.image(img, caption=f"Histogram · {hist_col}", use_column_width=True)

        with col2:
            x_col = st.selectbox("Scatter X", options=numeric_cols, key="x")
            y_col = st.selectbox("Scatter Y", options=numeric_cols, key="y")
            if st.button("Create Scatter"):
                img = plot_scatter(analyzer.data, x_col, y_col)
                st.image(img, caption=f"Scatter · {x_col} vs {y_col}", use_column_width=True)

        with col3:
            if st.button("Create Correlation Heatmap"):
                img = plot_correlation_heatmap(analyzer.data)
                st.image(img, caption="Correlation Heatmap", use_column_width=True)

        st.divider()
        if st.button("Generate PDF Report"):
            info = analyzer.basic_info()
            charts = {}
            # Try to add last generated charts if they exist (simple heuristic)
            try:
                if hist_col:
                    charts[f"Histogram: {hist_col}"] = f"reports/hist_{hist_col}.png"
            except Exception:
                pass
            try:
                charts["Correlation Heatmap"] = "reports/correlation_heatmap.png"
            except Exception:
                pass

            path = generate_pdf_report({"Basic Info": info}, charts=charts)
            st.success(f"Report generated at {path}")
    else:
        st.info("No numeric columns detected to plot. You can still view basic info and stats.")
else:
    st.write("Upload a dataset to begin.")
