# Simulando um caixa eletrônico simples

# O usuário tem um saldo inicial de R$500,00 e pode sacar dinheiro até zerar o saldo ou encerrar.

print("BEM-VINDO AO CAIXA ELETRÔNICO")
print("-----------------------------------------")

saldo = 1000
extrato = []

while True:
    print("MENU INICIAL:")
    print("Saldo Atual: 1")
    print("Saque: 2")
    print("Depósito: 3")
    print("Extrato: 4")
    print("Sair: 0")
    print("-----------------------------------------")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Por favor, digite apenas números.")
        continue   
    #SALDO
    if opcao == 1:
        print(f"Seu saldo atual é R$ {saldo}")
    # SAQUE
    elif opcao == 2:
        try:
            saque = float(input("Informe o valor que deseja sacar:"))
        except ValueError:
            print("Valor inválido!")
            continue

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            extrato.append(f"Saque: R$ {saque:.2f}")
            print(f"Saque realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}")

        # DEPÓSITO
    elif opcao == 3:
        try:
            deposito = float(input("Informe o valor que deseja depositar:"))
        except ValueError:
            print("Valor inválido!")
            continue

        if deposito <= 0:
            print("O valor do depósito deve ser maior que zero.")
        else:
            saldo += deposito
            extrato.append(f"Depósito: R$ {deposito:.2f}")
            print(f"Depósito realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}")
        
    # EXTRATO
elif opcao == 4:
    print("------- EXTRATO -------")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimento in extrato:
            print(movimento)
        print(f"Saldo atual: R$ {saldo:.2f}")

# SAIR
elif opcao == 0:
    print("Encerrando o atendimento. Obrigado por usar o caixa eletrônico!")
    break
    
else:
    print("Opção inválida! Por favor, selecione uma opção válida.")