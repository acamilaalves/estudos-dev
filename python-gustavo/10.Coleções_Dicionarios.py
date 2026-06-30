# DICIONÁRIOS: elementos na forma de pares chave-valor, são representados por chaves {}.
#  A chave é única e o valor pode se repetir.

dicionario = {
    "nome": "Camila",
    "idade": 31,
    "cidade": "Rio de Janeiro",
    "altura": 1.76
    }

print(f"Tipo do dicionário: {type(dicionario)}")
print(dicionario)
print(dicionario["nome"])

print("Dicionário antes da modificação")
print(dicionario)

dicionario["nome"] = "Camila"
dicionario["linguagem"] = "Python"

print("Dicionário depois da modificação")
print(dicionario)

print(dicionario["nome"])
print(dicionario["linguagem"])
