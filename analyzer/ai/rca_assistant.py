import json
import requests

def call_ollama(prompt):

    url = "http://192.168.105.1:11434/api/generate"

    payload = {
        "model": "qwen3:4b",
        "prompt": prompt,
        "stream": False,
        "think": False
        
    }

    response = requests.post(
        url,
        json=payload,
        timeout=600
        )

    return response.json()["response"]


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

    ai_prompt = f"""
    You are a Linux server troubleshooting assistant.

    Analyze this failure evidence:

    {json.dumps(evidence, indent=2)}

    Provide:

    1. Failure summary
    2. Possible root causes
    3. Recommended checks
    """

    ai_result = call_ollama(ai_prompt)


    result["ai_analysis"] = ai_result

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

