saldo_disponivel=float(input("digite seu saldo:"))
valor_da_compra=float(input("digite o valor:"))
if saldo_disponivel >= valor_da_compra:
    confirmar=input("confirmar?:")
    if confirmar == "sim":
        print("compra realizada")
    else:
        print("compra cancelada")
else:
    print("saldo insuficiente")
