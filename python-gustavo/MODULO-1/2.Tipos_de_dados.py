# TIPOS DE DADOS

# str: dados textuais (strings)
# int: números inteiros (sem parte decimal)
# float: números decimais (com parte decimal, ponto)
# bool: valores lógicos (verdadeiro e falso)

# --------------------------------------------------------------------------

# STRING: Pode-se usar aspas duplas ou simples para definir strings em Python

meu_texto = "Minha palavra"
# meu_texto_simples = 'Minha palavra simples'

print(meu_texto)
# print(meu_texto_simples)

# type : serve para verificar/validar o tipo de dado de uma variável
print(type(meu_texto))

# --------------------------------------------------------------------------

# INTEIROS são números que não contenham nenhuma casa decimal é um tipo de dado inteiro em Python.

variavel_int = 100
print(variavel_int)
print(type(variavel_int))  # Type mostra o tipo da variável

# --------------------------------------------------------------------------

# FLOAT é um tipo de dado numérico que representa números reais, ou seja, números com parte decimal.
# em python, os números float são representados com ponto decimal.

print(type(290.56))  # Saída: <class 'float'>

preco = 100.25
print(f"Preço: R$ {preco:.2f}") # Formata o float com 2 casas decimais

# --------------------------------------------------------------------------

# TIPO BOLEANO
# é um tipo de dado que pode assumir apenas dois valores: True (verdadeiro) ou False (falso).
# Em python SEMPRE o True e False começam com letra maiúscula.

# esta_chovendo = False
# luz_esta_acessa = True
# print(esta_chovendo)
# print(luz_esta_acessa)
# print(type(esta_chovendo))
# print(type(luz_esta_acessa))

# Classe (type) em python: é como um modelo que vai definir regras, padrões e 
# comportamentos para criar objetos.

# print(type(esta_chovendo))
# print(type(luz_esta_acessa))

valor_inteiro = 100
valor_textal = 'Minha String'
valor_float = 23.42

print(type(valor_inteiro))
print(type(valor_textal))
print(type(valor_float))