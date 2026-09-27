import subprocess


def test_cpu_stress():

    log_file = "evidence/cpu/cpu_stress.log"

    result = subprocess.run(
        [
            "stress-ng",
            "--cpu",
            "2",
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
