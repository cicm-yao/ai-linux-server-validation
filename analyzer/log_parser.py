import json
from pathlib import Path


def parse_log(log_file):

    path = Path(log_file)

    if not path.exists():
        raise FileNotFoundError(log_file)

    with open(path, "r") as f:
        content = f.read().lower()

    result = {
        "source_log": str(path),
        "keywords": [],
        "facts": []
    }

    keywords = [
        "network",
        "unavailable",
        "failed",
        "down"
    ]

    for keyword in keywords:
        if keyword in content:
            result["keywords"].append(keyword)


    if "network unavailable" in content:
        result["facts"].append(
            "Network unavailable condition detected"
        )

    if "ens33" in content:
        result["facts"].append(
            "Network interface state collected"
        )


    return result



if __name__ == "__main__":

    import sys

    if len(sys.argv) < 2:
        print(
            "Usage: python log_parser.py <log_file>"
        )
        exit(1)


    result = parse_log(sys.argv[1])

    print(
        json.dumps(
            result,
            indent=4
        )
    )
