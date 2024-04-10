
def validar_coluna(escolha, listagem):
    if escolha not in listagem:
        print("Houve um erro no seu pedido, encerrando o programa, tente novamente mais tarde.")
        return False
    else:
        return True

def validar_fileira(escolha,listagem_fileiras):
    if escolha not in listagem_fileiras:
        print("Houve um erro no seu pedido, encerrando o programa, tente novamente mais tarde.")
        return False
    else:
        return True

def validar_poltrona(escolha, listagem_poltronas):

    if escolha not in listagem_poltronas:
        print("Houve um erro no seu pedido, encerrando o programa, tente novamente mais tarde.")
        return False
    else:
        return True

def validar_numero(entrada):
    try:
        float(entrada)  # Tenta converter a entrada para um número float
        return True     # Se não houver erro, a entrada é um número
    except ValueError:
        print("Tipo de entrada Inválida.")
        return False
