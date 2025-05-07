print("\n*****Bem-vindo ao sistema bancário*****")


menu = """
 
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [0] Sair

  """


saldo = 0
valor_maximo = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES_DIA = 3

while True:
    print("\n*****Escolha uma opção*****")
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))

        if valor > saldo:
            print("\nOperação falhou! Saldo insuficiente.")
        elif valor > valor_maximo:
            print("\nOperação falhou! O valor do saque excede o limite permitido de R$500,00.")
        elif qtd_saques >= LIMITE_SAQUES_DIA:
            print("\nOperação falhou! Limite máximo de três saques por dia atingido!")
        elif valor > 0:
            saldo -= valor
            qtd_saques += 1
            extrato += f"Saque de: R$ {valor:.2f}\n"
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n************Extrato************")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "0":
        break
    
    else:
        print("\nOpção inválida, por favor selecione uma opção válida.")
