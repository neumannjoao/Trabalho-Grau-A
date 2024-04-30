import random
import os

############  FUNÇÕES ############

#rodar a roleta
def roleta():
    return random.randint(1,6)

#regra do dado
def rolar_dado (jogador):
    input("Pressione ENTER para jogar os dados...")
    dado = random.randint (1,6)
    print(f"Você tirou {dado}")

    if dado == 1:
        jogador["posicao"] += 1
    elif dado == 3:
        jogador["posicao"] -= 1
    elif dado == 6:
        print("Você perdeu uma rodada")

#regra da morte


#regra do desafio matemático
def desafio_matematico(jogador):
    print("Hora do desafio matemático!")
    input("Pressione ENTER para girar a roleta novamente...")
    num_roleta = roleta()
    print(f"Você tirou {num_roleta}")
    
    if num_roleta == 1:
        print("Mostrar na tela os números primos até 100")
        # Números primos até 100
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        print("Números primos até 100:", primos)
    
    elif num_roleta == 2:
        print("Fazer o somatório dos números de 1 até 10:", sum(range(1, 11)))
    
    elif num_roleta == 3:
        print("Imprimir a série de Fibonacci até o décimo elemento:")
        a, b = 0, 1
        for _ in range(10):
            print(a, end=" ")
            a, b = b, a + b
            print()
        
    elif num_roleta == 4:
        print("Calcular a área de um círculo com raio 2.5:", 3.14 * (2.5 ** 2))

    elif num_roleta == 5:
        print("Imprimir o fatorial de 5:", 5 * 4 * 3 * 2 * 1)

    elif num_roleta == 6:
        print("Imprimir os 8 primeiros números divisíveis por 2 e por 5:")
        divisiveis = [x for x in range(1, 100) if x % 2 == 0 and x % 5 == 0][:8]
        print(divisiveis)


#regra da formatura
def escolher_curso(jogador):
    while True:
        print("1 - Direito")
        print("2 - Medicina")
        print("3 - Jogos Digitais")
        print("4 - Segurança da Informação")
        print("5 - Análise e Desenvolvimento de Sistemas")
        print("6 - Economia")
        curso_escolhido = input("Digite a opção do curso desejado: ")

        if curso_escolhido == '1':
            print("Parabéns você se formou em Direito!")
            jogador ['formado'] = "Direito"
            break
    
        elif curso_escolhido == '2':
            print("Parabéns você se formou em Medicina!")
            jogador ['formado'] = "Medicina"
            break

        elif curso_escolhido == '3':
            print("Parabéns você se formou em Jogos Digitais!")
            jogador ['formado'] = "Jogos Digitais"
            break

        elif curso_escolhido == '4':
            print("Parabéns você se formou em Segurança da Informação!")
            jogador ['formado'] = "Segurança da informação"
            break

        elif curso_escolhido == '5':
            print("Parabéns você se formou em Análise e Desenvolvimento de Sistemas!")
            jogador ['formado'] = "Análise e Desenvolvimento de Sistemas"
            break
    
        elif curso_escolhido == '6':
            print("Parabéns você se formou em Economia!")
            jogador ['formado'] = "Economia"
            break
    
        else:
            print("Opção inválida, digite uma opção válida.")


#regra dos filhos
def filhos (jogador):
    roleta_filhos = roleta

    if roleta_filhos == 5:
        print("Parabéns!\nVocê teve gêmeos.")
        jogador['filhos'] += 2
    else:
        print("Parabéns!\nSeu bebê Nasceu.")
        jogador['filhos'] +=1

#regra do casamento
def casou(jogador):
    print("Parabéns!\nVocê se Casou.")

    if jogador ['casado'] == "Não" and jogador ['divorciado'] == "Não" and jogador ['divorciado'] == "Sim":
        jogador['casado'] = "Sim"
    else:
        jogador['casado'] = 'Não'
    
#regra ficou famoso
def ficou_famoso(jogador):
    print("Parabéns!\nVocê ficou famoso.")
    jogador ['famoso'] = "Sim"

#regra divorcio
def divorciou(jogador):
    print("O casamento não deu certo\nVocê se divorciou.")
    jogador ['casado'] = "Não"
    jogador ['divorciado'] = "Sim"
    imprimir_status_jogador(jogador)

