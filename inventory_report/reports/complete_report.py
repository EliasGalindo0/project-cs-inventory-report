from collections import Counter
from inventory_report.reports.simple_report import SimpleReport

# [
#   {
#     "id": 1,
#     "nome_do_produto": "MESA",
#     "nome_da_empresa": "Forces of Nature",
#     "data_de_fabricacao": "2022-05-04",
#     "data_de_validade": "2023-02-09",
#     "numero_de_serie": "FR48",
#     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
#   }
# ]


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        cls.simple_report = super().generate(products)
        cls.companies = [product["nome_da_empresa"] for product in products]
        companies_and_quantity_of_products = dict(Counter(cls.companies))
        product_stocked_by_company = ''
        for company in companies_and_quantity_of_products:
            product_stocked_by_company += (
                f"- {company}: {companies_and_quantity_of_products[company]}\n"
            )

        return (
            f"{cls.simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{product_stocked_by_company}"
        )
