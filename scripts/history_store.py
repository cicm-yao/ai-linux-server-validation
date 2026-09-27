import json
import os
from datetime import datetime


HISTORY_FILE = "history/rca_history.json"


def save_rca_case(rca_report):

    history = []


    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)


    case = {

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "failure_id":
            rca_report.get(
                "failure_id",
                "Unknown"
            ),

        "component":
            rca_report.get(
                "component",
                "Unknown"
            ),

        "root_cause":
            rca_report.get(
                "root_cause",
                "Unknown"
            ),

        "confidence":
            rca_report.get(
                "confidence",
                0
            ),

        "matched_keywords":
            rca_report.get(
                "matched_keywords",
                []
            ),

        "suggestion":
            rca_report.get(
                "suggestion",
                "Unknown"
            ),

        "evidence":
            rca_report.get(
                "evidence",
                "Unknown"
            )
    }


    history.append(case)


    with open(HISTORY_FILE, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )


    print("RCA case saved")


if __name__ == "__main__":

    with open(
        "reports/rca_report.json",
        "r"
    ) as file:

        report = json.load(file)


    save_rca_case(report)
