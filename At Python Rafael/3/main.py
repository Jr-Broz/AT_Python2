import random
from validacoes import *
def filmes():
    """Função que lista de forma aleatória os filmes em cartazes.    
    Começa como uma lista, entretanto, o método random.choices() não inibe a possibilidade de duplicatas, por isso,
    existe uma conversão para a estrutura de dados SET, que não aceita duplicatas e a remove caso haja alguma.
    Após isso é retornada para uma lista.
    """

    filmes = ["A felicidade nao se compra", "Batman cavaleiro das trevas", "Garota Interrompida", "Jogo da Imitação", "Missão impossível", "Os Incriveis", "Lilo e Stitch", "Dr Estranho", "MIB homens de preto", "2012", "Velozes e Furiosos"]
    filmes_escolhidos =  random.choices(filmes, None, k=3)

    # Transformei em set pra que caso haja duplicatas, ele naturalmente irá remove-las.
    filmes_pre_aprovados = set(filmes_escolhidos) 
    filmes_aprovados = list(filmes_pre_aprovados) #Coloquei novamente em listas caso seja necessário manipula-lás depois

    print(f"Filmes em Cartaz:  {filmes_aprovados}")


def menu():
    """Função que simula uma pequena interface gráfica para o usuário."""    
    print("-" * 20)    
    
    escolha = input("[1] Para iniciar a compra dos ingressos.   ")
    
    match(escolha):
    
        case '1':
            comprar_ingressos()


# Funçao para validar se uma variavel nao possui entrada de numeros
def validar_palavra(palavra):
    if palavra.isalpha():
        return True
    else:
        print("Insira um valor válido, terminando programa.")
        return False


def comprar_ingressos():
    """Função que pega os dados do cliente, nome, quantidade de ingressos, escolha do filme, fileira e qual o identificador da poltrona e os guarda num arquivo.txt"""
    
    filmes()
    print('-' * 30)
    
    escolha = input("Qual filme você quer escolher ?   ")
    colunas_possiveis = ['a','b','c','d','e','f','g','h','i','j','k','l''m','n']
    numeros_poltronas_possiveis = ['1','2','3','4','5','6']
    fileiras_disponiveis = ['A','B','C','D','E','F']

    try:
        quantidade = int(input("Quantos ingressos você deseja comprar?  "))        

    except ValueError:
        print("Erro de Valor, insira um numero na proxima vez")
        return

        
    print("-----------------------")
    print("Escolha seu assento abaixo:  sendo x lugares ocupados e _ lugares disponíveis")    
            
    print("==================================")
    print("  a b c d e f g h i j k l m n") #Coluna
    print("A|xx_xxxxx_x_x_xx_xxxxxx__x_x|1")    
    print("B|___xxx_x_x_xx__x__x__x_xxx_|2")    
    print("C|xx_xx_x_x_x*x_xxxxxx__x_xxx|3")
    print("D|x__xx_xx_x_x_xxxxxx__x_x_xx|4")
    print("E|xx xxxxx_x_x_x*x_xx_xxx__x_|5")
    print("F|____________x______________|6")

    try:          
        fileira = input("Qual fileira você deseja escolher:  ").upper()
    
    except ValueError:
        print("Escreva um valor válido, terminando programa.")
            
    if fileira == "":
        print("Escreva um valor valido, terminando programa.")
        return
    
    if validar_palavra(fileira):
            
        if validar_fileira(fileira, fileiras_disponiveis): 
            
            numero_poltrona = input("Cada poltrona possui um numero identificador, a direita qual o seu ?   ")
                
            if validar_poltrona(numero_poltrona, numeros_poltronas_possiveis): # Caso validação de entrada do usuario seja correta
        
                coluna =  input("Escolha uma das colunas, [a,b,c,d,e,f,g,h,i,j,k,l,m ou n]  ").lower()
                print("-" * 30)
                    
                if validar_palavra(coluna): # caso nao haja entrada de numeros em coluna.
                        
                    if validar_coluna(coluna, colunas_possiveis):

                        
                        nome = input("Qual o seu nome?   ")
                                    
                        if validar_palavra(nome):
                            print("-" * 30)
                            print(f"\n Nome do cliente: {nome} | \n Filme: {escolha} | \nQuantidade de ingressos: {quantidade} | \nFileira: {fileira} | na Coluna: {coluna} | no Número {numero_poltrona}")
                            print("-" * 30)
                            print("Obrigado, bom filme.")


                        with open ("ingresso_cliente.txt", 'w') as arquivo:
                                    
                            arquivo.write(f"\nNome do cliente: {nome}")
                            arquivo.write(f"\nFilme: {escolha}")
                            arquivo.write(f"\nQuantidade de ingressos: {quantidade}")
                            arquivo.write(f"\n Fileira: {fileira} na coluna: {coluna} no número {numero_poltrona}")
                    


menu()#Função que faz a união entre comprar_ingressos() e filmes()