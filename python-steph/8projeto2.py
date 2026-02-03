# Simulando um caixa eletrônico simples

# O usuário tem um saldo inicial de R$500,00 e pode sacar dinheiro até zerar o saldo ou encerrar.

print("BEM-VINDO AO CAIXA ELETRÔNICO")
print("-----------------------------------------")

saldo = 500

while saldo > 0:
    saque = float(input("Informe o valor que deseja sacar OU digite 0 para sair:"))

    if saque == 0:
        break

    if saque > saldo:
        print(f"Saldo insuficiente! Seu saldo atual é R$ {saldo}")
    else: 
        saldo -= saque
        print(f"Saque efetuado com sucesso! Seu saldo atual é R$ {saldo:.2f}")    



    # inteiros: 1, 2, 3, 4, 5
    # float: 10.50
