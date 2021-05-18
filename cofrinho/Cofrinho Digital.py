from os import system , name
def limpaTela():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def deposito(qt100=0,qt50=0, qt20=0, qt10=0, qt5=0, qt2=0, qt1=0):
    valorDepositado = int(input("Coloque seu dinheiro: R$ "))

    if valorDepositado <0:
        return qt100,qt50, qt20, qt10, qt5, qt2, qt1

    if valorDepositado != 100 and valorDepositado != 50 and valorDepositado != 20 and valorDepositado != 10 and valorDepositado != 5 and valorDepositado != 2 and valorDepositado != 1:
        print(f"Nota de R${valorDepositado:.2f} não reconhecida.")
        return deposito(qt100,qt50, qt20, qt10, qt5, qt2, qt1)

    if valorDepositado > 0:
        if valorDepositado == 100:
            qt100 += 1
        elif valorDepositado == 50:
            qt50 +=1
        elif valorDepositado == 20:
            qt20 += 1
        elif valorDepositado == 10:
            qt10 += 1
        elif valorDepositado == 5:
            qt5 +=1
        elif valorDepositado == 2:
            qt2 +=1
        elif valorDepositado == 1:
            qt1 +=1

        return deposito(qt100,qt50, qt20, qt10, qt5, qt2, qt1)

def verificar(valoSacar, qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1,N=0):
    if valoSacar < 0:
        return False
    if valoSacar==0:
        return valoSacar, qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1
    if N == 100:
        return False
    elif valoSacar-100 >=0 and qtNota100 > 0:
        qtNota100-=1
        valoSacar-=100
    elif valoSacar-50 >=0 and qtNota50 > 0:
        qtNota50-=1
        valoSacar-=50
    elif valoSacar-20 >=0 and qtNota20 > 0:
        qtNota20-=1
        valoSacar-=20
    elif valoSacar-10 >=0 and qtNota10 > 0:
        qtNota10-=1
        valoSacar-=10
    elif valoSacar-5 >=0 and qtNota5 > 0:
        qtNota5-=1
        valoSacar-=5
    elif valoSacar-2 >=0 and qtNota2 > 0:
        qtNota2-=1
        valoSacar-=2
    elif valoSacar-1 >=0 and qtNota1 > 0:
        qtNota1-=1
        valoSacar-=1
    

    return verificar(valoSacar,qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1,N+1)

def imprime(entrada,n100,n50,n20,n10,n5,n2,n1):
    if entrada == 0:
        return entrada, n100,n50,n20,n10,n5,n2,n1
    elif entrada-100 >=0 and n100 > 0:
        n100-=1
        entrada-=100
        print("R$100,00")
    elif entrada-50 >=0 and n50 > 0:
        n50-=1
        entrada-=50
        print("R$50,00")
    elif entrada-20 >=0 and n20 > 0:
        n20-=1
        entrada-=20
        print("R$20,00")
    elif entrada-10 >=0 and n10 > 0:
        n10-=1
        entrada-=10
        print("R$10,00")
    elif entrada-5 >=0 and n5 > 0:
        n5-=1
        entrada-=5
        print("R$5,00")
    elif entrada-2 >=0 and n2 > 0:
        n2-=1
        entrada-=2
        print("R$2,00")
    elif entrada-1 >=0 and n1 > 0:
        n1-=1
        entrada-=1
        print("R$1,00")
    return imprime(entrada, n100,n50,n20,n10,n5,n2,n1)

