# EXCEÇÃO é um tipo de erro que pode acontecer durante
# execução do nosso código, ou seja quando ele já está sendo executado pelo interpretador do Python.

# Quando uma exceção ocorre, se ela não for tratada por nós, o interpretador do python
# vai interromper a execução do nosso código, exibir uma mensagem mostrando a exceção que ocorreu,
# e em que parte do código ela ocorreu.

#--------------------------------------------------

# DIVISÃO POR ZERO (EXCEÇÕES SEM TRATAMENTO)

# Estamos pedindo um número ao usuário e vamos dividir 100 por esse número lido.
# Caso o número lido seja zero, isso vai desencadear um erro.

# numero = int(input("Digite um número: "))

# Se o número lido foi zero, ocorrerá uma exceção ZeroDivisionError, e o interpretador do Python vai interromper
# a execução do código.

# resultado = 100 / numero
# print(f"O resultado da divisão é: {resultado}")

# ----------------------------------------------------------

# CONVERSÃO STRING NÃO NÚMERICA (EXCEÇÕES SEM TRATAMENTO)

# Exemplo: Estamos pedindo um número ao usuário. Como a função input() sempre retorna o que foi lido na
# forma de uma string, é necessário converter para o tipo int.

# Caso a string lida não represente um número, ocorrerá uma exceção ValueError, e o interpretador do Python
# vai interromper a execução do código.

# numero = int(input("Digite um número: "))

# print(f"O número digitado foi: {numero}")

# --------------------------------------------

# INDICE FORA LISTA (EXCEÇÕES SEM TRATAMENTO)

# Exemplo: Temos uma lista de quatro elementos.Estamos pedindo ao usuário um número de uma posição na lista
# para acessarmos.

# lista = [10, 20, 30, 40]
# posicao = int(input("Qual posição da lista você quer acessar? "))

# Se a posição lida estiver "fora dos limites"  da lista, ocorrerá uma exceção IndexError,
# e o interpretador do Python vai interromper a execução do código.

# print(f"O elemento na posição {posicao} é: {lista[posicao]}")

# ----------------------------------------------------------

# FOR (EXCESSÃO SEM TRATAMENTO)

# Exemplo: Temos uma lista de cinco divisores.

lista_divisores = [3, 6, 0, 9, 12]

# Com uma estrutura de repetição for, vamos percorrer a nossa lista e dividir 36 por cada um dos divisores.

for item in lista_divisores:
    # Quando o divisor for zero, ocorrerá uma exceção DivisionByZeroError, e o interpretador do 
    # Python vai interromper a execução do código. Nosso programa não continuará as próximas interações
    # (rodadas) do for quando isso acontecer.
    resultado_divisao = 36 / item
    print(f"36 dividido por {item} = {resultado_divisao}")