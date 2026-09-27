import sys
import os

sys.path.append(
    os.path.abspath(".")
)

from fault_injection.cpu.cpu_stress import inject_cpu_fault


def test_cpu_fault_injection():

    log_file = "evidence/fault/cpu_fault.log"

    result = inject_cpu_fault()


    with open(log_file, "w") as file:

        file.write(
            result["stdout"]
        )

        file.write(
            result["stderr"]
        )


    assert result["return_code"] == 0
