import yaml
import json


def analyze_failure():

    with open(
        "rca/failure_cases.yaml",
        "r"
    ) as file:

        failure = yaml.safe_load(file)


    report = {
        "failure_id": failure["failure_id"],
        "component": failure["component"],
        "symptom": failure["symptom"],
        "evidence": failure["evidence"],
        "root_cause": failure["root_cause"],
        "recovery": failure["recovery"]
    }


    with open(
        "reports/rca_report.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print("RCA report generated:")
    print("reports/rca_report.json")


if __name__ == "__main__":
    analyze_failure()
