# Variáveis e tipos de dados "básicos"

# Uma variável é um espaço na memória do computador onde armazenamos um valor.

# <nome da variarvel> = <valor>

# nome = "Camila"  # Variável do tipo String (texto), sempre entre aspas ("" ou '')
#idade = 31       # Variável do tipo Inteiro (número sem casa decimais)
# altura = 1.76    # Variável do tipo Float (número com casa decimais)
# dev = True       # Variável do tipo Booleano (Verdadeiro ou Falso)

nome = input("Digite seu nome: ")  # entrada de texto
idade = int(input("Digite sua idade: "))  # entrada de texto convertido para inteiro
altura = float(input("Digite sua altura: "))  # entrada de texto convertido para float

print(f"Olá, {nome}! Você tem {idade} anos, e mede {altura}m.")
