# Laços de Repetição (for e while)

# Imagine que você precisa pedir para alguém contar de 1 a 100
# e escrever cada número em um papel. Fazer isso manualmente seria muito cansativo e demorado, ne?

# Agora, imagine que um programa pode fazer essa contagem automaticamente,
# sem precisar repetir o mesmo comando 100 vezes. É exatamente isso que os laços de repetição fazem!

# Os laços de repetição são usados para executar um bloco de código várias vezes,
# até que uma determinada condição seja atendida/atingida.

# Python oferece dois tipos principais de laços de repetição:

# for - Quando sabemos quantas vezes queremos repetir algo.
# while - Quando queremos repetir algo até que uma condição se torne falsa.

# FOR 
# é usado quando sabemos quantas vezes queremos repetir um bloco de código.
# ele percorre uma sequência de valores, como uma lista, um intervalo de números ou até mesmo letras de uma palavra.

# Estrutura:

# for variavel in sequencia:
    # Código a ser repetido 

# Contando de 1 a 5 com o FOR:
# [1,2,3,4,5]

# for numero in range(1, 6):  
#    print(numero)            

    # O range (1, 6) gera números de 1 a 5 (o ultimo número do range "6" não é incluído).

# PERCORRENDO UMA LISTA DE COMPRAS (NOMES)

# compras = ["Arroz", "Feijão", "Leite", "Ovos"]

# for item in compras:
#    print(f"📍 Comprar: {item}")

# PERCORRENDO AS LETRAS DE UMA PALAVRA

# Palavra = "COMUNIDADE"

# for letra in Palavra:
#     print(letra)

# WHILE
# é usado quando não sabemos exatamente quantas vezes a repetição vai acontecenr, mas sabemos a condição que
# deve ser atendida para continuar.

# While condição:
    # Código a ser repetido enquanto a condição for verdadeira

# Obs: Cuidado para não criar um loop infinito, ou seja, uma repetição que nunca termina.
# Se a condição nunca se tornar falsa, o código nunca para de rodar.

# contagem regressiva

#contador = 5

#while contador > 0:          # Enquanto o contador for maior que 0 preciso continuar contando
#    print(contador)         
#    contador -= 1            # diminui 1 do contador a cada repetição
#    contador = contador - 1  #  mesma coisa que a linha acima só que abreviado
#print("Fogo!")               

# PEDINDO UMA SENHA ATÉ ACERTAR

# senha_correta = "1234"
# senha = ""

# while senha != senha_correta:          # Enquanto a senha for diferente da correta
#     senha = input("Digite a senha: ")   # Pede para o usuário digitar a senha

# print("Acesso permitido!")            # Quando a senha estiver correta, sai do loop e mostra a mensagem

