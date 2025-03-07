from datetime import datetime, timedelta

# VARIÁVEIS INICIAIS

balance = 0
LIMIT = 500
extract = []
number_withdrawals = 0
number_transaction = 0
date_now = datetime.now()
date_next = date_now - timedelta(days=1)

"""
============= REGRAS TRANSACIONAIS =============
            LIMIT_WITHDRAWALS = 3
            LIMIT_TRANSACTION = 10
"""

# TEMPLATES

menu = """"
======== MENU BANCÁRIO ========
        [D] Depositar
        [S] Sacar
        [E] Extrato
        [X] Sair do sistema
===============================
=>"""

# FUNÇÕES

def deposit(value):
    global balance, number_transaction, extract

    balance += value
    extract.append(f"Depósito - R$ +{value:.2f} | Dia: {date_now.strftime('%d/%m/%Y')} - {date_now.strftime('%H:%M:%S')}")
    number_transaction += 1

def withdraw(value):
    global balance, number_transaction, number_withdrawals, extract

    balance -= value
    extract.append(f"Saque - R$ - {value:.2f} | Dia: {date_now.strftime('%d/%m/%Y')} - {date_now.strftime('%H:%M:%S')}")
    number_withdrawals += 1
    number_transaction +=1


# OPÇÕES

while True:

    option = input(menu).upper()


    if option == "D":
        while True:
            value_deposit = float(input(
                f"""
                ============= ÁREA DE DEPÓSITO =============
                Saldo atual da conta: R${balance:.2f}

                Digite o valor do deposito:
                =>"""
            ))

            if value_deposit >= 0:
                if number_transaction == 10:
                    print(f"[ERROR] Você excedeu o número de transações diárias, só poderá fazer novas transações a partir do dia {date_next.strftime('%d/%m/%Y')} - {date_next.strftime('%H:%M:%S')}")
                    break

                else:
                    deposit(value_deposit)
                    print(f"""
                        Valor de R${value_deposit} depositado com sucesso!

                        Saldo atual da conta: R${balance:.2f}
                    """)
                    break

            else:
                print("[ERROR] Valor inválido, tente novamente.")


    elif option == "S":
        while True:
            value_withdraw = float(input(
                f"""
                ============= ÁREA DE SAQUE =============
                Saldo atual da conta: R${balance:.2f}

                Digite o valor do saque:
                =>"""
            ))

            if value_withdraw > balance:
                print(f"[ERROR] Seu saldo atual é de apenas R${balance:.2f}, não foi possível realizar o saque.")

            elif value_withdraw > LIMIT:
                print(f"[ERROR] Limite de saque de no máximo R${LIMIT:.2f} por dia.")
            
            else:
                if number_transaction > 10:
                    print(f"[ERROR] Você excedeu o número de transações diárias, só poderá fazer novas transações a partir do dia {date_next.strftime('%d/%m/%Y')} - {date_next.strftime('%H:%M:%S')}")
                    break

                else:
                    withdraw(value_withdraw)
                    print(f"""
                    Valor de R${value_withdraw} retirado com sucesso!

                    Saldo atual da conta: R${balance:.2f}
                    """)
                    break


    elif option == "E":
        extract_str = "\n".join(extract)
        extract_bank = f"""
    ============= EXTRATO =============
    {extract_str if extract else "Não foram realizadas movimentações"}
    """

        print(extract_bank)

    elif option == "X":
        raise SystemExit("Operação finalizada com sucesso, até a próxima.")
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")