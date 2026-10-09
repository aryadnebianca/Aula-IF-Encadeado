idade=int(input("sua idade:"))
ingresso=input("possui ingresso?")
if idade >= 18:
    if ingresso == "sim":
        print("entrada permitida")
    else:
        print("ingresso necessario")
else:
    print("idade insuficiente")