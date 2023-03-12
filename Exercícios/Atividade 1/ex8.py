""""
Faça um Programa que peça 2 números inteiros e um número
real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo.
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.

"""
n1 = int(input("Digite o primeiro número inteiro "))
n2 = int(input("Digite o segundo número inteiro "))
r1 = float(input("Digite um número real "))

prod = (2 * n1) * (n2 /2)
soma = (3 * n1) + r1
cubo = r1 **3

print(f"O produto do dobro do primeiro com metade do segundo é {prod}")
print(f"A soma do triplo do primeiro com o terceiro é {soma}")
print(f"O terceiro elevado ao cubo é {cubo}")


#%%
