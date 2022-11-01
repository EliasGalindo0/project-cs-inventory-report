from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
      1, 'jPhone', 'Orange', '01/02/2003', '01/02/2004', 'JKLMNO123',
      'Manter afastado do fogo'
    )

    assert str(product) == (
      f"O produto {product.nome_do_produto}"
      f" fabricado em {product.data_de_fabricacao}"
      f" por {product.nome_da_empresa} com validade"
      f" até {product.data_de_validade}"
      f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
