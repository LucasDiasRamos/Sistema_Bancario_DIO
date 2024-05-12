import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def deposito (valor,saldo,extrato):
    print('Depósito')

    if valor > 0:
        saldo += valor
        extrato += f"Deposito de R${valor:.2f} \n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\nOperação falhou!Valor informado inválido")

    return saldo, extrato

def saque (*,valor ,limite,numero_de_saques,saldo,limite_saques,extrato):
        print('Saque')

        if limite_saques == 0:
            print(
                "Não foi possivel realizar o Saque. Pois Todos os saques diarios foram realizados")

        elif valor > limite:
            print(
                "Não foi possivel realizar o Saque. Valor Informado Maior que o limite da conta")

        elif valor > saldo:
            print("Não foi possivel realizar o Saque. Saldo Insulficiente")

        elif valor > 0:
            print("Saque realizado")
            limite_saques -= 1
            numero_de_saques += 1
            extrato += f"Saque de R${valor:.2f}\n"
            saldo -= valor
            
        else:
            print("Não foi possivel realizar o saque, tente novamente.")

        return saldo, extrato

def exibir_extrato (saldo, / , *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print('Não foram realizadas Movimentanções na sua conta.')
    else:
        print(extrato)    
    
    print(f"\nSaldo: R$ {saldo:.2f} ")
    print("==========================================")



def cria_usuario(usuario):
    cpf = input('Digite seu CPF (somente os números): ')
    cpf_validado =valida_cpf(cpf,usuario)

    if cpf_validado:
        print('CPF já cadastrado')
        return

    nome = input('Digite seu nome: ')
    dt_nascimento = input('Digite sua Data de Nascimento (dia/mes/ano):' )
    endereco = input('Digite seu endereço (logradouro,numero - bairro - cidade/sigla do estado): ')

    usuario.append({'CPF':cpf,'nome':nome,'Data de Nascimento':dt_nascimento,'Endereço':endereco})
    print("=== Usuário criado com sucesso! ===") 

def valida_cpf(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        
def cria_conta_corrente (agencia,usarios,num_conta):
    cpf = input('Digite o seu CPF (somente os números): ')
    cpf_validado = valida_cpf(cpf,usarios)
  

    if cpf_validado:
        print('======Conta criada com Sucesso======')
        return ({'Agencia':agencia,'Número conta':num_conta,'usuario':cpf_validado})
    else:
        print('Erro ao criar conta')
        return

def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['Agencia']}
            C/C:\t\t{conta['Número conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))




def main():
    global menu
    
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    usuario = []
    contas =[]
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 0
    

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Digite o valor do Depósito: R$ "))
            saldo, extrato =deposito(valor,saldo,extrato)

        
        elif opcao == 's':
            valor = float(input("Digite o valor de saque: R$ "))

            saldo,extrato = saque(
                    valor=valor,
                    limite = limite,
                    saldo=saldo,
                    numero_de_saques= numero_saques,
                    limite_saques=LIMITE_SAQUES,
                    extrato=extrato
                )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            cria_usuario(usuario)
        
        elif opcao == 'nc':
            numero_conta =len(contas)+1
            conta = cria_conta_corrente(AGENCIA,usuario,numero_conta)

            if conta:
                contas.append(conta)
        
        elif opcao =='lc':
            listar_conta(contas)

        elif opcao == 'q':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()