import json


def generate_rca_summary(evidence):

    summary = {

        "observed_facts": evidence.get(
            "facts",
            []
        ),

        "possible_causes": [],

        "recommended_checks": [

            "ip link show",

            "ethtool",

            "dmesg"

        ],

        "confidence": "medium"

    }


    if "network" in evidence.get("keywords", []):

        summary["possible_causes"].append(
            "Network interface configuration issue"
        )

        summary["possible_causes"].append(
            "NIC link or driver problem"
        )


    return summary



if __name__ == "__main__":

    import sys


    if len(sys.argv) < 2:

        print(
            "Usage: python rca_assistant.py evidence.json"
        )

        exit(1)


    with open(sys.argv[1], "r") as f:

        evidence = json.load(f)


    result = generate_rca_summary(evidence)

    with open(
        "reports/ai_rca_report.json",
        "w"
    ) as f:
        json.dump(
            result,
            f,
            indent=4
    )

    
    print(
        json.dumps(
            result,
            indent=4
        )
    )

