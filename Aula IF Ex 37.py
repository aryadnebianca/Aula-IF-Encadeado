valor_da_compra=float(input("digite o valor:"))
if valor_da_compra >= 200:
    vip=input("cliente vip?")
    if vip == "sim":
        print("desconto vip")
    else:
        print("desconto comum")
else:
    print("sem desconto")
