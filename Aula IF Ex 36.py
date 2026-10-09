media=float(input("digite sua média:"))
frequencia=int(input("digite sua frequência:"))
if media >= 7 and frequencia >= 75:
    print("aprovado")
else:   
    if media <= 7 and frequencia >= 75:
        print("reprovado por nota")
    else:
        print("reprovado por frequência")
