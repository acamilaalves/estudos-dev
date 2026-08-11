# Crie uma função que receba um número inteiro como argumento e retorne "Even"
#  para números pares ou "Odd" para números ímpares.

# def even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
    
#     return "Odd"

# print(even_or_odd(12))
# print(even_or_odd(-4))
# print(even_or_odd(134))
# print(even_or_odd(11))

#------------------------------------------------------

# Escreva uma função que receba um número inteiro não negativo n e uma strings como 
# parâmetros e retorne uma string composta por s repetida exatamente n vezes.

# Exemplos (entrada -> saída)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

# def repeat_str(repeat, string):
#     return repeat * string

# print(repeat_str(5, "Camila"))

#------------------------------------------------------

# Nesta tarefa simples, você recebe um número e precisa torná-lo negativo. 
# Mas talvez o número já seja negativo?

# Exemplos
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0

# def make_negative( number ):
#     if number > 0:
#         return -number
#     return number

# print(make_negative(1))
# print(make_negative(-5))
# print(make_negative(0))

#------------------------------------------------------
# Considere uma matriz/lista de ovelhas onde algumas ovelhas podem estar faltando em seus lugares. 
# Precisamos de uma função que contenha o número de ovelhas presentes no array 
# (verdadeiro significa presente).
# Por exemplo,

# lista = [True, True, True, False,
# True, True, True, True,
# True, False, True, False,
# True, False, False, True,
# True, True, True, True,
# False, False, True, True]
# # A resposta correta seria 17.

# # minha solução
# def count_sheeps(sheep):
#     return sheep.count(True)

# print(count_sheeps(lista))

# ------------------------------------------------

# Você consegue encontrar uma agulha no palheiro?

# Escreva uma função findNeedle() que receba uma lista cheia de lixo, mas que contenha 
# um único elemento."needle"
# Após sua função encontrar a agulha, ela deverá retornar uma mensagem (em formato de texto) que diga:
# "encontrei a agulha na posição "Além disso, index encontrou a agulha, então:

# Exemplo (Entrada --> Saída)
#         0        1      2      3       4           5           6
# lista = ["hay", "junk", "hay", "needle", "moreJunk", "hay", "randomJunk"]
# #  "encontrei a agulha na posição 5" 
# # Observação: Em COBOL, deve retornar “encontrei a agulha na posição 6”

# def find_needle(haystack):
#     index = haystack.index("needle")
#     return f"encontrei a agulha na posição {index}"

# print(find_needle(lista))

#----------------------------------------------------

# Dado um conjunto de números, retorne o inverso aditivo de cada um. 
# Cada número positivo se torna negativo e os negativos se tornam positivos.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# Você pode assumir que todos os valores são inteiros. Não modifique o array de entrada.
# lst = [1, -2, -3, 4, 5]

# def invert(list):
#     inverted_list = []

#     for item in list:
#         inverted_item = item * -1
#         inverted_list.append(inverted_item)

#     return inverted_list

# input_list = [1, 2, 3, 4, 5]
# print(invert(input_list)) 

# input_list = [1, -2, 3, -4, 5]
# print(invert(input_list))

# ---------------------------------------------------

# Dado um vetor de números inteiros, sua solução deve encontrar o menor número inteiro.
# Por exemplo:
# Dada [34, 15, 88, 2]a sua solução, retornará2
# Dada [34, -345, -1, 100]a sua solução, retornará-345
# Para efeitos deste kata, pode assumir que o array fornecido não estará vazio.

# def find_smallest_int(arr):
#     return max(arr)

# arr = [34, 15, 88, 2]
# print(find_smallest_int(arr))

#----------------------------------------------

# O primeiro século abrange o período do ano 1 até o ano 100, inclusive ; o segundo século, do ano 101 até o ano 200, inclusive ; e assim por diante.

# Tarefa
# Dado um ano, retorne o século em que ele se encontra.

# Exemplos
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28

# def century(year):
#     return (year - 1) // 100 + 1

# century = century(1900)
# print(century)

# -----------------------------------------------

# Escreva uma função partlistque retorne todas as maneiras de dividir uma lista (ou array) com pelo menos dois elementos em duas partes não vazias.

