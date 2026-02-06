# Exercício 1

# Peça ao usuário para digitar o nome dele e exiba uma saudação personalizada.
# Ex. Olá, Fulano! Bem-vindo ao curso de Python!

# usuario = input("Digite seu nome: ")
# print(f"Olá, {usuario}! Bem-vindo ao curso de Python!")

# Exercício 2

# Peça dois números inteiros ao usuário, some-os e apresente o resultado em uma frase no formato a baixo.
# Ex. O resultado é 20.

# numero = int(input("Digite um número inteiro: "))
# numero2 = int(input("Digite outro número inteiro: "))
# soma = numero + numero2
# print(f"O resultado é {soma}.")

# Exercício 3

# Peça duas notas ao usuário (podem ter casas decimais) e mostre a média delas.

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota1 + nota2) / 2
# media_round = round(media, 1)  # Arredonda a média para 1 casa decimal ou mais.
# print(f"A média das notas é {media_round}.") # ou somente media, sem arredondar. O resultado será a média das notas digitadas pelo usuário.

# Exercício 4

# Peça ao usuário o nome, idade e estado dele, e exiba uma frase completa no formato abaixo.
# Ex. Fulano tem 25 anos e mora em São Paulo.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
estado = input("Digite o estado onde você mora: ")
# print(f"{nome} tem {idade} anos e mora em {estado}.")

# outra forma de armazenar o print

frase = f"{nome} tem {idade} anos e mora em {estado}."
print(frase)