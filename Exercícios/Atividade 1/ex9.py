""""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido

"""

ganhoHr = float(input("Quanto você ganha por hora?"))
horasMes = float(input("Quantas horas você trabalha por mês?"))

salarioTotal = ganhoHr * horasMes
valInss = salarioTotal * 0.08
valIr = salarioTotal * 0.11
valSind = salarioTotal * 0.05
salarioLiquido = salarioTotal - (valSind + valIr + valInss)

print(f"Seu salário total bruto no mês é de R$ {salarioTotal}")
print(f"Você paga {valInss} de INSS")
print(f"Você paga {valIr} de Imposto de Renda")
print(f"Você paga {valSind} ao sindicato")
print(f"Seu salário líquido é de {salarioLiquido}")

#%%
