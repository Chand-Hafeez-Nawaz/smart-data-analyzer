
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")

def _ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def plot_histogram(df: pd.DataFrame, column: str, filename: str = None) -> str:
    _ensure_reports_dir()
    if filename is None:
        filename = f"hist_{column}.png"
    path = os.path.join(REPORTS_DIR, filename)
    plt.figure(figsize=(6, 4))
    sns.histplot(df[column].dropna(), kde=True, bins=30)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    return path

def plot_scatter(df: pd.DataFrame, x: str, y: str, filename: str = None) -> str:
    _ensure_reports_dir()
    if filename is None:
        filename = f"scatter_{x}_vs_{y}.png"
    path = os.path.join(REPORTS_DIR, filename)
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df[x], y=df[y])
    plt.title(f"{x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    return path

def plot_correlation_heatmap(df: pd.DataFrame, filename: str = "correlation_heatmap.png") -> str:
    _ensure_reports_dir()
    path = os.path.join(REPORTS_DIR, filename)
    plt.figure(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    return path
