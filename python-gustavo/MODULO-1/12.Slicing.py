# SLICING DE LISTA (FATIAMENTO)

# É uma forma de pegar apenas uma parte de uma lista. Pense em uma pizza, você não precisa pegar a pizza inteira;
# pode pegar apenas  algumas fatias. O Slicing faz exatamente isso com uma lista.

# REGRA: O índice inicial é INCLUSIVO e o índice final é EXCLUSIVO.

# Em outras palavras o python começa em início e para antes de chegar em fim.


# ex:   A , B, C, D, E
#       0  1   2   3  4         Se escrever: lista[1:4] -> ['b', 'c', 'd']  (começa no índice 1 e para antes do índice 4)

# SINTAXE

# Inicio: onde começa
# Fim: onde termina (não inclui o índice final)
#lista[inicio:fim]

# Se omitir o início: o python assume que é 0 (zero) e começa do primeiro elemento
#print(frutas[:3])  # ['maçã', 'banana', 'laranja']

# Se omitir o fim: o python assume que é o tamanho da lista e vai até o último elemento
#print(frutas[2:])  # ['laranja', 'uva', 'abacaxi']

# Copiar a lista inteira: isso cria uma cópia da lista original, mas não é a mesma lista 
# (ou seja, se você alterar a cópia, a lista original não será alterada)
#print(frutas[:])  # ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']

# Indices negativos: você pode usar índices negativos para acessar elementos a partir do final da lista
# (ou seja, -1 é o último elemento, -2 é o penúltimo, e assim por diante)
# Exemplo: frutas[-3:-1]  # ['laranja', 'uva']
#print(frutas[-2:])  # ['uva', 'abacaxi']

# Passo: você pode usar um terceiro parâmetro para especificar o passo (ou seja, quantos elementos pular)
#lista[inicio:fim:passo]

# de 2 em 2:
# exemplo: numeros=[1, 2, 3, 4, 5, 6, 7, 8]
# print(numeros[::2])  # [1, 3, 5, 7] (começa do início e vai até o final, pegando de 2 em 2)

# Invertendo a lista: você pode usar um passo negativo para inverter a lista (o python vai percorrer a lista de trás pra frente)
# exemplo: lista=[1, 2, 3, 4, 5, 6, 7, 8]
# print(numeros[::-1])  # [8, 7, 6, 5, 4, 3, 2, 1]

# Exemplos práticos:

# Primeiros 3 elementos: lista[:3]
# Últimos 3 elementos: lista[-3:]
# Do indice 2 até o final: lista[2:]
# Do inicio até o índice 4 (não incluindo o índice 4): lista[:4]
# Elementos de 2 em 2: lista[::2]
# Lista invertida: lista[::-1]