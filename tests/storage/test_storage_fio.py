import subprocess


def test_storage_fio():

    log_file = "evidence/storage/storage_fio.log"

    result = subprocess.run(
        [
            "fio",
            "--name=test_io",
            "--filename=/tmp/testfile",
            "--size=100M",
            "--rw=read",
            "--bs=4k",
            "--runtime=10",
            "--time_based"
        ],
        capture_output=True,
        text=True
    )

    with open(log_file, "w") as file:
        file.write(result.stdout)
        file.write(result.stderr)

    assert result.returncode == 0