# Cada duas partes não vazias estarão em um par (ou em um array para linguagens sem tuplas ou structem C - C: veja Exemplos Casos de teste - ).
# Cada parte estará em uma string
# Os elementos de um par devem estar na mesma ordem que no array original.
# Exemplos de retornos em diferentes idiomas:

# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# [["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"], ["az toto picaro", "zone kiwi"], ["az toto picaro zone", "kiwi"]] 
# or
#  a = {"az", "toto", "picaro", "zone", "kiwi"} -->
# {{"az", "toto picaro zone kiwi"}, {"az toto", "picaro zone kiwi"}, {"az toto picaro", "zone kiwi"}, {"az toto picaro zone", "kiwi"}}
# or
# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]
# or 
# a = [|"az", "toto", "picaro", "zone", "kiwi"|] -->
# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]
# or
# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# "(az, toto picaro zone kiwi)(az toto, picaro zone kiwi)(az toto picaro, zone kiwi)(az toto picaro zone, kiwi)"

#                             [LIMITE]
# lista: ["az", "toto", "picaro", "zone", "kiwi"]
# #posições: 0,    1,      2,        3,      4

# primeiro_pedaco = "az toto"
# segundo_pedaco= "picaro zone kiwi"
# tupla= ("az toto picaro zone", "kiwi")
# lista_resultante = [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]

#---------------------------------------

# posições        0         1           2           3       4
# minha_lista = ["Brasil","Argentina", "Colômbia", "Peru", "Bolívia"]

# primeiro_pedaco = minha_lista[:2]
# print(f"Primeiro pedaço: {primeiro_pedaco}")

# segundo_pedaco = minha_lista[2:]
# print(f"Segundo pedaço: {segundo_pedaco}")

# JOIN

# separador = " , "
# minha_lista = ["Azul", "Amarelo", "Laranja"]
# string_resultante = separador.join(minha_lista)

# print(string_resultante)

# def partlist(lista_entrada):
#     lista_resultante = []
#     tam_lista = len(lista_entrada)
#     espaco = " "

#     # range (1, 5): 1, 2, 3, 4
#     for limite in range(1, tam_lista):
#         primeiro_pedaco_sublista = lista_entrada[:limite]
#         segundo_pedaco_sublista = lista_entrada[limite:]

#         primeiro_pedaco_str = espaco.join(primeiro_pedaco_sublista)
#         segundo_pedaco_str = espaco.join(segundo_pedaco_sublista)

#         tupla = (primeiro_pedaco_str, segundo_pedaco_str)

#         lista_resultante.append(tupla)

#     return lista_resultante
#         #print(primeiro_pedaco)
#         #print(segundo_pedaco)

# lista_entrada = ["Brasil", "Japão", "Argentina", "América"]
# print(partlist(lista_entrada))

# separador = " "
# minha_lista = ["az", "toto", "picaro", "zone", "kiwi"]
# string_resultante = separador.join(minha_lista)

# print(string_resultante)

# def partlist(arr):
#     return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]

# print(partlist(["az", "toto", "picaro", "zone", "kiwi"]))

# -----------------------------

# No encontro familiar anual, a família gosta de descobrir a idade do membro mais velho e 
# do mais novo da família e calcular a diferença entre elas. Você receberá um array com as idades de 
# todos os membros da família, em qualquer ordem. As idades serão dadas em números inteiros, então
#  um bebê de 5 meses terá a 'idade' atribuída de 0. Retorne um novo array (uma tupla em Python) 
# com [idade do membro mais novo, idade do membro mais velho, diferença entre a idade do membro 
# mais novo e a do membro mais velho].

# def difference_in_ages(ages):
#     idade_mais_novo = min(ages)
#     idade_mais_velho = max(ages)
#     diferenca_idade = idade_mais_velho - idade_mais_novo
#     return (idade_mais_novo, idade_mais_velho, diferenca_idade)

# ages = [82, 15, 6, 38, 35]

# print(idade_mais_novo := min(ages))
# print(idade_mais_velho := max(ages))
# print(diferenca_idade := idade_mais_velho - idade_mais_novo)