# COLEÇÕES DE PYTHON

# Variável: Guarda apenas um valor por vez
# Coleção: Guarda vários valores por vez

# Principais tipos de coleções em Python:
# 1. Listas: elementos ordenados, mutáveis e permitem duplicatas.(com posição)
# 2. Tuplas: elementos ordenados, imutáveis e permitem duplicatas.(com posição)
# 3. Conjuntos: elementos não ordenados, mutáveis e não podem se repetir.(sem posição)
# 4. Dicionários: elementos na forma de pares chave-valor.

#--------------------------------------------------------------------------------------------

# LISTAS: elementos ordenados (com posição), mutáveis e permitem duplicatas. São representadas por colchetes [].

# LISTAS:
#              0       1       2
# animais = ["Cão", "Gato", "Coelho"]
# print(animais)

# print("Posições positivas")
# print (animais[0]) # Acessando o elemento da posição 0
# print (animais[2])

# print("Posições negativas")
# print (animais[-1]) # Acessando o elemento da posição -1 (coelho)
# print (animais[-3]) # cão

# LISTA MISTA

# lista_mista = [10, "teclado", 2.60]
# print("Lista inteira")
# print(lista_mista)

# print("Posições positivas")
# print(lista_mista[0]) # Acessando o elemento da posição 0
# print(lista_mista[1]) # Acessando o elemento da posição 1

# append(valor) - Adiciona um elemento no final da lista
# insert(posição, valor) - Adiciona um elemento em uma "posição" específica da lista

# lista = [10, 11, 12, 13]
# print(f"Tipo da lista: {type(lista)}")
# print("Lista antes do append")
# print(lista)

# lista.append(14)
# print("Lista após o append")
# print(lista)

# FUNÇÃO INSERT(,)
# lista =[5.4, 5.5, 5.6]

# print(f"Tipo dalista: {type(lista)}")

# print("Lista antes do insert")
# print(lista)

# lista.insert(2, 5.55)

# print("Lista após o insert")
# print(lista)

# REMOVE(VALOR) - Remove o primeiro elemento da lista que for igual ao valor passado como parâmetro
# lista =["Batata", "Beterraba", "Gerimum"]
# print(f"Tipo da minha lista: {type(lista)}")

# print("Lista antes do remove")
# print(lista)

# lista.remove("Beterraba")

# print("Lista após o remove")
# print(lista)

#POP(posição) - Remove o elemento da posição passada como parâmetro e retorna o valor removido

# lista = [2.54, False, "Caneta"]
# print(f"Tipo da minha lista: {type(lista)}")

# print("Lista antes do pop")
# print(lista)

# tam = len(lista)
# print(f"Tamanho da lista: {tam}")

# lista.pop(1)

# print("Lista após o pop")
# print(lista)

# tam = len(lista)
# print(f"Tamanho da lista: {tam}")

lista = [10, 20, 30, 40, 50]
print("Lista antes da modificação")
print(lista)

lista [2]= 3000

print("Lista após a modificação")
print(lista)