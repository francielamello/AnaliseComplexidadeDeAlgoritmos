import os

# Obtém o diretório atual do projeto
diretorio_do_projeto = os.getcwd()

# Define o nome do arquivo
nome_arquivo = 'palavras.txt'

# Cria o caminho completo para o arquivo
caminho_arquivo = os.path.join(diretorio_do_projeto, nome_arquivo)

# Agora você pode usar o caminho completo do arquivo em suas operações de leitura/gravação
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    conteudo = file.read()

import os
import time

# Função de busca linear
def linear_search(word, word_list):
    for i, w in enumerate(word_list):
        if w == word:
            return i
    return -1

# Função de busca binária
def binary_search(word, word_list):
    low = 0
    high = len(word_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if word_list[mid] < word:
            low = mid + 1
        elif word_list[mid] > word:
            high = mid - 1
        else:
            return mid
    return -1

# Obtém o diretório atual do projeto
diretorio_do_projeto = os.getcwd()

# Define o nome do arquivo
nome_arquivo = 'palavras.txt'

# Cria o caminho completo para o arquivo
caminho_arquivo = os.path.join(diretorio_do_projeto, nome_arquivo)

# Carregar o conteúdo do arquivo 'palavras.txt' para uma lista
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    words_list = file.read().split()

# Frase para busca
frase = "Não atire o pau no gato Porque isso Não se faz O gatinho É nosso amigo Não devemos maltratar os animais Jamais"
palavras = frase.split()

# Medir o tempo de busca linear
start_time_linear = time.time()
for palavra in palavras:
    linear_search(palavra.lower(), words_list)
end_time_linear = time.time()

# Medir o tempo de busca binária
start_time_binary = time.time()
for palavra in palavras:
    binary_search(palavra.lower(), words_list)
end_time_binary = time.time()

# Calculando os tempos de execução
tempo_execucao_linear = (end_time_linear - start_time_linear)  # Em segundos
tempo_execucao_binaria = (end_time_binary - start_time_binary)  # Em segundos

# Convertendo para milissegundos
tempo_execucao_linear_ms = tempo_execucao_linear * 1000
tempo_execucao_binaria_ms = tempo_execucao_binaria * 1000

# Convertendo para microssegundos
tempo_execucao_linear_micros = tempo_execucao_linear * 1000000
tempo_execucao_binaria_micros = tempo_execucao_binaria * 1000000

# Mostrando os resultados
print("Frase:", frase)
print()
print("Tempo de busca linear:", tempo_execucao_linear, "segundos,", tempo_execucao_linear_ms, "milissegundos,", tempo_execucao_linear_micros, "microssegundos")
print("Tempo de busca binária:", tempo_execucao_binaria, "segundos,", tempo_execucao_binaria_ms, "milissegundos,", tempo_execucao_binaria_micros, "microssegundos")

# Exibir unidade de medida dos tempos avaliados
print("\nUnidade de medida dos tempos avaliados:")
print("segundos (s), milissegundos (ms) e microsegundos (µs)")
