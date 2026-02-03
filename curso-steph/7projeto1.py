# Jogo de adivinhação

# No jogo, o usuário precisa adivinhar um número secreto. Ele pode tentar várias vezes  até acertar.

print("BEM-VIDOS AO JOGO DO NUMERO SECRETO")
print("-----------------------------------------")

numero_secreto = 5
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar um número de 1 a 10: "))

    if tentativa < numero_secreto:
        print("O número secreto é maior.")
    elif tentativa > numero_secreto:
        print("O número secreto é menor.")
    else:
        print("Parabéns! Você adivinhou o número secreto.")
print("Fim do jogo.")



