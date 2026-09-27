import subprocess


def test_network_interface():

    log_file = "evidence/network/network_check.log"

    result = subprocess.run(
        [
            "ip",
            "-br",
            "link"
        ],
        capture_output=True,
        text=True
    )

    with open(log_file, "w") as file:
        file.write(result.stdout)
        file.write(result.stderr)

    assert result.returncode == 0
    assert "ens33" in result.stdout
