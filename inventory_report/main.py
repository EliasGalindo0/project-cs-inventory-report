import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    if "csv" in sys.argv[1]:
        instance = InventoryRefactor(CsvImporter)
        result = instance.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(result)
    if "json" in sys.argv[1]:
        instance = InventoryRefactor(JsonImporter)
        result = instance.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(result)
    if "xml" in sys.argv[1]:
        instance = InventoryRefactor(XmlImporter)
        result = instance.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(result)