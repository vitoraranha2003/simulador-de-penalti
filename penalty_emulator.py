import random
from time import sleep

#Tela inicial:

print("===========================")
print("   Simulador de Pênalti")
print("===========================")
sleep(3.0)
print("Escolha seu time:")
print("[1] Flamengo")
print("[2] Palmeiras")
print("[3] Corinthians")
print("[4] Vasco")
print("[5] Fluminense")
print("[6] São Paulo")
print("===========================")
sleep(5)
escolha_jogador=int(input("Digite o número do seu time:"))
print(".")
sleep(1.5)
print(".")
sleep(1.5)
print(".")
sleep(1.5)

#Escolhendo o time:

if escolha_jogador==1:
    print("Você escolheu o Flamengo")
    sleep(2)
    escolha_cpu=random.choice([2, 3, 4, 5, 6])
    if escolha_cpu==2:
        print("Seu adversário escolheu o Palmeiras")
    if escolha_cpu==3:
        print("Seu adversário escolheu o Corinthians")
    if escolha_cpu == 4:
        print("Seu adversário escolheu o Vasco")
    if escolha_cpu==5:
        print("Seu adversário escolheu o Fluminense")
    if escolha_cpu==6:
        print("Seu adversário escolheu o São Paulo")

if escolha_jogador==2:
    print("Você escolheu o Palmeiras")
    sleep(2)
    escolha_cpu = random.choice([1, 3, 4, 5, 6])
    if escolha_cpu == 1:
        print("Seu adversário escolheu o Flamengo")
    if escolha_cpu == 3:
        print("Seu adversário escolheu o Corinthians")
    if escolha_cpu == 4:
        print("Seu adversário escolheu o Vasco")
    if escolha_cpu == 5:
        print("Seu adversário escolheu o Fluminense")
    if escolha_cpu == 6:
        print("Seu adversário escolheu o São Paulo")

if escolha_jogador==3:
    print("Você escolheu o Corinthians")
    sleep(2)
    escolha_cpu = random.choice([1, 2, 4, 5, 6])
    if escolha_cpu == 1:
        print("Seu adversário escolheu o Flamengo")
    if escolha_cpu == 2:
        print("Seu adversário escolheu o Palmeiras")
    if escolha_cpu == 4:
        print("Seu adversário escolheu o Vasco")
    if escolha_cpu == 5:
        print("Seu adversário escolheu o Fluminense")
    if escolha_cpu == 6:
        print("Seu adversário escolheu o São Paulo")
if escolha_jogador==4:
    print("Você escolheu o Vasco")
    sleep(2)
    escolha_cpu = random.choice([1, 2, 3, 5, 6])
    if escolha_cpu == 1:
        print("Seu adversário escolheu o Flamengo")
    if escolha_cpu == 2:
        print("Seu adversário escolheu o Palmeiras")
    if escolha_cpu == 3:
        print("Seu adversário escolheu o Corinthians")
    if escolha_cpu == 5:
        print("Seu adversário escolheu o Fluminense")
    if escolha_cpu == 6:
        print("Seu adversário escolheu o São Paulo")
if escolha_jogador==5:
    print("Você escolheu o FLuminense")
    sleep(2)
    escolha_cpu = random.choice([1, 2, 3, 4, 6])
    if escolha_cpu == 1:
        print("Seu adversário escolheu o Flamengo")
    if escolha_cpu == 2:
        print("Seu adversário escolheu o Palmeiras")
    if escolha_cpu == 3:
        print("Seu adversário escolheu o Corinthians")
    if escolha_cpu == 4:
        print("Seu adversário escolheu o Vasco")
    if escolha_cpu == 6:
        print("Seu adversário escolheu o São Paulo")
if escolha_jogador==6:
    print("Você escolheu o São Paulo")
    sleep(2)
    escolha_cpu = random.choice([1, 2, 3, 4, 5])
    if escolha_cpu == 1:
        print("Seu adversário escolheu o Flamengo")
    if escolha_cpu == 2:
        print("Seu adversário escolheu o Palmeiras")
    if escolha_cpu == 3:
        print("Seu adversário escolheu o Corinthians")
    if escolha_cpu == 4:
        print("Seu adversário escolheu o Vasco")
    if escolha_cpu == 5:
        print("Seu adversário escolheu o Fluminense")

