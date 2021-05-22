# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
# de download do arquivo usando este link (em minutos).

# Fórmula
print('********** NETWORK CALCULATE **********')
file_size = int(input('Tamanho do arquivo (MB): '))
link_size = int(input('Valocidade de conexão (Mbps): '))

# Taxa de transferência
down_stream = link_size / 8

# Tempo de download
download_time = file_size / down_stream

print(
    f'******* Tempo de download *******\n\n'
    f'Segundos: {download_time}s\n'
    f'Minutos : {download_time / 60: .2f}m'
)