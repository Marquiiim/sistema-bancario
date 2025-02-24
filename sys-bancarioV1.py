# 1 - É POSSÍVEL DEPOSITAR APENAS VALORES POSITIVOS
# 2 - TRABALHANDO APENAS COM UM USUÁRIO, SEM IDENTIFICAÇÃO
# 3 - TODOS DEPÓSITOS DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO.
# 4 - APENAS 3 SAQUES DIÁRIOS
# 5 - LIMITE DE 500 REAIS
# 6 - CASO NÃO HAJA SALDO, EXIBIR MENSAGEM

# VARIÁVEIS INICIAIS

balance = 0
LIMIT = 500
extract = ""
number_withdrawals = 0
LIMIT_WITHDRAWALS = 3

# TEMPLATES

menu = """"
======== MENU BANCÁRIO ========
        [D] Depositar
        [S] Sacar
        [E] Extrato
        [X] Sair do sistema
===============================
=>"""

deposit_menu = f"""
======== ÁREA DE DEPÓSITO ========
Saldo atual da conta: R${balance:.2f}

    Digite o valor do deposito:
=>"""

withdraw_menu = f"""
======== ÁREA DE SAQUE ========
Saldo atual da conta: R${balance:.2f}

    Digite o valor do saque:
=>"""

# FUNÇÕES

def deposit(value):
    global balance, number_withdrawals, extract

    balance += value
    number_withdrawals += 1

def withdraw(value):
    global balance, number_withdrawals, extract

    balance -= value
    number_withdrawals += 1


# OPÇÕES

while True:

    option = input(menu).upper()

    if option == "D":
        
        value_deposit = float(input(deposit_menu))

        if value_deposit >= 0:
            SystemError("[ERROR] Valor invalido, tente novamente.")
        else:
            deposit(value_deposit)
            print(deposit_menu)

    elif option == "S":

        value_withdraw = float(input(withdraw_menu))

        if value_withdraw > balance and value_withdraw > LIMIT:
            SystemError("[ERROR] Não foi possível realizar o saque, verifique seu limite de saque ou seu saldo atual.")
        else:
            withdraw(value_withdraw)
            print(withdraw_menu)


    elif option == "E":
        print("teste")
    elif option == "X":
        raise SystemExit("Operação finalizada.")
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")