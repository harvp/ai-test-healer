# src/main.py
import os
from utils import parse_katalon_report
from healer import suggest_fix

if __name__ == "__main__":
    #report_path = "/data/reports/sample_katalon_report.xml"
    current_dir = os.path.dirname(os.path.abspath(__file__))  # src/
    report_path = os.path.join(current_dir, "../data/reports/sample_katalon_report.xml")
    report_path = os.path.normpath(report_path) 
    failures = parse_katalon_report(report_path)
    print("Failures found:")
    for f in failures:
        print("-", f)
        print("\nAI Suggestion:")
        print(suggest_fix(f))
