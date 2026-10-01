import yaml
import subprocess
import json
import datetime
import sys
from pathlib import Path


PLAN_FILE = "regression/regression_plan.yaml"
REPORT_FILE = "reports/regression_report.json"
MAP_FILE = "config/failure_regression_map.yaml"
RCA_FILE = "reports/rca_report.json"

def load_plan():

    with open(PLAN_FILE, "r") as file:
        return yaml.safe_load(file)
def load_failure_map():
   with open(MAP_FILE, "r") as file:
        return yaml.safe_load(file)
def load_rca():

    with open(RCA_FILE, "r") as file:
        return json.load(file)
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

    failure_map = load_failure_map()
    rca = load_rca()
    results = []


    selected_cases = None
    triggered_failure = None
    recovery_action = None

    if len(sys.argv) > 1:

        failure_id = sys.argv[1]
        triggered_failure = failure_id
        selected_cases = failure_map["failure_mapping"].get(
            failure_id,
            {}
        ).get(
            "regression_cases",
            []
        )

        print(
            f"Triggered by failure: {failure_id}"
        )


    for item in plan["regression_suite"]:


        if selected_cases:

            if item["id"] not in selected_cases:
                continue


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
         "trigger_failure":
        triggered_failure,
        "recovery_action":
    rca.get(
        "suggestion",
        "Not available"
    ),
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
