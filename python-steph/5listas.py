# LISTAS E TUPLAS

# Tipos de dados que armazenam multiplos valores, mas tem diferenças importantes.

# LISTAS:
# - Modificáveis (podem ser alteradas depois de criadas, pode adicionar, remover e alterar valores)
# - Mais lenta
# - Quando precisamos modificar dados

# TUPLAS:
# - Não é modificavel (uma vez criada, não pode ser alterada)
# - Mais rápida
# - Quando os dados não devem ser alterados

# Lista
# Definida entr colchetes [] e pode armazenar diferentes tipos de dados.

# frutas = ["maçã", "banana", "laranja"]
# numeros = [1, 2, 3, 4, 5]
# misturado = ["Python",3.14, True]

# Acessando elementos da lista

#print(frutas[0])  # Saída: maçã
#print(frutas[1])  # Saída: banana
#print(frutas[2])  # Saída: laranja
#print(frutas[-1])  # Saída: laranja

# Alterando um valor na lista
#print(frutas)

#frutas [1] = "uva"
#print(frutas) # Saída: ['maçã', 'uva', 'laranja']

# Adicionando elementos à lista

#append (): Adiciona um item ao final da lista.
#insert (): Adiciona um item em uma posição específica.

#numeros = [1, 2, 3]
#print(numeros)

#numeros.append(4)
#print(numeros)          # [1, 2, 3, 4]

#numeros.insert(3, 8)
#print(numeros)         # [1, 10, 2, 3, 4] (inseriu o 10 na posição 1)

# Removendo elementos da lista

# remove(): Remove um item pelo valor
# pop(): remove um item pelo índice (ou o último item se nenhum índice for passado)

#frutas = ["maçã", "banana", "laranja","uva"]
#frutas.remove("banana")
#print(frutas)                        

#frutas.pop(0)
#print(frutas)        

# frutas.pop()
# print(frutas)

# TUPLAS
# São como listas,mas imutáveis. Elas são criadas com parênteses ().

# cores = ("vermelho", "azul", "verde")
# numeros = (1, 2, 3, 4, 5)

# # Acessando elementos da tuplas
# print(cores[0])  # "vermelho"
# print(cores[-1]) # "verde"

# # Tentando mofificar uma tupla (Erro!)
# cores[1] ="amarelo"  # Isso causará um erro, pois tuplas são imutáveis.

# Convertendo entre listas e tuplas
#Podemos converter uma tupla para uma lista e modificar os elementos.

# tupla = (1, 2, 3)
# lista = list(tupla)     # Converte tupla para lista
# lista.append(4)         # Modifica a lista
# tupla = tuple(lista)    # Converte de volta para tupla
# print(tupla)            # (1, 2, 3, 4)

meses = ("janeiro", "fevereiro", "março", "abril")
print(meses [2])  # Saída: março