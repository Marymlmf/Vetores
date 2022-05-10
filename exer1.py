vet = []
informado = False
soma2=0
while True:
    tipo=0
    print("1-Entre com um vetor de 10 inteiros")
    print("2-Mostrar o vetor.")
    print("3-Mostrar todos os valores pares do vetor")
    print("4-Mostrar todos os valores dos índices impares do vetor")
    print("5-Mostrar a soma de todos os valores pares do vetor")
    print("6-Informar um número e mostrar os valores (e seu respectivo índice) diferentes que este valor do primeiro ao quinto índice (4) e o valores iguais do sexto ao décimo índice.")
    print("7-Mostrar os valores ao mesmo tempo do quinto e o sexto índice, quarto e sétimo assim por diante até o fim e o início do vetor.")
    print("8-Verificação de compatibilidade")
    print("9-Sair: ")
    tipo= int(input("... : "))
    if tipo == 9:
        print('-=' * 20)
        print("|",' '*9,"Fim do programa!",' '*9,"|")
        print('-=' * 20)
        break
    elif tipo >=1 and tipo<=9:
        if tipo==1:
            for i in range(10):
                vet.append(int(input("Entre com o valor de para a posição %d:" % i)))
                informado=True
        elif tipo==2:
            if informado:
                print(vet)
                print('-=' * 20)
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
        elif tipo == 3:
            if informado:
                for i in range(10):
                    if vet[i]%2==0:
                        soma2+=vet[i]
                        print(vet[i],end="")
                        print('-=' * 20)
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
        elif tipo == 4:
            if informado:
                print(vet[1],",",vet[3],",",vet[5],",",vet[7],",",vet[9])
                print('-=' * 20)
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
        elif tipo == 5:
            if informado:
                print("A soma dos números pares é: ")
                print(soma2)
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
        elif tipo == 6:
            if informado:
                print("Desculpa professor não consegui pensar em uma lógica")
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
        elif tipo == 7:
            if informado:
                print(vet[4],"",vet[5])
                print(vet[3],"",vet[6])
                print(vet[2],"",vet[7])
                print(vet[1],"",vet[8])
                print(vet[0],"",vet[9])
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
        elif tipo==8:
            if informado:
                print("Desculpa professor não consegui pensar em uma lógica")
            else:
                print("Primeiramente entre com um vetor de 10 números inteiros.")
    else:
        print("Opção Inválida")