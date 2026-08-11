# Exercício 1
# Crie uma lista chamada países com alguns nomes de países dentro dela. Em seguida:
# - Adicione um novo país ao fim da lista.
# - Adicione um novo país antes da posição 1
# - Remova um país pelo nome
# - Remova um país pelo índice
# - Mostre o total de países na lista.

# paises = ["Brasil", "Argentina", "Chile"]
# print("Lista de países inicial:", paises)

# paises.append("Portugal")
# print("Após adicionar Portugal:", paises)

# paises.insert(0,"Alemanha")
# print("Após adicionar Alemanha:", paises)

# paises.remove("Chile")
# print("Após remover Chile:", paises)

# paises.pop(2)
# print("Após remover país na posição 2:", paises)

# len(paises)
# print("Total de países na lista:", len(paises))


# Exercício 2
# Crie um dicionário que armazene as informações de um carro, informações essas que
# serão a marca, modelo e ano. Em seguida, exiba uma frase apresentando essas informações do carro,
# no seguinte formato: O carro é um MARCA MODELO do ano ANO.

# dicionario_carro = {
#     "Marca": "Toyota",
#     "Modelo": "Corolla",
#     "Ano": 2020}

# print(f"O carro é um {dicionario_carro['Marca']} {dicionario_carro['Modelo']} do ano {dicionario_carro['Ano']}")

# Exercício 3
# Crie uma lista com números repetidos, e através da conversão desta para um conjunto, elimine os valores
# duplicados.

lista = [1, 4, 3, 1, 6, 5]

print(f"Tipo da lista: {type(lista)}")
print(lista)

conjunto_convertido = set(lista)
print(f"Tipo do conjunto convertido: {type(conjunto_convertido)}")
print(conjunto_convertido)

lista_convertida = list(conjunto_convertido)
print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida)



