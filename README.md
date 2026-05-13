AutoReporter is a Python-based automation pipeline designed to ingest raw workforce data, calculate key productivity metrics, and generate professional, high-readability PDF reports. The system includes a built-in scheduler to dispatch these reports via email automatically.

🚀 Features
Data Processing: Uses pandas to parse and analyze employee time-tracking logs.

KPI Engine: Automatically calculates departmental time allocation and role-based focus scores.

Dynamic Templating: Uses Jinja2 to inject data into HTML templates.

Enterprise Styling: Features a custom "Slate & Indigo" theme designed to reduce cognitive load for HR managers.

PDF Generation: Converts styled HTML into PDF documents using wkhtmltopdf.

Automated Dispatch: Integrated SMTP mailer with background scheduling via APScheduler.

🛠️ Tech Stack
Language: Python 3.x

Libraries: Pandas, Jinja2, pdfkit, APScheduler, python-dotenv

Engine: wkhtmltopdf

Environment: Virtual Environment (venv) with .env for secure credential management.# AutoReporter
