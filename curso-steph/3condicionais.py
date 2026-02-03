# CONDICIONAIS

# São estruturas que permitem ao nosso programa tomar decisões com base em determinadas condições.
# em outras palavras, o programa pode executar ações diferentes dependendo de uma situação específica.

# Exemplo:

# Você está em uma cafeteria e está com pouca grana.
# O Cappucino custa 10 reais, café com leite 7 e o café simples 4.

# Se você tiver 10 reais ou mais na carteira, você pode comprar o Cappucino.
# Se tiver entre 7 reais ou mais, pode comprar o café com leite.
# Se não, pede o café simples.

# Sintaxe básica no Python:

# if - "Se"
# else - "Se não"
# elif - Se + se não

# if condição:
    # Código a ser executado se a condição for verdadeira
# elif outra_condição:
    # Código executado se a primeira condição for falsa, mas essa for verdadeira
# else:
    # Código executado se nenhuma das condições anteriores for verdadeira


# Exemplo prático:

# Verificando a idade para entrar em uma festa (18 anos)

# idade = int(input("Digite sua idade: "))    # Usuário insere a idade

# if idade >= 18:                            # Se a idade for maior ou igual a 18
   # print("Você pode entrar na festa!")     # Permite a entrada
# else:                                     # Se a idade for menor que 18
  #  print("Desculpe você não tem idade para entrar na festa.")  # Nega a entrada

# Exemplo com múltiplas condições:

# Verificando a nota de um aluno

nota = float(input("Digite sua nota: "))  # Usuário insere a nota

if nota >= 7.0:                               # Se a nota for maior ou igual a 7.0
    print("Parabéns! você está Aprovado!")    # Aluno aprovado
elif nota >= 5.0:                                                           # Se a nota for menor que 7.0 mas maior ou igual a 5.0
    print("Você está de Recuperação. Estudo mais e tente novamente")        # Aluno em recuperação
else:                                                # Se a nota for menor que 5.0
    print("Infelizmente você está Reprovado.")       # Aluno reprovado
    