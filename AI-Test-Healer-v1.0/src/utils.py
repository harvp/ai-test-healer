import xml.etree.ElementTree as ET

def parse_katalon_report(path):
    tree = ET.parse(path)
    root = tree.getroot()
    failures = []
    for test_case in root.findall(".//testcase"):
        failure = test_case.find("failure")
        if failure is not None:
            name = test_case.get("name", "Unnamed Test")
            message = failure.get("message", "No message")
            failures.append(f"{name}: {message}")
    return failures
