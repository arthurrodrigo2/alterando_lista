# lista de nomes
nomes = ["Arthur", "Jeane", "Rodrigo", "Jhenifer", "Santana", "Sousa", "Shirley", "Patrícia"]

# Exibir a lista original
for i in range(len(nomes)):
    print(f"índice {i}: {nomes[i]}")

# usuário deve informa o índice que deseja alterar
try:
    indice = int(input("Informe o indice do nome que deseja alterar: "))
    confirmacao = input(f"Deseja alterar o nome {nomes[indice]}? Digite 'sim' para confirmar.")

    if confirmacao == "sim":
        novo_nome = input("Informe o novo nome: ")
        nomes[indice] = novo_nome
    else:
        ...
except Exception as e:
    print(f"Não foi possível alterar o nome. {e}")
finally:
    # nova lista
    for i in range(len(nomes)):
        print(f"Índice {i}: {nomes[i]}.")