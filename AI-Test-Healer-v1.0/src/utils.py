# src/utils.py
import pandas as pd

def parse_katalon_report(path):
    """
    Reads a Katalon CSV report and returns a list of failed test cases with error messages.
    """
    df = pd.read_csv(path)
    
    # Filter rows where Status is FAILED
    failed = df[df["Status"] == "FAILED"]
    
    # Extract test case and error message
    failures = []
    for _, row in failed.iterrows():
        test_case = row["Test Case"]
        error_message = row["Error Message"]
        failures.append(f"{test_case}: {error_message}")
    
    return failures
