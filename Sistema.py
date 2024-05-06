print(" BANCO DIO ".center(20, "-"))

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        deposito = float(input("Digite o valor do Depósito: R$ "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito de R${deposito:.2f} \n"
        else:
            print("Valor informado inválido")

    elif opcao == 's':
        print('Saque')

        saque = float(input("Digite o valor de saque: R$ "))

        if LIMITE_SAQUES == 0:
            print(
                "Não foi possivel realizar o Saque. Pois Todos os saques diarios foram realizados")

        elif saque > limite:
            print(
                "Não foi possivel realizar o Saque. Valor Informado Maior que o limite da conta")

        elif saque > saldo:
            print("Não foi possivel realizar o Saque. Saldo Insulficiente")

        elif saque > 0:
            print("Saque realizado")
            LIMITE_SAQUES -= 1
            extrato += f"Saque de R${saque:.2f}\n"
            saldo -= saque
            
        else:
            print("Não foi possivel realizar o saque, tente novamente.")

    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        if not extrato:
            print('Não foram realizadas Movimentanções na sua conta.')
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f} ")
        print("==========================================")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
