
import os
from typing import Dict, Any
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")

def generate_pdf_report(report_data: Dict[str, Any],
                        charts: Dict[str, str] = None,
                        filename: str = "data_report.pdf") -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    path = os.path.join(REPORTS_DIR, filename)
    doc = SimpleDocTemplate(path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [Paragraph("Smart Data Analyzer Report", styles['Title']), Spacer(1, 16)]

    for section, content in report_data.items():
        story.append(Paragraph(f"<b>{section}</b>", styles['Heading2']))
        if isinstance(content, dict):
            # render as simple key/value table
            data = [[str(k), str(v)] for k, v in content.items()]
            table = Table(data, hAlign='LEFT')
            story.append(table)
        else:
            story.append(Paragraph(str(content), styles['Normal']))
        story.append(Spacer(1, 12))

    if charts:
        story.append(Paragraph("<b>Charts</b>", styles['Heading2']))
        for title, img_path in charts.items():
            if img_path and os.path.exists(img_path):
                story.append(Paragraph(title, styles['Heading3']))
                story.append(Image(img_path, width=450, height=300))
                story.append(Spacer(1, 12))

    doc.build(story)
    return path