#regra loteria
def loteria (jogador):
    print('Uau!\nSeu bilhete foi premiado!')
    input('Pressione ENTER para girar a roleta e descobrir o valor do seu prêmio...')
    roleta_loteria = random.randint(1,6)


    if roleta_loteria == 1:
        print("Você ganhou R$2,50.")
        jogador['dinheiro'] = 2.50

    elif roleta_loteria == 2:
        print("Você ganhou R$5.000")
        jogador['dinheiro'] = 5000
    
    elif roleta_loteria == 3:
        print("Você ganhou R$50.000")
        jogador['dinheiro'] = 50000

    elif roleta_loteria == 4:
        print("Você ganhou R$500.000")
        jogador['dinheiro'] = 500000

    elif roleta_loteria == 5:
        print("Você ganhou R$5.000.000")
        jogador['dinheiro'] = 5000000

    elif roleta_loteria == 6:
        print("Você ganhou R$100.000.000")
        jogador['dinheiro'] = 100000000

#regra da maquina do tempo
def maquina_tempo(jogador):
    print("Você encontrou uma máquina do tempo e decidiu usá-la.")
    jogador['posicao'] = 0
    jogador['filhos'] = 0
    jogador['dinheiro'] = 0
    jogador['casado'] = "Não"
    jogador['divorciado'] = "Não"
    jogador['famoso'] = "Não"
    jogador['formado'] = "Não"
    jogador['vivo'] = "Sim"
    print("Todos os seus dados foram resetados.")

#função para imprimir status do jogador
def imprimir_status_jogador(jogador):
    print(f"\nStatus do jogador {jogador['nome']}:")
    print(f"Posição: {jogador['posicao']}")
    print(f"Filhos: {jogador['filhos']}")
    print(f"Dinheiro: {jogador['dinheiro']}")
    print(f"Casado: {jogador['casado']}")
    print(f"Divorciado: {jogador['divorciado']}")
    print(f"Famoso: {jogador['famoso']}")
    print(f"Formado: {jogador['formado']}")
    print(f"Vivo: {jogador['vivo']}")


#######################################################################################  PROGRAMA PRINCIPAL #######################################################################################
def main():
    jogador1 = {
        "nome": input("Nome do jogador 1: "),
        "posicao": 0,
        "filhos" : 0,
        "dinheiro" : 0,
        "casado": "Não",
        "divorciado": "Não" ,
        "famoso": "Não",
        "formado" : "Não",
        "vivo": "Sim"
    }

    jogador2 = {
        "nome": input("Nome do jogador 2: "),
        "posicao": 0,
        "filhos" : 0,
        "dinheiro" : 0,
        "casado": "Não",
        "divorciado": "Não",
        "famoso": "Não",
        "formado" : "Não",
        "vivo": "Sim"
    }
    
    jogadores = [jogador1, jogador2]
    vencedor = None

    while vencedor is None:
        for jogador in jogadores:
            print(f"\nVez de {jogador['nome']}:")
            input("Pressione ENTER para girar a roleta...")
            num_roleta = roleta()
            print(f"Você tirou {num_roleta}")

            jogador ['posicao'] += num_roleta

            #aplicar regra do dado
            if jogador['posicao'] in [1, 3, 10, 17]:
                rolar_dado(jogador)
                imprimir_status_jogador(jogador)

            #aplicar regra da morte
            elif  jogador['posicao'] in [2, 8, 18]:
                print("Você morreu e perdeu o jogo!")
                jogador['vivo'] = "Não"
                vencedor = next (x for x in jogadores if x != jogador)
                imprimir_status_jogador(jogador)
                break
        

            #aplicar regra do desafio matemático
            elif  jogador['posicao'] in [4, 11, 19]:
                desafio_matematico(jogador)
                imprimir_status_jogador(jogador)

            #aplicar regra da formatura:
            elif  jogador['posicao'] == 5:
                print("Você vai se formar!!")
                escolher_curso(jogador)
                imprimir_status_jogador(jogador)

            #aplicar regra dos filhos
            elif jogador['posicao'] in [6, 9, 13]:
                filhos(jogador)
                imprimir_status_jogador(jogador)
            
            #aplicar regra do casamento
            elif  jogador['posicao'] in [7,16]:
                casou(jogador)
                imprimir_status_jogador(jogador)

            #aplicar regra ficou famoso
            elif  jogador['posicao'] == 15:
                ficou_famoso(jogador)
            
            #aplicar regra divorcio
            elif  jogador['posicao'] == 12:
                divorciou(jogador)

            #aplicar regra loteria
            elif  jogador['posicao'] == 14:
                loteria(jogador)
                imprimir_status_jogador(jogador)

            #aplicar regra da maquina do tempo
            elif jogador['posicao'] == 20:
                maquina_tempo(jogador)
                imprimir_status_jogador(jogador)

main()