a = 10
b = 2.55

# Python tem um problema de precisão com números decimais. Por isso, o resultado pode não ser exatamente o esperado. Para resolver esse problema, podemos usar a função round() para arredondar o resultado.

resultado = a + b
print(resultado)
print(round(a + b, 2))  # Arredonda o resultado para 2 casas decimais.

# Ao somar um número inteiro com um número decimal, o resultado será um número decimal. tipo float.