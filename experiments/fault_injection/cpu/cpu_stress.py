import subprocess


def inject_cpu_fault(duration=20):

    process = subprocess.Popen(
        [
            "stress-ng",
            "--cpu",
            "2",
            "--timeout",
            f"{duration}s"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate()

    return {
        "return_code": process.returncode,
        "stdout": stdout,
        "stderr": stderr
    }


if __name__ == "__main__":

    result = inject_cpu_fault()

    print(result)
