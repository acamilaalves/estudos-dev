# CONJUNTOS: elementos não ordenados (sem posição) e não podem  se repetir, ele vai remover as duplicatas e só vai
# mostrar os elementos uma única vez. São representados por chaves {}.

# conjunto = {10, 8, 2, 3, 8, 10, 3}
# print(f"Tipo do conjunto: {type(conjunto)}")

# print(conjunto) 

a = {1, 2, 3}
b = {3, 2, 4, 5}

print (a | b) # união
print (a & b) # interseção
print (a - b) # diferença