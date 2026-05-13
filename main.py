import os
from apscheduler.schedulers.blocking import BlockingScheduler
from src.ingest import load_data
from src.kpi_engine import calculate_productivity_trends
from src.report_builder import create_pdf_report
from src.mailer import send_email

def run_pipeline():
    """The main execution flow: Ingest -> Calculate -> Build -> Send"""
    print("--- STARTING AUTOREPORTER PIPELINE ---")
    try:
        # 1. Ingest
        raw_data = load_data('data/raw_data.csv')
        
        # 2. Calculate
        kpis = calculate_productivity_trends(raw_data)
        
        # 3. Build Report
        report_path = create_pdf_report(kpis, "weekly_workforce_report.pdf")
        
        # 4. Dispatch
        send_email(report_path)
        
        print("--- PIPELINE COMPLETED SUCCESSFULLY ---")
    except Exception as e:
        print(f"PIPELINE FAILED: {e}")

if __name__ == "__main__":
    # For testing, we run it once immediately before starting the scheduler
    run_pipeline()
    
    print("\nStarting background scheduler...")
    scheduler = BlockingScheduler()
    # Schedule the report to run automatically every Friday at 5:00 PM
    scheduler.add_job(run_pipeline, 'cron', day_of_week='fri', hour=17, minute=0)
    
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped by user.")