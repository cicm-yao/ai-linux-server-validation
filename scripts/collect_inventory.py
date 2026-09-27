import subprocess


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

    print("=== Kernel ===")
    print(run_command("uname -a"))

    print("\n=== CPU ===")
    print(run_command("lscpu | grep 'Model name'"))

    print("\n=== Memory ===")
    print(run_command("free -h | grep Mem"))

    print("\nInventory collection finished.")


if __name__ == "__main__":
    main()
