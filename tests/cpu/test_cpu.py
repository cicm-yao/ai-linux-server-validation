import json


def test_cpu_information_available():

    with open("inventory/reports/inventory_report.json") as file:
        inventory = json.load(file)

    cpu_info = inventory["cpu"]

    assert cpu_info != ""
