import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

# Explicitly tell Python where the engine was installed on your Windows machine
# We use r"..." to ensure the backslashes don't break the path
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

def create_pdf_report(kpis: dict, output_filename: str = "weekly_report.pdf") -> str:
    """
    Injects KPI data into the HTML template and renders a PDF.
    """
    print("Applying Slate & Indigo styling and generating PDF...")
    
    # Verify the engine exists before trying to run it
    if not os.path.exists(WKHTMLTOPDF_PATH):
        raise FileNotFoundError(f"CRITICAL: wkhtmltopdf not found at {WKHTMLTOPDF_PATH}. Did you install it?")

    # Load the HTML template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')
    
    # Convert our pandas DataFrames into raw HTML tables
    html_out = template.render(
        time_table=kpis['time_allocation'].to_html(index=False, border=0),
        focus_table=kpis['focus_trends'].to_html(index=False, border=0)
    )
    
    # Convert that styled HTML string into a PDF file using our config
    pdfkit.from_string(html_out, output_filename, configuration=config)
    
    print(f"Report successfully generated: {output_filename}")
    return output_filename