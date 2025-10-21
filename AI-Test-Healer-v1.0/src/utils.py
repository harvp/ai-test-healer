# src/utils.py
import pandas as pd
import glob
import os
import re
import xml.etree.ElementTree as ET

def parse_katalon_report(report_path):
    """Parse Katalon report CSV and extract failed test names and error messages."""
    import csv

    failures = []
    with open(report_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Adjust these field names to match your CSV columns
            test_name = row.get("Test Case") or row.get("Test Name")
            status = row.get("Status", "").lower()
            error = row.get("Message") or row.get("Error Message") or ""

            if status == "failed":
                failures.append({
                    "Test Case": test_name.strip(),
                    "Error Message": error.strip()
                })

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

def find_test_object_file(base_repo_path, object_ref):
    file_path = os.path.join(base_repo_path, object_ref.replace("/", os.sep) + ".rs")
    if os.path.isfile(file_path):
        return file_path
    return None

def get_xpath_from_rs(rs_path):
    try:
        tree = ET.parse(rs_path)
        root = tree.getroot()
        for entry in root.findall(".//entry"):
            key = entry.find("key")
            if key is not None and key.text == "XPATH":
                value = entry.find("value")
                if value is not None:
                    return value.text
        return None
    except Exception as e:
        print(f"Error parsing {rs_path}: {e}")
        return None

def extract_test_object_refs(candidate_lines):
    refs = set()
    pattern = r"findTestObject\(['\"](.+?)['\"]\)"
    for _, line in candidate_lines:
        matches = re.findall(pattern, line)
        refs.update(matches)
    return list(refs)