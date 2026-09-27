import json
import sys
from knowledge_loader import load_knowledge


def analyze_failure():

    # Evidence log
    if len(sys.argv) < 2:
        print("Usage: python3 rca_analyzer.py <evidence_log>")
        sys.exit(1)


    log_file = sys.argv[1]


    # Read log
    with open(log_file, "r") as file:
        log = file.read()


    # Load knowledge base
    knowledge = load_knowledge()


    result =  {
         "failure_id": "Unknown",
        "evidence": log_file,
        "component": "Unknown",
        "root_cause": "Unknown",
        "suggestion": "Unknown",
        "confidence": 0,
        "matched_keywords": []
    }


    best_match = None
    best_score = 0
    best_keywords = []


    # Weighted matching
    for failure in knowledge:

        score = 0
        matched = []


        for keyword in failure.get("keywords", []):

            text = keyword["text"]
            weight = keyword["weight"]


            if text in log:

                score += weight
                matched.append(text)


        # Keep highest score
        if score > best_score:

            best_score = score
            best_match = failure
            best_keywords = matched



    # Generate RCA result

    if best_match:
        result["failure_id"] = best_match.get(
             "id",
             "Unknown"
        )

        result["component"] = best_match.get(
            "component",
            "Unknown"
        )

        result["root_cause"] = best_match.get(
            "root_cause",
            "Unknown"
        )

        result["suggestion"] = best_match.get(
            "recommended_action",
            "Unknown"
        )

        result["confidence"] = best_score

        result["matched_keywords"] = best_keywords



    # Write RCA report

    with open(
        "reports/rca_report.json",
        "w"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )


    print("RCA report generated:")
    print("reports/rca_report.json")



if __name__ == "__main__":

    analyze_failure()
