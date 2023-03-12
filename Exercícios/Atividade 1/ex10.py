"""
Faça um programa que peça o tamanho de um arquivo para
download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).

1 MB = 8 Mb
"""

tamArq = float(input("Digite o tamanho do arquivo em MB"))
velInt = float(input("Digite a velocidade da internet em Mbps"))

tempoDownload = (tamArq / (velInt / 8)) / 60

print(f"O tempo aproximad  o de download é de {tempoDownload} minutos")
#%%
