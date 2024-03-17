import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def busca_binaria(chave, lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

def gerar_sequencia(tamanho):
    return [random.randint(1, tamanho * 10) for _ in range(tamanho)]

def gerar_chaves(qtd, tamanho):
    return [random.randint(1, tamanho * 10) for _ in range(qtd)]

def experimentar(busca, sequencia, chaves):
    tempos = []
    for chave in chaves:
        inicio = time.time()
        busca(chave, sequencia)
        fim = time.time()
        tempos.append(fim - inicio)
    return sum(tempos) / len(tempos)

tamanhos_sequencia = [10**4, 10**5, 10**6, 10**7]
qtd_chaves = [10**2, 10**3, 10**4, 10**5]

resultados_binaria = []

for tamanho in tamanhos_sequencia:
    sequencia = gerar_sequencia(tamanho)
    sequencia = merge_sort(sequencia)  # Ordena a sequência com Merge Sort
    
    chaves = gerar_chaves(max(qtd_chaves), tamanho)
    
    tempos = []
    for qtd in qtd_chaves:
        tempo_binaria = experimentar(busca_binaria, sequencia, chaves[:qtd])
        tempos.append(tempo_binaria)
    resultados_binaria.append(tempos)

print("Resultados da Busca Binária:")
for i in range(len(tamanhos_sequencia)):
    print(f"Tamanho da Sequência: {tamanhos_sequencia[i]}")
    for j in range(len(qtd_chaves)):
        print(f"Número de Consultas: {qtd_chaves[j]} - Tempo Médio: {resultados_binaria[i][j]} segundos")
    print("\n")
