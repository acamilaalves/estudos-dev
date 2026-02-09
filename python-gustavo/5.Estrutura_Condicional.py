# ESTRUTURAS CONDICIONAIS: IF, ELIF, ELSE

# IF: "Se" a condição for verdadeira, o bloco de código dentro do IF será executado.

# ELIF: "Senão se" se a condição do IF for falsa, o programa irá verificar a condição do ELIF, se for verdadeira, o bloco de código dentro do ELIF será executado. O ELIF é opcional e pode ser usado quantas vezes forem necessárias.

# ELSE: "Senão" se a condição for falsa, o bloco de código dentro do ELSE será executado.

# CONDIÇÃO: Qualquer operação que utilizando operadores lógicos e/ou relacionais, resulte em verdadeiro (True) ou (False) falso.

# if CONDICAO:
#     comando_1
#     comando_2
# elif CONDIÇÃO_2:
#     comando_3
#     comando_4
# else:
#     comando_se_nao


# Exemplo 1:

# idade = int(input("Digite sua idade: ")) # A função input() sempre é para trabalhar dados de entrada do usuário.

# if idade >= 18:
#     print("Já pode tirar a CNH.")
#     print("Dirija com cuidado!")
# else:
#     print("Ainda não pode tirar a CNH.")
#     print("Volte quando estiver com 18 anos!")

# print("Fim do programa.")

# Exemplo 2:

media = float(input("Média do aluno: "))

if media >= 7.0: # IF é obrigatório, e deve ser o primeiro bloco de código.
    print("Aluno aprovado. Passou direto!")
elif (media >= 4.9) and (media < 7.0): # ELIF é opcional, mas pode ser usado "quantas vezes" forem necessárias.
    print("Aluno em recuperação. Estude mais!")

    nota_rec = float(input("Nota da recuperação: "))

    if nota_rec >= 7.0:
        print("Passou na recuperação.")
    else:
        print("Reprovou na recuperação.")        
else: # Else é opcional, mas só pode ser usado uma vez, e deve ser o último bloco de código.
    print("Aluno reprovado. Estude mais e tente novamente!")
