import subprocess
import yaml
import json
import time
from datetime import datetime


TEST_PLAN = "config/test_plan.yaml"
REPORT_FILE = "reports/validation_report.json"


def load_test_plan():
    """
    Load test cases from YAML
    """

    with open(TEST_PLAN, "r") as file:
        data = yaml.safe_load(file)

    return data["test_cases"]



def run_test(test_case):

    test_id = test_case["id"]
    script = test_case["script"]

    print("\n==============================")
    print(f"Running {test_id}")
    print(f"Script: {script}")
    print("==============================")


    start_time = time.time()


    result = subprocess.run(
        [
            "python3",
            "-m",
            "pytest",
            "-q",
            script
        ],
        capture_output=True,
        text=True
    )


    duration = time.time() - start_time


    if result.returncode == 0:
        status = "PASS"
    else:
        status = "FAIL"


    return {

        "test_case_id": test_id,

        "script": script,

        "status": status,

        "duration": round(duration,2),

        "output": result.stdout[-500:],

        "evidence": test_case.get(
            "evidence",
            []
        )
    }



def save_report(results):

    report = {

        "project":
        "AI-Augmented Linux Server System Validation",

        "run_time":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "results":
        results
    }


    with open(
        REPORT_FILE,
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print(
        "\nReport generated:"
    )

    print(REPORT_FILE)



def run_rca(results):
    subprocess.run(
    [
     "python3",
     "analyzer/ai/rca_assistant.py",
     "reports/structured_evidence.json"
    ]
    )

    for item in results:

        if item["status"] == "FAIL":

            evidence = item["evidence"]


            if evidence:

                print(
                    "\nFailure detected."
                )

                print(
                    "Evidence:"
                )

                print(
                    evidence
                )
                
                   # RCA
                subprocess.run(
                    [
                        "python3",
                        "scripts/rca_analyzer.py",
                        evidence[0]
                    ]
                )


                # History
                subprocess.run(
                    [
                        "python3",
                        "scripts/history_store.py"
                    ]
                )

def main():

    tests = load_test_plan()


    results = []


    for test in tests:

        result = run_test(test)
        subprocess.run(
        [
            "python3",
            "scripts/evidence_collector.py",
            test["id"]
        ]
    )

        results.append(result)



    save_report(results)


    run_rca(results)



if __name__ == "__main__":

    main()
