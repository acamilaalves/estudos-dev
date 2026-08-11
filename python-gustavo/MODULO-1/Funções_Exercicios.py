# EXERCICIO 1: 
# O código abaixo repete o mesmo cálculo várias vezes.

# Refatore-o, criando uma função que leia as notas dos alunos, calcule a média, retorne-a arredondada com
# uma casa decimal e evite a repetição.

# print("Aluno 1")
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# media = round(media, 1)
# print(f"A média do aluno 1 é: {media}")

# print("Aluno 2")
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# media = round(media, 1)
# print(f"A média do aluno 2 é: {media}")

# print("Aluno 3")
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# media = round(media, 1)
# print(f"A média do aluno 3 é: {media}")

# def calcular_media(aluno_numero):
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
#     nota3 = float(input("Digite a terceira nota: "))

#     media = (nota1 + nota2 + nota3) / 3
#     media = round(media, 1)

#     print(f"A média do aluno {aluno_numero} é: {media}")

# calcular_media(1)
# calcular_media(2)
# calcular_media(3)

# EXERCICIO 2:
# Crie uma função chamada calcular_velocidade_media que receba a distancia percorrida (em km) e o
# tempo gasto para o deslocamento (horas).

# A função deve calcular a velocidade média e devolvê-la arredondada com duas casas decimais.

# def calcular_velocidade_media(distancia, tempo): # Minha Resposta
#     velocidade_media = distancia / tempo
#     return round(velocidade_media, 2)

# calculada_velocidade = calcular_velocidade_media(150, 2.5)
# print(f"A velocidade média é: {calculada_velocidade} km/h")

# RESPOSTA DO PROFESSOR:
# def calcular_velocidade_media(distancia, tempo):
#     resultado = distancia / tempo
#     return round(resultado, 2)

#     return resultado

# dist = int(input("Digite a distância percorrida (em km): "))
# tempo = float(input("Digite o tempo gasto (em horas): "))

# vel_media = calcular_velocidade_media(dist, tempo)

# print(f"A velocidade média é: {vel_media} km/h")

# EXERCICIO 3:
# Crie uma função chamada notas_aprovadas que receba uma lista de notas (lista de floats)
# e retorne uma lista apenas com as notas maiores ou iguais a sete.

def notas_aprovadas(lista_notas):
    lista_aprovadas = []
    for nota in lista_notas:
        if nota >= 7:
            lista_aprovadas.append(nota)
    return lista_aprovadas

lista_notas_alunos = [10.0, 4.5, 7.5, 9.0]
lista_resultante = notas_aprovadas(lista_notas_alunos)

print(f"As notas aprovadas são: {lista_resultante}")
