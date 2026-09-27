import subprocess
import json


def run_test(test_path):

    print("\nRunning:", test_path)

    result = subprocess.run(
        [
            "pytest-3",
            test_path
        ]
    )

    if result.returncode == 0:
        status = "PASS"
    else:
        status = "FAIL"

    print(status + ":", test_path)

    return {
        "test": test_path,
        "result": status
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
