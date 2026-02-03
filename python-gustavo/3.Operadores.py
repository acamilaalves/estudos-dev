# OPERADORES DE PYTHON

# Aritméticos - Usados para fazer calculos matemáticos
# Relacionais - Usados para comparar valores
# Lógicos - Usados para combinar condições, normalmente booleanas.

# ------------------------------------------------------------------------

# ARITMÉTICOS

x = 10
y = 3

print(10 + 3)
print(x + 3)

print(x + y)  # Soma
print(x - y)  # Subtração
print(x * y)  # Multiplicação
print(x / y)  # Divisão

print(x ** y) # Exponenciação
print(x // y) # Divisão inteira
print(x % y)  # Módulo (resto da divisão) (quando quero saber se o núero é par ou ímpar. Se o resultado for 0, é par. Se for 1, é ímpar.)

# DECIMAIS

a = 10
b = 2.55

# Python tem um problema de precisão com números decimais. Por isso, o resultado pode não ser exatamente o esperado. Para resolver esse problema, podemos usar a função round() para arredondar o resultado.

resultado = a + b
print(resultado)
print(round(a + b, 2))  # Arredonda o resultado para 2 casas decimais.

# Ao somar um número inteiro com um número decimal, o resultado será um número decimal. tipo float.

# -----------------------------------------------------------------------------

# RELACIONAIS

a = 10
b = 11

# a = 10       # Atribuição de valor (estou dizendo que o valor de a é igual a 10)
print(a == b)  # Comparação de igualdade
print(a != b)  # Comparação de desigualdade
print(a > b)   # Maior que
print(a < b)   # Menor que
print(a >= b)  # Maior ou igual a
print(a <= b)  # Menor ou igual a

# -----------------------------------------------------------------------------

# LOGICOS

a = True
b = True

print(a and b)  # E lógico (todos os valores envolvidos devem ser True. Ex: a = True e b = True => a and b = True)
print(a or b)   # OU lógico (pelo menos um dos valores envolvidos deve ser True. Ex: a = True ou b = False => a or b = True)
print(not a)    # Negação lógica (inverte o valor lógico. Ex: a = True => not a = False)
