""""
Usando o que foi visto em sala, crie uma estrutura que
pergunte ao usuário qual o dia da semana. Se o dia for
igual a domingo ou igual a sábado, imprima na tela
"Hoje é dia de descanso", caso contrário imprima na
tela "Você precisa trabalhar!"

"""

dia = input("Qual o dia da semana?")
diasDesejados = ["Sábado", "Sabado", "sabado", "sábado", "Domingo", "domingo"]

if dia in diasDesejados:
    print("Hoje é dia de descanso")

else:
    print("Você precisa trabalhar!")
#%%
