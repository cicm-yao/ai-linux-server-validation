import yaml
import json


def analyze_failure():

    log_file = "evidence/fault/cpu_fault.log"

    with open(log_file, "r") as file:
        log = file.read()


    with open("rca/rules.yaml", "r") as file:
        rules = yaml.safe_load(file)


    result = {
        "evidence": log_file,
        "component": "Unknown",
        "root_cause": "Unknown",
        "suggestion": "Unknown"
    }


    for rule in rules["rules"]:

        if rule["keyword"] in log:

            result["component"] = rule["component"]
            result["root_cause"] = rule["root_cause"]
            result["suggestion"] = rule["suggestion"]

            break


    with open(
        "reports/rca_report.json",
        "w"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )


    print("RCA report generated")
    print("reports/rca_report.json")


if __name__ == "__main__":
    analyze_failure()
