import subprocess
import json
import time
from datetime import datetime


def run_test(test_path):

    print("\nRunning:", test_path)

    start_time = time.time()

    result = subprocess.run(
        [
            "pytest-3",
            test_path
        ]
    )

    duration = time.time() - start_time

    if result.returncode == 0:
        status = "PASS"
    else:
        status = "FAIL"

    print(status + ":", test_path)

    return {
        "test": test_path,
        "result": status,
        "duration": round(duration, 2)
    }


def main():

    tests = [
        "tests/cpu/test_cpu.py",
        "tests/cpu/test_cpu_stress.py",
        "tests/memory/test_memory_stress.py",
        "tests/storage/test_storage_fio.py"
    ]

    results = []

    for test in tests:
        results.append(run_test(test))


    report = {
        "project": "Linux Server Validation",
        "run_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": results
    }


    with open(
        "reports/validation_report.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print("\nReport generated:")
    print("reports/validation_report.json")


if __name__ == "__main__":
    main()
