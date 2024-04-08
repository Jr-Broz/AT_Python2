quantidade_acertos = 0
quantidade_erros = 0

"""
Cada função aqui possui perguntas que serão chamadas no dicionário no arquivo jogo.py 

"""


def pergunta_um():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Python é lento ?")
    
    print("[1] Em comparação com as demais é, afinal é interpretada e compilada.")
    print("[2] Não, é mais rápida do que c++ e javascript.")
    print("[3] Depende do computador de quem usa.")
    print("[4] Não sei.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '1':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
    
        
def pergunta_dois():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Quem criou Python?")
    
    print("[1] Steve Jobs")
    print("[2] Alan Turing")
    print("[3] Guido van Rossum")
    print("[4] Linus Torvalds")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        
    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
    
    
 
def pergunta_tres():
    

    print("Marque V para verdadeiro e F para falso")
    print("-" * 20)
    print("() Python é uma linguagem de alto nível.")
    print("() Python NÃO é uma linguagem orientada a objetos.")
    print("() Python é utilizada para criação de jogos.")
    print("() Python não é utilizada no desenvolvimento de IA.")
    
        
    print("[1] V-V-V-V")
    print("[2] V-F-V-F")
    print("[3] F-V-V-F")
    print("[4] Todas as alternativas são falsas.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '2':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
    
   
def pergunta_quatro():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual comando para tirar espaços de uma string?")
    
    print("[1] print()")
    print("[2] split()")
    print("[3] strip()")
    print("[4] console.log()")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")


def pergunta_cinco():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Python usa qual paradigma de programação? ")
    
    print("[1] Orientação a objetos")
    print("[2] Estrutural")
    print("[3] Procedural")
    print("[4] Python é multiparadigma")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '4':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
            
def pergunta_seis():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("O que é orientação a objeto ?")
    
    print("[1] Um paradigma de programação")
    print("[2] é uma biblioteca")
    print("[3] uma função.")
    print("[4] Uma comida.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '1':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
            
def pergunta_sete():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual desses é um protocolo?")
    
    print("[1] binary search")
    print("[2] sort()")
    print("[3] https")
    print("[4] Big O")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
               
def pergunta_oito():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual dessas é utilizada MAJORITARIAMENTE no Front-End ?")
    
    print("[1] Django")
    print("[2] ASP NET MVC")
    print("[3] Java Spring Boot")
    print("[4] Javascript")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '4':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
        
def pergunta_nove():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual dessas são Orientadas a Objetos")
    
    print("[1] Java, C# & Python")
    print("[2] Https, LinkedLists & Ipv4")
    print("[3] Javascript, IPV6 & Ethical hacking.")
    print("[4] Machine Learning")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '1':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
        
        
def pergunta_dez():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual estrutura de dados não permite duplicatas ?")
    
    print("[1] Arrays")
    print("[2] Strings")
    print("[3] Sets")
    print("[4] Float")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
        
        
def pergunta_onze():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Como se mede a eficiência de um algoritmo?")
    
    print("[1] Contando quanto tempo um computador demora do inicio ao fim dele.")
    print("[2] Todo algoritmo tem a mesma eficiência.")
    print("[3] Não depende do hardware de quem utiliza.")
    print("[4] Através da Big O")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '4':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
        
        
def pergunta_doze():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual biblioteca que é muito utilizada para aleatorizar dados?")
    
    print("[1] Math.")
    print("[2] sys.")
    print("[3] Random.")
    print("[4] Open Cv.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
        
        
def pergunta_treze():
    
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Qual o nome do professor de python")
    
    print("[1] Felpo.")
    print("[2] Pablo Marçal.")
    print("[3] Dácio.")
    print("[4] Samuel.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
            
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
                
        
def pergunta_quatorze():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("Em teoria o que é programação ?")
    
    print("[1] Dar Instrução ao computador.")
    print("[2] Uma das áreas do direito digital.")
    print("[3] brincar com o computador")
    print("[4] Computador realizar suas função diárias, sem a necessidade de um terceiro.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '1':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        

    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")
        
        
def pergunta_quinze():
    
    print("Qual das resposta abaixo é resposta que mais se enquadra?")
    print("-" * 20)
    print("A sede do Infnet Fica ?")
    
    print("[1] No ceará, em boa viagem.")
    print("[2] Rio de Janeiro, Niterói")
    print("[3] Rio de Janeiro, RJ.")
    print("[4] Minas Gerais.")
    print("-" * 30)
    resposta = input("Sua resposta: ")
        
    print("----------------------")
    
    if resposta == '3':
        
        global quantidade_acertos
        quantidade_acertos +=1
        print("Você acertou, parabéns. Vamos para a próxima pergunta.")
        
    else:
        global quantidade_erros
        quantidade_erros += 1
        print("Que pena! você errou vamos para a próxima.")     