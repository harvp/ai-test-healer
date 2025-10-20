# src/main.py
import glob
from utils import parse_katalon_report
from healer import suggest_fix

if __name__ == "__main__":

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
                print("  Failures found:")
                for f in failures:
                    print("  -", f)
                    print("\n  AI Suggestion:")
                    print("   ", suggest_fix(f))

from utils import find_groovy_file, extract_candidate_lines

base_scripts_path = "../qa-automated-testing-collective-regression/Scripts"

test_case_name = "SPG - Verify Help My Account Options"
error_msg = "element click intercepted: Element <li data-v-2ba57165='' class='nav-item'>...</li> is not clickable"

groovy_path = find_groovy_file(base_scripts_path, test_case_name)
print("Groovy path:", groovy_path)

lines = extract_candidate_lines(groovy_path, error_msg)
for lineno, content in lines:
    print(f"{lineno}: {content}")