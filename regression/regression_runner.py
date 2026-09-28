import yaml
import subprocess
import json
import datetime
from pathlib import Path


PLAN_FILE = "regression/regression_plan.yaml"
REPORT_FILE = "reports/regression_report.json"


def load_plan():

    with open(PLAN_FILE, "r") as file:
        return yaml.safe_load(file)


def run_test(test_path):

    print(f"Running regression test: {test_path}")

    result = subprocess.run(
        [
            "pytest",
            test_path
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        status = "PASS"
    else:
        status = "FAIL"

    return {
        "test": test_path,
        "result": status,
        "stdout": result.stdout,
        "stderr": result.stderr
    }


def main():

    print("Starting regression test...\n")

    plan = load_plan()

    results = []

    for item in plan["regression_suite"]:

        result = run_test(
            item["test"]
        )

        result["test_id"] = item["id"]

        results.append(result)


    report = {

        "project":
        "Linux Server Validation",

        "type":
        "Regression",

        "time":
        str(datetime.datetime.now()),

        "results":
        results
    }


    Path("reports").mkdir(
        exist_ok=True
    )


    with open(
        REPORT_FILE,
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print("\nRegression report generated:")
    print(REPORT_FILE)



if __name__ == "__main__":
    main()
