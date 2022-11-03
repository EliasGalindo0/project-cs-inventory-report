import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            raw_content = xmltodict.parse(file.read())["dataset"]["record"]
            data = [item for item in raw_content]
            return data