def sacar(saldo,qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1):
    valoSacar = int(input("Qual valor será sacado R$"))
    n100 = qtNota100
    n50 = qtNota50
    n20 = qtNota20
    n10 = qtNota10
    n5 = qtNota5
    n2 = qtNota2
    n1 = qtNota1
    entrada = valoSacar

    if valoSacar < 0:
        return saldo,qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1

    if valoSacar > saldo:
        notas = (qtNota100 * 100) + (qtNota50 * 50) + (qtNota20 * 20) + (qtNota10 * 10) + (qtNota5 * 5) + (qtNota2 * 2) + (qtNota1 * 1)
        print(f"Saldo insuficiente. Temos apenas R${notas:.2f} em caixa.")
        ordem = input("Deseja sacar esse valor (S/N)? ")

        if ordem == "s":
            valoSacar = (valoSacar - valoSacar) + notas
            ordem, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1 = verificar(valoSacar, qtNota100,qtNota50, qtNota20,qtNota10, qtNota5,qtNota2, qtNota1)

            entrada = (entrada - entrada) + notas
            imprime(entrada, n100, n50, n20, n10, n5, n2, n1)
            print(f"Valor sacado: R${notas:.2f}")
            saldo-=valoSacar

            _ = input("-->Enter para continuar...")
            return caixa(saldo,qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

        else:
            return sacar(saldo,qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

    if verificar(valoSacar, qtNota100,qtNota50, qtNota20,qtNota10, qtNota5,qtNota2, qtNota1) == False:
        print("Não a notas para realizar essa operação")
        _=input("Enter para continuar...")
        return caixa(saldo, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

    if saldo >= valoSacar:

        saldo-=valoSacar
        valoSacar, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1 = verificar(valoSacar, qtNota100,qtNota50, qtNota20,qtNota10, qtNota5,qtNota2, qtNota1)

        print("---Pegue seu dinheiro---")
        imprime(entrada, n100, n50, n20, n10, n5, n2, n1)

        _=input("-->Enter para continuar...")
        return caixa(saldo, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)



def caixa(saldo,qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1):
    limpaTela()
    print(">","-"*15,"<")
    print("|","1 - Depositar"," "*1,"|")
    print("|","2 - Saque"," "*5,"|")
    print("|","3 - Saldo"," "*5,"|")
    print("|","4 - Relatorio"," "*1,"|")
    print("|","5 - Finalizar"," "*1,"|")
    print(">","-"*15,"<")
    opcao = int(input("Qual vai ser sua operação: "))

    if opcao == 1:
        print("-- Digite um valor negativo para parar --")
        qt100,qt50,qt20,qt10,qt5,qt2,qt1 = deposito()
        soma = qt100 * 100 + qt50 * 50 + qt20 * 20 + qt10 * 10 + qt5 * 5 + qt2 * 2 + qt1 * 1
        print(f"Valor depositado R$ {soma:.2f}")
        _ = input("-->Enter para continuar...")
        caixa(saldo+soma, qtNota100 + qt100, qtNota50+ qt50, qtNota20+ qt20, qtNota10+ qt10, qtNota5+ qt5, qtNota2+ qt2, qtNota1+ qt1)

    elif opcao == 2:

        if saldo > 0:
            print("> Notas disponiveis no caixa <")
            if qtNota100 > 0:
                print(f"{qtNota100} x R$100,00")
            if qtNota50 > 0:
                print(f"{qtNota50} x R$50,00")
            if qtNota20 > 0:
                print(f"{qtNota20} x R$20,00")
            if qtNota10 > 0:
                print(f"{qtNota10} x R$10,00")
            if qtNota5 > 0:
                print(f"{qtNota5} x R$5,00")
            if qtNota2 > 0:
                print(f"{qtNota2} x R$2,00")
            if qtNota1 > 0:
                print(f"{qtNota1} x R$1,00")
            print(">", "-" * 25, "<")

            print("-- Digite um valor negativo para parar --")
            saldo,qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1 = sacar(saldo,qtNota100,qtNota50,qtNota20,qtNota10,qtNota5,qtNota2,qtNota1)

            caixa(saldo, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

        else:
            print("Saldo insuficiente")
            _ = input("-->Enter para continuar...")
            caixa(saldo,qtNota100,qtNota50,qtNota20, qtNota10, qtNota5,qtNota2, qtNota1)

    elif opcao == 3:

        print(f"Seu saldo atual R${saldo:.2f}")
        _ = input("-->Enter para continuar...")
        caixa(saldo, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

    elif opcao == 4:
        print("-"*5,"Relatorio","-"*5)
        print(f"Notas de R$100,00: {qtNota100}")
        print(f"Notas de R$50,00 : {qtNota50}")
        print(f"Notas de R$20,00 : {qtNota20}")
        print(f"Notas de R$10,00 : {qtNota10}")
        print(f"Notas de R$5,00  : {qtNota5}")
        print(f"Notas de R$2,00  : {qtNota2}")
        print(f"Notas de R$1,00  : {qtNota1}")
        print(">","-"*17,"<")
        _=input("-->Enter para continuar...")
        caixa(saldo, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

    elif opcao == 5:
        saida = input(f"deseja sacar os R${saldo:.2f} antes de fechar (S/N)? ")
        if saida == "s" or "S":
            n100 = qtNota100
            n50 = qtNota50
            n20 = qtNota20
            n10 = qtNota10
            n5 = qtNota5
            n2 = qtNota2
            n1 = qtNota1
            entrada = saldo
            imprime(entrada, n100, n50, n20, n10, n5, n2, n1)
            print(f"Valor sacado R${saldo:.2f}")
            _ = input("-->Enter para finalizar...")
            exit()
        else:
            exit()


    else:
        print("Opção invalida tente novamente!")
        _ = input("-->Enter para continuar...")
        caixa(saldo, qtNota100, qtNota50, qtNota20, qtNota10, qtNota5, qtNota2, qtNota1)

def main():
    
    caixa(188,1,1,1,1,1,1,1)

main()