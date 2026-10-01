import subprocess
from pathlib import Path
from datetime import datetime
import json
import sys


RUN_ROOT = Path("runs")


def collect_command(cmd, output):

    with open(output, "w") as f:
        result = subprocess.run(
            cmd,
            stdout=f,
            stderr=subprocess.STDOUT,
            text=True
        )


def main():

    testcase = sys.argv[1]

    run_id = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    run_dir = RUN_ROOT / run_id

    system_dir = run_dir / "system"

    system_dir.mkdir(
        parents=True,
        exist_ok=True
    )


    collect_command(
        ["dmesg"],
        system_dir/"dmesg.log"
    )


    collect_command(
        ["journalctl","-n","200"],
        system_dir/"journal.log"
    )


    collect_command(
        ["lspci","-nn"],
        system_dir/"lspci.txt"
    )


    collect_command(
        ["lsblk"],
        system_dir/"lsblk.txt"
    )


    collect_command(
        ["ip","-br","link"],
        system_dir/"ip_link.txt"
    )


    metadata = {

        "testcase":
        testcase,

        "timestamp":
        run_id,

        "evidence_path":
        str(run_dir)

    }


    with open(
        run_dir/"testcase.json",
        "w"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4
        )


    print(
        f"Evidence collected: {run_dir}"
    )


if __name__=="__main__":
    main()
