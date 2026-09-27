import subprocess


def test_memory_stress():

    log_file = "evidence/memory/memory_stress.log"

    result = subprocess.run(
        [
            "stress-ng",
            "--vm",
            "1",
            "--vm-bytes",
            "512M",
            "--timeout",
            "10s"
        ],
        capture_output=True,
        text=True
    )

    with open(log_file, "w") as file:
        file.write(result.stdout)
        file.write(result.stderr)

    assert result.returncode == 0
