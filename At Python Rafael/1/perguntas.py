import random
def perguntas():
    
    quantidade_acertos = 0
    quantidade_erros = 0

    def pergunta_um():

        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            print(quantidade_acertos)            
    
            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
        
            
    def pergunta_dois():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            
            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
            
            
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
        
        
    
    def pergunta_tres():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
        
    
    def pergunta_quatro():
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")


    def pergunta_cinco():
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
                
    def pergunta_seis():
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
        
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
                
    def pergunta_sete():
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
        
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
                
    def pergunta_oito():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
            
    def pergunta_nove():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
            
            
    def pergunta_dez():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
            
            
    def pergunta_onze():
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
        
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
            
            
    def pergunta_doze():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
        
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
            
            
    def pergunta_treze():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

        else:
            
            quantidade_erros += 1
            print("Que pena! você errou vamos para a próxima.")
                    
            
    def pergunta_quatorze():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            

            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            

            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
            
    def pergunta_quinze():
        
        nonlocal quantidade_acertos 
        nonlocal quantidade_erros
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
            
            
            quantidade_acertos +=1
            print("Você acertou, parabéns. Vamos para a próxima pergunta.")
            
            if quantidade_acertos >= 5:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
        elif quantidade_erros >= 5:
                        
            print("Você zerou o jogo.")
            return

        else:
            quantidade_erros +=1
            print("Que pena, voce errou! indo para a próxima pergunta...")
            
    
    pergunta = {
        1: pergunta_um, 
        2: pergunta_dois,
        3: pergunta_tres,
        4: pergunta_quatro,
        5: pergunta_cinco,
        6: pergunta_seis,
        7: pergunta_sete,
        8: pergunta_oito,
        9: pergunta_nove,
        10: pergunta_dez,
        11: pergunta_onze,
        12: pergunta_doze,
        13: pergunta_treze,
        14: pergunta_quatorze,
        15: pergunta_quinze
    }

    while quantidade_acertos >= 5:

        escolha_aleatoria = random.randint(1, 15)
        pergunta_escolhida = pergunta[escolha_aleatoria]()
        print(pergunta_escolhida)

    
    # 0 a 14 indices
    # listagem_perguntas = [pergunta_um(), pergunta_dois(), pergunta_tres(), pergunta_quatro(), pergunta_cinco(), pergunta_seis(), pergunta_sete(), pergunta_oito(), pergunta_nove(), pergunta_dez(), pergunta_onze(), pergunta_doze(), pergunta_treze(), pergunta_quatorze(), pergunta_quinze()]
            
perguntas()
