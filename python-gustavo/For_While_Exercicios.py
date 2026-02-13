# Exercício 1
# Monte um programa que peça, um de cada vez, vários números para o usuário até que ele
# digite zero. Ao fim, mostre a soma de todos esses números que ele digitou.

programa = "Soma de números"
print(programa)
soma = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para sair): "))
print(f"A soma dos números digitados é: {soma}")


# Exercício 2
# Monte um programa que, para um determinado número informado pelo usuário (limite), exiba
# o produtório dos números de 1 até esse limite.

produtorio = 1
limite = int(input("Digite um número limite: "))
for i in range(1, limite + 1):
    produtorio *= i
print(f"O produtório dos números de 1 até {limite} é: {produtorio}")

# Exercício 3
# Monte um programa que, para um determinado número informado pelo usuário (limite), exiba o dobro
# de cada número de 1 até esse limite.

