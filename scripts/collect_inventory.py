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


def main():

    print("Collecting system inventory...\n")

    kernel = run_command("uname -a")
    cpu = run_command("lscpu | grep 'Model name'")
    memory = run_command("free -h | grep Mem")

    inventory = {
        "kernel": kernel,
        "cpu": cpu,
        "memory": memory
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
