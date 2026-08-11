# Exercício 1 - Operadores Aritméticos

# Crie duas variaveis, com valores inteiros.

# Faça com essas variáveis todas as operações aritméticas (adição, subtração, multiplicação, divisão, módulo, exponenciação e divisão inteira) mostradas na aula. Armazene o resultado de cada operação variável separada e utilize strings para imprimir cada resultado no seguinte modelo:
# (exemplo para soma)

# "Resultado da soma: 10"

# a = 20
# b = 5

# resultado = a + b
# print("Resultado da operação:", resultado)
# resultado = a - b
# print("Resultado da operação:", resultado)
# resultado = a * b
# print("Resultado da operação:", resultado)
# resultado = a / b
# print("Resultado da operação:", resultado)
# resultado = a ** b
# print("Resultado da operação:", resultado)
# resultado = a // b
# print("Resultado da operação:", resultado)
# resultado = a % b
# print("Resultado da operação:", resultado)


# Exercício 2 - Trabalhando com números decimais

# Crie duas variáveis, uma contendo um valor com três casas decimais e outra contendo um valor decimal com duas
# casas decimais.

# Multiplique essas duas variáveis e apresente o resultdo contendo apenas duas casas decimais.

# valor1 = 5.678
# valor2 = 2.34

# resultado = valor1 * valor2
# resultado_formatado = valor1 * valor2
# print(f"Resultado antes da formatação: {resultado}")
# print(f"Resultado da multiplicação: {resultado:.2f}")

# Exercício 3 - Operadores Relacionais

# Crie duas variáveis inteiras. Faça todas as operações relacionais apresentadas na aula, exibindo o resultado de cada comparação.

# a = 15
# b = 20

# print("a é igual b? :", a == b)
# print("a é diferente de b? :", a != b)
# print("a é maior que b? :", a > b)
# print("a é menor que b? :", a < b)
# print("a é maior ou igual a b? :", a >= b)
# print("a é menor ou igual a b? :", a <= b)


# Exercício 4 - Vou conseguir viajar?

# Pense na seguinte situação: ano que vem, eu quero viajar. Mas, eu só consigo viajar se eu estiver de férias do
# trabalho e tiver conseguido comprar as passagens.

# Não consegui as férias no trabalho, mas consegui comprar as passagens.

# Se eu fosse utilizar variáveis booleanas do python e um operador lógico para montar um código para
# exibir se desse jeito eu vou ou não conseguir viajar, como esse código ficaria?

# férias = False
# passagens = True
# vou_viajar = férias and passagens
# print("Vou conseguir viajar? :", vou_viajar)

# Exercício 5 - Pode entrar no evento?

# Eu só posso participar de um evento na minha cidade se eu tiver um convite ou então, se meu nome estiver na lista de entrada.

# Meu nome não está na lista, mas eu tenho um convite.

# Se eu fosse utilizar variáveis booleanas do python e um operador lógico para montar um código para exibir se desse jeito eu vou ou não conseguir participar do evento, como esse código ficaria?

convite = True
nome_na_lista = False

pode_entrar = convite or nome_na_lista
print("Posso entrar no evento?", pode_entrar)