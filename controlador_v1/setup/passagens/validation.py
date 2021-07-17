def origem_destino_iguais(origem, destino,lista_de_erros):
    """verifica se origem e destino sao iguais"""

    if origem == destino:
        lista_de_erros['destino'] = 'A Origem e o Destino não podem ser iguais'

def campo_tem_numeros(valor_campo,nome_campo,lista_de_erros):
    """veridica se possui algum digito numérico"""

    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Nao inclua números neste campo'

def data_ida_maior_que_volta(data_ida,data_volta,lista_de_erros):
    """verifica se a data de ida é maior que a da volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = "A data da volta não pode ser menor que a ida"

def data_compra_menor_que_compra(data_ida, data_pesquisa, lista_de_erros):
    """verifica se a data de ida eh maior que hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = "A data de viagem não pode ser menor que a data de hoje"