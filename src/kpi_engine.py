import pandas as pd

def calculate_productivity_trends(df: pd.DataFrame) -> dict:
    """
    Processes raw workforce data to generate insights into 
    time allocation, task organization, and productivity trends.
    """
    print("Calculating productivity metrics...")
    
    # Clean the data: drop rows where critical info is missing
    df = df.dropna(subset=['logged_hours', 'department'])
    
    # KPI 1: Overall Time Allocation (Total hours per department)
    time_allocation = df.groupby('department')['logged_hours'].sum().reset_index()
    
    # KPI 2: Focus Trends (Average focus score by role)
    # Using .round(2) to keep the numbers clean for the final report
    if 'focus_score' in df.columns:
        focus_trends = df.groupby('role')['focus_score'].mean().round(2).reset_index()
    else:
        focus_trends = pd.DataFrame(columns=['role', 'focus_score'])
        
    # Return a dictionary of dataframes so we can easily pass them into our PDF
    return {
        "time_allocation": time_allocation,
        "focus_trends": focus_trends
    }