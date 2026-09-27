import subprocess


def test_cpu_stress():

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

    assert result.returncode == 0
