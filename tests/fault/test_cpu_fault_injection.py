import subprocess
import time


def test_cpu_fault_injection():

    log_file = "evidence/fault/cpu_fault.log"

    process = subprocess.Popen(
        [
            "stress-ng",
            "--cpu",
            "2",
            "--timeout",
            "20s"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    time.sleep(5)

    if process.poll() is None:
        status = "Fault injection running"

    stdout, stderr = process.communicate()

    with open(log_file, "w") as file:
        file.write(status + "\n")
        file.write(stdout)
        file.write(stderr)

    assert process.returncode == 0
