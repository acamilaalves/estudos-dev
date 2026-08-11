# Exercício 1
# Peça ao usuário para digitar a temperatura atual em Celsius.
# Se for maior ou igual a 30, exiba "está muito quente". Se estiver
# acima ou igual a 20 e abaixo de 30, exiba "está agradavel". Se estiver
# abaixo de 20 exiba "está muito frio".

# temperatura_atual = float(input("Digite a temperatura atual em Celsius: "))
# if temperatura_atual >= 30:
#     print("Está muito quente.")
# elif (temperatura_atual >= 20) and (temperatura_atual < 30):
#     print("Está agradável.")
# else:
#     print("Está muito frio.")


# Exercício 2
# Peça ao usuário para digitar a idade de uma pessoa. Com base nessa idade, informe
# o valor da tarifa de transporte que terá que ser paga. 
# Se a idade for menor de 6 anos a tarifa será gratuita. 
# Se for acima ou igual a 6 anos e abaixo de 18 anos, meia tarifa (5 reais).
# Se for a partir de 18 anos e abaixo de 60 anos, tarifa inteira (10 reais).
# Se for idoso (acima de 60 anos), tarifa gratuita.

idade = int(input("Digite a sua idade: "))
if idade < 6:
    print("A tarifa é gratuita.")
elif (idade >= 6) and (idade < 18):
    print("A tarifa é meia (5 reais).")
elif (idade >= 18) and (idade < 60):
    print("A tarifa é inteira (10 reais).")
else:
    print("A tarifa é gratuita.")

# Exercício 3
# Peça ao usuário para digitar um username e uma senha. Considere que o usuário correto é
# "admin" e a senha correta é "pyhton2026". Se as credenciais estiverem corretasm exiba "login bem sucedido".
# Do contrário, exiba "Login e senha inválidos".

username = input("Digite o username: ")
senha = input("Digite a senha: ")
if (username == "admin") and (senha == "python2026"):
    print("Login bem sucedido.")
else:
    print("Login e senha inválidos.")