from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
      1, 'jPhone', 'Orange', '01/02/2003', '01/02/2004', 'JKLMNO123',
      'Manter afastado do fogo'
    )

    assert product.id == 1
    assert product.nome_do_produto == "jPhone"
    assert product.nome_da_empresa == "Orange"
    assert product.data_de_fabricacao == "01/02/2003"
    assert product.data_de_validade == "01/02/2004"
    assert product.numero_de_serie == "JKLMNO123"
    assert product.instrucoes_de_armazenamento == "Manter afastado do fogo"
