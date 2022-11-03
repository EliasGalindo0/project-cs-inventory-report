from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[36m"
RESET = "\033[0m"

product_mock = [
    {
        "id": 1,
        "nome_do_produto": "Borracha",
        "nome_da_empresa": "Papelaria Solar",
        "data_de_fabricacao": "2021-07-04",
        "data_de_validade": "2029-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Ao abrigo de luz solar",
    }
]


def test_decorar_relatorio():
    colored = ColoredReport(SimpleReport).generate(product_mock)
    assert colored == (
        f"{GREEN}Data de fabricação mais antiga:{RESET}"
        + f" {BLUE}2021-07-04{RESET}\n"
        f"{GREEN}Data de validade mais próxima:{RESET}"
        + f" {BLUE}2029-02-09{RESET}\n"
        f"{GREEN}Empresa com mais produtos:{RESET} {RED}Papelaria Solar{RESET}"
    )
