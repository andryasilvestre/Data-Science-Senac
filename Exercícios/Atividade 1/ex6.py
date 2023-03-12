# Faça um Programa que converta metros para centímetros.

metro = float(input("Digite a quantidade de metro(s) "))
centimetro = metro * 100

if (metro == 1):
    print(f"{metro} metro tem {centimetro} centímetros")
else:
    print(f"{metro} metros têm {centimetro} centímetros")
