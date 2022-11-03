import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def json_import_data(path, type):
    with open(path) as file:
        raw_data = json.load(file)
        data = [item for item in raw_data]
        return data


def xml_import_data(path, type):
    with open(path) as file:
        raw_data = file.read()
        data = xmltodict.parse(raw_data)["dataset"]["record"]
        return data


def csv_import_data(path, type):
    with open(path) as file:
        raw_data = csv.DictReader(file)
        data = [item for item in raw_data]
        return data


class Inventory:
    @staticmethod
    def import_data(path, type):
        if "json" in path:
            data = json_import_data(path, type)
        elif "xml" in path:
            data = xml_import_data(path, type)
        else:
            data = csv_import_data(path, type)
        if type == "simples":
            data = SimpleReport.generate(data)
        elif type == "completo":
            data = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo inválido")
        return data
