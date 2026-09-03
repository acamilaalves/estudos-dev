#EXEMPLO CONTINUE FOR

for item in range(1, 11):
    if item == 5:
        print("Item 5 encontrado, vou pular o resto do laço.")
        continue
    
    print("Passou pelo item", item)
    print("Avançando para a próxima rodada...")

print("Fim do For.")

#EXEMPLO CONTINUE WHILE

while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        break

    if numero < 0:
        print("Número negativo ignorado. Vou pular o resto do laço.")
        continue

    print("Você digitou:", numero)

print("Loop encerrado")