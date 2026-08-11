# TUPLAS: elementos ordenados (com posição) e não podem ser alterados. São representadas por parênteses ().

# tupla = (10, 20, 30)
# print(f"Tipo da tupla: {type(tupla)}")

# print("Tupla toda")
# print(tupla)

# print("Primeiro elemento da tupla")
# print(tupla[0])

# print("Terceiro elemento da tupla")
# print(tupla[2])

# Convertendo tupla para lista

tupla = (10, 20, 30)
print(f"Tipo da tupla: {type(tupla)}")

lista_convertida = list(tupla)

print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida)

# convertendo de volta para tupla

lista_convertida[1] = 1000
tupla_convertida = tuple(lista_convertida)

print(tupla_convertida)
