import subprocess


def run_test(test_path):

    print("\nRunning:", test_path)

    result = subprocess.run(
        [
            "pytest-3",
            test_path
        ]
    )

    if result.returncode == 0:
        print("PASS:", test_path)
    else:
        print("FAIL:", test_path)


def main():

    tests = [
        "tests/cpu/test_cpu.py",
        "tests/cpu/test_cpu_stress.py",
        "tests/memory/test_memory_stress.py",
        "tests/storage/test_storage_fio.py"
    ]

    for test in tests:
        run_test(test)


if __name__ == "__main__":
    main()