print("======================================")

#Escolhendo quem começa
sleep(1.5)
print("Vamos começar as penalidades!")
sleep(2)
print("Vamos ver quem começa!")
print("[1] Cara")
print("[2] Coroa")
cara_ou_coroa=int(input("Digite sua escolha:"))
escolha_cara_ou_coroa=random.choice([1,2])

#Você ganhou:

if escolha_cara_ou_coroa==cara_ou_coroa:
    print("Você ganhou! Você começa nas cobranças")
    num_cobranças_jogador = num_cobranças_cpu = 0
    jogador = []
    cpu = []

    while True:
        print("Sua vez!")
        sleep(1)
        print("Escolha onde você vai cobrar o pênalti:")
        print("[1] Esquerda")
        print("[2] Meio")
        print("[3] Direita")
        cobrança_jogador = int(input("Digite sua escolha:"))
        num_cobranças_jogador += 1
        cobrança_cpu = random.choice([1, 2, 3])
        sleep(1)
        print("O jogador vai pra cobrança...")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        if cobrança_jogador == cobrança_cpu:
            print("PEEEEEEEEEEEEEEEEEGA O GOLEIRO!!!")
            jogador.append("X")
            print(jogador)
            print(cpu)
            sleep(5)
        else:
            print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!!!")
            jogador.append("O")
            print(jogador)
            print(cpu)
            sleep(5)
        pontos_jogador = pontos_cpu = 0
        for c in range(0, len(jogador)):
            if "O" in jogador[c]:
                pontos_jogador += 1
        for c in range(0, len(cpu)):
            if "O" in cpu[c]:
                pontos_cpu += 1
        if num_cobranças_jogador > 5:
            if num_cobranças_cpu > 5:
                if pontos_jogador != pontos_cpu:
                    break
        cobranças_faltantes_jogador = 5-num_cobranças_jogador
        cobranças_faltantes_cpu = 5-num_cobranças_cpu
        if num_cobranças_jogador<=5:
            if num_cobranças_cpu<=5:
                if (cobranças_faltantes_jogador + pontos_jogador) < pontos_cpu:
                    break
                if (cobranças_faltantes_cpu + pontos_cpu) < pontos_jogador:
                    break
        print("É a vez do adversário!")
        print("Escolha onde você vai pular:")
        print("[1] Esquerda")
        print("[2] Meio")
        print("[3] Direita")
        cobrança_jogador = int(input("Digite sua escolha:"))
        num_cobranças_cpu += 1
        cobrança_cpu = random.choice([1, 2, 3])
        sleep(1)
        print("O jogador adversário vai pra cobrança...")
        sleep(2)
        print("O goleiro se prepara...")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        if cobrança_jogador == cobrança_cpu:
            print("PEEEEEEEEEEEEEEEEEGA O GOLEIRO!!!")
            cpu.append("X")
            print(jogador)
            print(cpu)
            sleep(5)
        else:
            print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!!!")
            cpu.append("O")
            print(jogador)
            print(cpu)
            sleep(5)
        pontos_jogador = pontos_cpu = 0
        for c in range(0, len(jogador)):
            if "O" in jogador[c]:
                pontos_jogador += 1
        for c in range(0, len(cpu)):
            if "O" in cpu[c]:
                pontos_cpu += 1
        if num_cobranças_jogador > 5:
            if num_cobranças_cpu > 5:
                if pontos_jogador != pontos_cpu:
                    break
        cobranças_faltantes_jogador = 5-num_cobranças_jogador
        cobranças_faltantes_cpu = 5-num_cobranças_cpu
        if num_cobranças_jogador<=5:
            if num_cobranças_cpu<=5:
                if (cobranças_faltantes_jogador + pontos_jogador) < pontos_cpu:
                    break
                if (cobranças_faltantes_cpu + pontos_cpu) < pontos_jogador:
                    break
    if pontos_jogador > pontos_cpu:
        print("Você ganhou!")
    else:
        print("Sinto muito, você perdeu!")







