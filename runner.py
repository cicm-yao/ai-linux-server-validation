import subprocess
import json
import time
from datetime import datetime


def get_evidence(test_path):

    evidence_map = {
        "tests/cpu/test_cpu.py":
            "inventory/reports/inventory_report.json",

        "tests/cpu/test_cpu_stress.py":
            "evidence/cpu/cpu_stress.log",

        "tests/memory/test_memory_stress.py":
            "evidence/memory/memory_stress.log",

        "tests/storage/test_storage_fio.py":
            "evidence/storage/storage_fio.log",

        "tests/network/test_network_check.py":
            "evidence/network/network_check.log"
    }

    return evidence_map.get(test_path, "N/A")

def run_rca():

    print("\nRunning RCA Analyzer...")

    result = subprocess.run(
        [
            "python3",
            "scripts/rca_analyzer.py"
        ]
    )

    if result.returncode == 0:
        print("RCA completed")
    else:
        print("RCA failed")

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
        "duration": round(duration, 2),
        "evidence": get_evidence(test_path)
    }


def main():

    tests = [
        "tests/cpu/test_cpu.py",
        "tests/cpu/test_cpu_stress.py",
        "tests/memory/test_memory_stress.py",
        "tests/storage/test_storage_fio.py",
        "tests/network/test_network_check.py"
    ]

    results = []

    failed = False

    for test in tests:
    
         result = run_test(test)

         results.append(result)

         if result["result"] == "FAIL":
            failed = True


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

    if failed:

        run_rca()

    print("\nReport generated:")
    print("reports/validation_report.json")


if __name__ == "__main__":
    main()
