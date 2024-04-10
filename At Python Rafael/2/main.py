import os
saldo = 0

def inserir_saldo():
            
        try:
            
            novo_saldo = float(input("Quanto é o seu saldo atual:  "))
            
            global saldo
            saldo_antigo = saldo
            saldo += novo_saldo

            print(f"Seu saldo antigo R${saldo_antigo} , novo saldo R${saldo}")

        except ValueError:

            print("Você deve inserir um número, retornando ao menu principal.")
           

def anotar_receitas():
    
    aumento_receita = float(input("Valor ganho:  "))
    fonte_financeira = input("Fonte financeira?:  ")

    global saldo
    saldo_antigo = saldo
    saldo += aumento_receita 

    with open("relatorio_receitas.txt", 'a') as f:
        f.writelines(f"\nFonte da nova receita: {fonte_financeira};Valor:{aumento_receita};Saldo antes do aumento: {saldo_antigo};Saldo após aumento: {saldo}")
    
    voltar = input("Voltar ao menu ?  [1] Sim  [2] Anotar mais alguma receita:  ")
    
    if voltar == '1': menu()
    if voltar == '2': anotar_receitas()


def anotar_despesas():
    """Função que permite o usuário anotar suas despesas com categorias pré-definidas."""
    
    try: # try catch para fazer com que o programa não crashe caso seja escrito algo alem de um float.
        gasto = float(input("Valor do gasto:  "))     
    except ValueError:
        print("Ocorreu um erro na sua instrução, retornando ao menu principal......")            
        return
        
    print("Categorias [1]Lazer  [2]Transporte  [3] Alimentaco")
    resposta = input("Qual:  ")
    descricao = input("Escreva a descrição:  ").split(";")
    global saldo
    saldo_antigo = saldo
    saldo -= gasto

    match resposta:
    
        case '1':
            with open("relatorio_lazer.txt", 'a') as f:
                f.writelines(f"\nCategoria: Lazer;Descricao {descricao} ;Valor: -{gasto}; Saldo antes: {saldo_antigo} ;Saldo Atual: {saldo}")

        case '2':
              
         with open("relatorio_transporte.txt", 'a') as f:
            f.writelines(f"Categoria: Transporte;Descricao {descricao} ;Valor: -{gasto} ;Saldo antes: {saldo_antigo}; Saldo Atual: {saldo}\n")

        case '3':
         with open("relatorio_alimentacao.txt", 'a') as f:
            f.writelines(f"Categoria: Alimentacao;Descricao {descricao} ;Valor: -{gasto};Saldo antes:{saldo_antigo}; Saldo Atual: {saldo}\n")
    
        case _:
            print("Categoria não reconhecida.... tente novamente.")
            
    return saldo


def listar_receitas():
    """Função que acessa o arquivo de texto contendo a quantidade de lucro que o usuário teve."""    
    
    with open("relatorio_receitas.txt", 'r') as ler:
        
        print(ler.readlines())
        

def listar_despesas():
    """Função que permite usuario escolher qual categoria de gasto ele deseja listar."""

    resposta = input("Qual categoria voce quer listar?  [1] Lazer [2] Transporte , [3] Alimentacao ")
    
    match(resposta):
        
        case '1':
            lazer()
        case '2':
            transporte()
        case '3':
            alimentacao()
        case _:
            print("Comando não reconhecido, por favor tente novamente...")


def listar_todas_despesas():
    """Função que lista de forma ordenada todos as despesas, checando primeiramente os arquivos de texto nais quais elas são anotadas existem ou não."""
    todas_despesas = []
    
    try:
        
        if os.path.isfile("relatorio_lazer.txt") == True:

            print("Exibindo do maior ao menor...")
            # Abrindo e lendo o arquivo de cada categoria
            with open("relatorio_lazer.txt", 'r') as f_lazer:
                todas_despesas.extend(f_lazer.readlines())

        if os.path.isfile("relatorio_transporte.txt") == True:

                print("Exibindo do maior ao menor...")
                with open("relatorio_transporte.txt", 'r') as f_transporte:
                    todas_despesas.extend(f_transporte.readlines())

        if os.path.isfile("relatorio_alimentacao.txt") == True:

                print("Exibindo do maior ao menor...")
                with open("relatorio_alimentacao.txt", 'r') as f_alimentacao:
                    todas_despesas.extend(f_alimentacao.readlines())

        else: # else caso não seja encontrado nada
                print("Não foi encontrado nenhum arquivo.")

        # Ordenando as despesas por categoria e valor
        todas_despesas.sort(key=lambda x: (
            x.split(';')[0] if len(x.split(';')) > 1 else '',
            float(x.split(';')[2].split(': ')[1]) if len(x.split(';')) > 2 else 0
        ))

        # Exibindo as despesas ordenadas
        for despesa in todas_despesas:
            print(despesa.strip())
 
    except FileNotFoundError:  # try catch para tratar em caso de erro do arquivo não existir.
        print("Não foi achado nenhum arquivo correspondente as categorias pré definidas, retornando ao menu")
        return


def lazer():
    """Função que lê o arquivo de texto referente aos gastos relacionados ao lazer"""    

    if os.path.isfile("relatorio_lazer.txt") == False:
        print("Não existe tal arquivo.")
        return

    else:
        with open("relatorio_lazer.txt", 'r') as f:

            print(f.readlines())


def transporte():
    """Função que lê o arquivo de texto referente aos gastos relacionados ao transporte"""

    if os.path.isfile("relatorio_transporte.txt") == False:
        print("Não existe tal arquivo.")
        return

    else:
        with open("relatorio_transporte.txt", 'r') as f:
            print(f.readlines())


def alimentacao():
    """Função que lê o arquivo de texto referente aos gastos relacionados a alimentacao"""
    if os.path.isfile("relatorio_alimentacao.txt") == False:
        print("Não existe tal arquivo.")
        return

    else:
        with open("relatorio_alimentacao.txt", 'r') as f:

            print(f.readlines())

        
def menu():
    """Função que simula uma interface gráfica para o usuário interagir com o programa."""

    while True:
        print("\n[1] Adicionar saldo \n[2] Anotar alguma receita \n[3] Listar todas as receitas  \n[4] Anotar despesa \n[5] Listar despesas \n[6] Listar Todas despesas \n[7] Sair")
        print('-' * 30)
        resposta = input("Escolha:  ")
    
        match resposta:
            case '1':
                inserir_saldo()
            case '2':
                anotar_receitas()
            case '3':
                listar_receitas()
            case '4':
                anotar_despesas()
            case '5':
                listar_despesas()
            case '6':
                listar_todas_despesas()
            case '7':
                break
            case _:
                print("Escolha uma das opções acima, por favor.")
                        
inserir_saldo()
menu()
