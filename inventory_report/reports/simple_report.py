from datetime import datetime
from statistics import mode

#  [
#    {
#      "id": 1,
#      "nome_do_produto": "CADEIRA",
#      "nome_da_empresa": "Forces of Nature",
#      "data_de_fabricacao": "2022-04-04",
#      "data_de_validade": "2023-02-09",
#      "numero_de_serie": "FR48",
#      "instrucoes_de_armazenamento": "Conservar em local fresco"
#    }
#  ]


class SimpleReport:
    @classmethod
    def generate(cls, products):
        cls.data_de_fabricacao = min([product["data_de_fabricacao"]
                                      for product in products], default=0)
        cls.data_de_validade = min([product["data_de_validade"]
                                    for product in products
                                    if product["data_de_validade"] >
                                    datetime.today().isoformat()],
                                   default=0)
        cls.nome_da_empresa = mode([product["nome_da_empresa"]
                                    for product in products])

        return (
              f"Data de fabricação mais antiga: {cls.data_de_fabricacao}\n"
              f"Data de validade mais próxima: {cls.data_de_validade}\n"
              f"Empresa com mais produtos: {cls.nome_da_empresa}"
        )