#Seu adversário ganhou:

if escolha_cara_ou_coroa!=cara_ou_coroa:
    print("Você perdeu! Seu adversário vai começar.")
    num_cobranças_jogador = num_cobranças_cpu = 0
    jogador = []
    cpu = []
    while True:
        print("É a vez do adversário!")
        print("Escolha onde você vai pular:")
        print("[1] Esquerda")
        print("[2] Meio")
        print("[3] Direita")
        cobrança_jogador = int(input("Digite sua escolha:"))
        num_cobranças_cpu += 1
        cobrança_cpu = random.choice([1, 2, 3])
        sleep(1)
        print("O jogador adversário vai pra cobrança...")
        sleep(2)
        print("O goleiro se prepara...")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        if cobrança_jogador == cobrança_cpu:
            print("PEEEEEEEEEEEEEEEEEGA O GOLEIRO!!!")
            cpu.append("X")
            print(jogador)
            print(cpu)
            sleep(5)
        else:
            print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!!!")
            cpu.append("O")
            print(jogador)
            print(cpu)
            sleep(5)
        pontos_jogador = pontos_cpu = 0
        for c in range(0, len(jogador)):
            if "O" in jogador[c]:
                pontos_jogador += 1
        for c in range(0, len(cpu)):
            if "O" in cpu[c]:
                pontos_cpu += 1
        if num_cobranças_jogador > 5:
            if num_cobranças_cpu > 5:
                if pontos_jogador != pontos_cpu:
                    break
        cobranças_faltantes_jogador = 5 - num_cobranças_jogador
        cobranças_faltantes_cpu = 5 - num_cobranças_cpu
        if num_cobranças_jogador <= 5:
            if num_cobranças_cpu <= 5:
                if (cobranças_faltantes_jogador + pontos_jogador) < pontos_cpu:
                    break
                if (cobranças_faltantes_cpu + pontos_cpu) < pontos_jogador:
                    break
        print("Sua vez!")
        sleep(1)
        print("Escolha onde você vai cobrar o pênalti:")
        print("[1] Esquerda")
        print("[2] Meio")
        print("[3] Direita")
        cobrança_jogador = int(input("Digite sua escolha:"))
        num_cobranças_jogador += 1
        cobrança_cpu = random.choice([1, 2, 3])
        sleep(1)
        print("O jogador vai pra cobrança...")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        print(".")
        sleep(2)
        if cobrança_jogador == cobrança_cpu:
            print("PEEEEEEEEEEEEEEEEEGA O GOLEIRO!!!")
            jogador.append("X")
            print(jogador)
            print(cpu)
            sleep(5)
        else:
            print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!!!")
            jogador.append("O")
            print(jogador)
            print(cpu)
            sleep(5)
        pontos_jogador = pontos_cpu = 0
        for c in range(0, len(jogador)):
            if "O" in jogador[c]:
                pontos_jogador += 1
        for c in range(0, len(cpu)):
            if "O" in cpu[c]:
                pontos_cpu += 1
        if num_cobranças_jogador > 5:
            if num_cobranças_cpu > 5:
                if pontos_jogador != pontos_cpu:
                    break
        cobranças_faltantes_jogador = 5 - num_cobranças_jogador
        cobranças_faltantes_cpu = 5 - num_cobranças_cpu
        if num_cobranças_jogador <= 5:
            if num_cobranças_cpu <= 5:
                if (cobranças_faltantes_jogador + pontos_jogador) < pontos_cpu:
                    break
                if (cobranças_faltantes_cpu + pontos_cpu) < pontos_jogador:
                    break
    if pontos_jogador > pontos_cpu:
        print("Você ganhou!")
        print("Parabéns! 🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
    else:
        print("Sinto muito, você perdeu!")