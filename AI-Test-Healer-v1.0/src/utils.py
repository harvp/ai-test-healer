# src/utils.py
import pandas as pd
import glob
import os
import re

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


def find_groovy_file(base_path, test_case_name):
    """
    Finds the Groovy file corresponding to a given test case.
    
    Args:
        base_path (str): The root folder containing all Scripts.
        test_case_name (str): The Test Case name from the CSV.
        
    Returns:
        str or None: Path to the Groovy file if found, else None.
    """
    folder_path = os.path.join(base_path, "**", test_case_name)
    files = glob.glob(os.path.join(folder_path, "*.groovy"), recursive=True)
    if files:
        return files[0]  # only one expected per folder
    return None

def extract_candidate_lines(groovy_path, error_message, max_lines=5):
    """
    Reads a Groovy script and finds lines that likely caused the error.
    
    Args:
        groovy_path (str): Path to the Groovy file.
        error_message (str): Error message from the CSV.
        max_lines (int): Maximum number of lines to return.
        
    Returns:
        List of tuples: (line_number, line_content)
    """
    if not groovy_path or not os.path.isfile(groovy_path):
        return []

    candidates = []
    with open(groovy_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Extract keywords from the error message (element IDs, class names, text, etc.)
    # This is a simple heuristic; can improve later with regex patterns
    keywords = re.findall(r"['\"]?([\w\-]+)['\"]?", error_message)

    for i, line in enumerate(lines):
        if any(keyword in line for keyword in keywords):
            candidates.append((i + 1, line.strip()))
            if len(candidates) >= max_lines:
                break

    return candidates