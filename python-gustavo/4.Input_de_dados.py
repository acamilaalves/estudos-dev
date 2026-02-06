# INPUT DE DADOS (ENTRADA DE DADOS)
# Neste arquivo, vamos aprender a como receber dados do usuário em Python.
# A função input() é usada para receber dados do usuário.
# Exemplo básico de uso da função input():

# nome = input()
# ou
# nome  = input("Digite seu nome: ")
# print(f"Bem-vindo, {nome}")

# numero = input("Olá, informe um número: ")

# print(numero - 1)
# print(f"O número que você digitou foi: {numero}")

# Experimeto:
# print(type(numero))  # O tipo de classe recebido será uma string, mesmo que o usuário digite um número, ele será tratado como uma string, pois sempre que terá um input ele nos devolverá uma string.

# No python dá erro quanto você tenta diminuir um texto (string) de um número. Como no exemplo acima. Para resolver isso, podemos usar a função int() para converter a string em um número inteiro, ou a função float() para converter a string em um número decimal.

# numero = int(input("Olá, informe um número: "))
# print(type(numero))  

# Agora o tipo de classe recebido será um inteiro, pois usamos a função int() para converter a string em um número inteiro.
# print(f"O número que você digitou menos 1 é: {numero - 1}")

# numero = int(input("Informe um número inteiro: "))
# numero_decimal = float(input("Agora informe um número decimal: "))

# print(type(numero))  # O tipo de classe recebido será um inteiro, pois usamos a função int() para converter a string em um número inteiro.
# print(type(numero_decimal))  # o tipo de classe recebido será um float, pois usamos a função float() para converter a string em um número decimal.

nome = input("Informe seu nome: ")
numero = int(input("Informe um número: "))

print(type(numero))
print (type(nome))
print(numero + 10)

# print(numero * 5)  # O resultado será a string repetida 5 vezes, pois o tipo de classe recebido é uma string.

print(f"Seu nome é {nome} e seu número é {numero}")  # O resultado será a string formatada com o nome e o número do usuário.