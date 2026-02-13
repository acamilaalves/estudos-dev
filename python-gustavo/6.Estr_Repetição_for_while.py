# ESTRUTURAS DE REPETIÇÃO

# Também conhecidas como loops. Um bloco de código pode ser executado várias vezes, até
# que uma condição seja atingida.

# Principais: FOR e WHILE

# FOR: Quando queremos repetir um número específico de vezes.(Sabemos o número de repetições)

# WHILE: Quando queremos repetir até que uma condição seja atingida.(Não sabemos o número de repetições)

# Estrutura FOR
# for INDICE in SEQUENCIA DE VALORES:
#     comando_1
#     comando_2

# range(): retorna uma sequencia de valores dentro de uma faixa.
# ex: range (1, 6) retorna [1, 2, 3, 4, 5] # Por padrão o ultimo número de uma range não entra na lista.

# somatorio = 0
# sequencia: [1, 2, 3, 4, 5]
# i = 1
# somatorio = 0 + 1-> 1
# i = 2
# somatorio = 1 + 2 -> 3
# i = 3
# somatorio = 3 + 3-> 6
# i = 4
# somatorio = 6 + 4-> 10
# i = 5
# somatorio = 10 + 5-> 15

# somatorio = 0
# for i in range(1, 6):
#     print(f"Executando pela {i}ª vez")
#     # somatorio = somatorio + i
#     # somatorio += i -> formas reduzidas de escrever a linha acima.
#     # somatorio = somatorio - i 
#     # somatorio -= i

# print(f"Somatório dos números: {somatorio}")
# print("Acabou o loop FOR")


# Estrutura WHILE

# while CONDIÇÃO:
#     comando_1
#     comando_2
#     comando_3

# OBS: É fundamental que dentro do bloco de código de uma estrutura while, algo possa 
# causar uma mudança na condição, para que ela deixe de ser verdadeira em algum momento, caso contrário, teremos um loop infinito.
# ex:

# atribuição inicial da senha

# senha = input("Informe a senha: ")

# while senha != "cdc123":
#     print("Senha incorreta, tente novamente.")
#     senha = input("Informe a senha: ")

# print("Senha correta. Fim do while.")

# LOOP INFINITO

palavra = "notebook"

while palavra == "notebook":
    print("A palavra é notebook.")
    palavra = input("Nova palavra: ")
print("Acabou o loop while.")

# APERTE CTRL + C PARA INTERROMPER O LOOP INFINITO.