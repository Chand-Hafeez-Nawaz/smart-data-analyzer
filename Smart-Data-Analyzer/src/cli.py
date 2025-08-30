
import argparse
from .analyzer import SmartDataAnalyzer
from .visualization import plot_histogram, plot_scatter, plot_correlation_heatmap
from .report_generator import generate_pdf_report

def main():
    parser = argparse.ArgumentParser(description="Smart Data Analyzer CLI")
    parser.add_argument("--file", required=True, help="Path to CSV or Excel file")
    parser.add_argument("--hist", help="Column name for histogram")
    parser.add_argument("--scatter", nargs=2, metavar=("X", "Y"), help="Plot scatter of X vs Y")
    parser.add_argument("--heatmap", action="store_true", help="Generate correlation heatmap")
    parser.add_argument("--report", action="store_true", help="Generate PDF report")
    args = parser.parse_args()

    analyzer = SmartDataAnalyzer(args.file)
    info = analyzer.basic_info()
    stats = analyzer.statistics()

    print("=== Basic Info ===")
    print(info)
    print("\n=== Statistics (describe) ===")
    print(stats)

    charts = {}
    if args.hist and args.hist in analyzer.data.columns:
        charts[f"Histogram: {args.hist}"] = plot_histogram(analyzer.data, args.hist)
        print(f"Saved histogram for {args.hist}.")

    if args.scatter:
        x, y = args.scatter
        if x in analyzer.data.columns and y in analyzer.data.columns:
            charts[f"Scatter: {x} vs {y}"] = plot_scatter(analyzer.data, x, y)
            print(f"Saved scatter {x} vs {y}.")

    if args.heatmap:
        charts["Correlation Heatmap"] = plot_correlation_heatmap(analyzer.data)
        print("Saved correlation heatmap.")

    if args.report:
        path = generate_pdf_report(
            {"Basic Info": info, "Columns": {c: t for c, t in info["dtypes"].items()}},
            charts=charts
        )
        print(f"Report saved to: {path}")

if __name__ == "__main__":
    main()
