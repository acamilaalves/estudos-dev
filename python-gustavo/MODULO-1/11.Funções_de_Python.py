# FUNÇÕES

# Funções são blocos de código separados e reutilizaveis, cada um tendo um objetivo e/ou tarefa específica.

# Estrutura de uma função no Python:

# def NOME_FUNCAO(PARAM_1, PARAM_2):
#    comando_1
#    comando_2
#    comando_3
#    return VALOR_RETORNO

# VARIAÇÕES
# SEM parâmetros e SEM retorno

# def NOME_FUNCAO():
#    comando_1
#    comando_2
#    comando_3

# COM parâmetros e SEM retorno

# def NOME_FUNCAO(PARAM_1, PARAM_2):
#     comando_1
#     comando_2
#     comando_3

# SEM parametros e COM retorno

# def NOME_FUNCAO():
#     comando_1
#     comando_2
#     comando_3

#     return VALOR_RETORNO

# EXEMPLO (sem parâmetros e sem retorno):

# def exibir():
#     print("Executando a função exibir()")
#     print("Fim da função exibir()")

# exibir()  # Chamando a função exibir()

# EXEMPLO (com parâmetros e com retorno / definindo mais de uma função em variáveis diferentes)

# def produto(x, y):
#     resultado = x * y
#     return resultado

# def soma(x, y):
#     resultado = x + y
#     return resultado

# multiplicacao = produto(4, 8)  # Chamando a função produto() com os parâmetros x e y
# sum = soma(42, 4)

# print(f"O resultado da multiplicação é: {multiplicacao}")  # Chamando a função produto() com os parâmetros x e y
# print(f"O resultado da soma é: {sum}")  # Chamando a função soma() com os parâmetros x e y

# diferenca = sum - multiplicacao
# print(f"A diferença entre a soma e a multiplicação é: {diferenca}")

# EXEMPLO (Com parâmetro e sem retorno):

# def exibir_frase(nome, altura, linguagem):
#     print(f"Olá, meu nome é {nome}, tenho {altura} de altura e gosto de programar em {linguagem}.")

# exibir_frase("Camila", 1.76, "Python")

