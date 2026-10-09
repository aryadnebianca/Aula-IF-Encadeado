matricula=input("você está matriculado?:")
if matricula == "sim":
    autorizacao=input("possui autorização?:")
    if autorizacao == "sim":
        print("acesso permitido")
    else:
        print("autorização necessária")
else:
    print("acesso negado")