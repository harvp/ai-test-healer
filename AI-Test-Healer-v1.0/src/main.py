# src/main.py
from utils import (
    parse_katalon_report,
    find_groovy_file,
    extract_candidate_lines,
    find_test_object_file,
    get_xpath_from_rs,
    extract_test_object_refs
)
from healer import suggest_fix
from classifier import classify_failure
import glob, os

def print_failure_summary(failure, category, candidate_lines, groovy_path, object_xpaths):
    print("\n" + "="*60)
    print(f"Test Case: {failure['Test Case']}")
    print(f"Category: {category['name']}")
    if category['name'] == "Unknown":
        print("(General troubleshooting suggested)")
    print("AI Focus:", ", ".join(category['ai_focus']))
    print(f"Error (truncated): {failure['Error Message'][:100]}...")
    print(f"Groovy Path: {groovy_path}")
    
    print("Candidate Lines:")
    if candidate_lines:
        for lineno, line in candidate_lines:
            print(f"{lineno}: {line}")
    else:
        print("  No candidate lines found.")
    
    if object_xpaths:
        print("Resolved Test Object XPaths:")
        for obj, xpath in object_xpaths.items():
            print(f"  {obj}: {xpath}")
    
    print("AI Suggestion:")
    print("   ", suggest_fix(failure))
    print("="*60 + "\n")

if __name__ == "__main__":
    base_scripts_path = os.path.join(os.getcwd(), "data", "groovy_scripts")
    obj_repo_path = os.path.join(os.getcwd(), "data", "test_objects")
    report_files = glob.glob("data/reports/*.csv")

    if not report_files:
        print("No report files found!")
    else:
        for report_path in report_files:
            print(f"\nProcessing report: {report_path}")
            failures = parse_katalon_report(report_path)

            if not failures:
                print("  No failures found in this report.")
            else:
                print(f"  Failures found: {len(failures)}")
                for f in failures:
                    # Classify the failure
                    category = classify_failure(f["Error Message"])

                    # Find Groovy path and candidate lines
                    groovy_path = find_groovy_file(base_scripts_path, f["Test Case"])
                    candidate_lines = extract_candidate_lines(groovy_path, f["Error Message"])
                    
                    # Extract test object references and resolve XPaths
                    object_refs = extract_test_object_refs(candidate_lines)
                    object_xpaths = {}
                    for ref in object_refs:
                        rs_path = find_test_object_file(obj_repo_path, ref)
                        if rs_path:
                            xpath = get_xpath_from_rs(rs_path)
                            object_xpaths[ref] = xpath
                        else:
                            object_xpaths[ref] = None
                    
                    # Attach context for future AI use
                    f["Groovy Context"] = "\n".join(f"{lineno}: {line}" for lineno, line in candidate_lines)
                    f["TestObjectXPaths"] = object_xpaths

                    # Print a grouped summary
                    print_failure_summary(f, category, candidate_lines, groovy_path, object_xpaths)
