from utils import parse_katalon_report, find_groovy_file, extract_candidate_lines
from healer import suggest_fix
import glob, os

if __name__ == "__main__":
    base_scripts_path = os.path.join(os.getcwd(), "data", "groovy_scripts")
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
                    print(f"  - {f['Test Case']}: {f['Error Message'][:100]}...")  # truncated for readability

                    print("\n  AI Suggestion:")
                    print("   ", suggest_fix(f))

                    groovy_path = find_groovy_file(base_scripts_path, f["Test Case"])
                    print(f"\nTest Case: {f['Test Case']}")
                    print("Groovy path:", groovy_path)
                    
                    candidate_lines = extract_candidate_lines(groovy_path, f["Error Message"])
                    print("Candidate lines:")
                    for lineno, line in candidate_lines:
                        print(f"{lineno}: {line}")
