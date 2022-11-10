import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


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


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):
        result = self.importer().import_data(path)
        self.data += result

        if type == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)
