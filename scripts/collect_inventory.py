import subprocess
import json


def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def collect_kernel():
    return run_command("uname -a")


def collect_cpu():
    return run_command("lscpu | grep 'Model name'")


def collect_memory():
    return run_command("free -h | grep Mem")


def collect_storage():
    return run_command("lsblk")


def collect_network():
    return run_command("ip -br link")


def main():

    print("Collecting system inventory...\n")

    inventory = {
        "kernel": collect_kernel(),
        "cpu": collect_cpu(),
        "memory": collect_memory(),
        "storage": collect_storage(),
        "network": collect_network()
    }

    output_file = "inventory/reports/inventory_report.json"

    with open(output_file, "w") as file:
        json.dump(
            inventory,
            file,
            indent=4
        )

    print("Inventory report generated:")
    print(output_file)


if __name__ == "__main__":
    main()
