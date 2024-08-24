# João Pedro Cochek Giovannoni
# crie um programa, utilizando alinguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.

def realizar_operacao(codigo, conjunto1, conjunto2):
    if codigo == 'U':
        return conjunto1.union(conjunto2)
    elif codigo == 'I':
        return conjunto1.intersection(conjunto2)
    elif codigo == 'D':
        return conjunto1.difference(conjunto2)
    elif codigo == 'C':
        return {(a, b) for a in conjunto1 for b in conjunto2}
    else:
        raise ValueError(f"Código de operação desconhecido: {codigo}")

def processar_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    numero_operacoes = int(linhas[0].strip())
    linha_atual = 1

    for _ in range(numero_operacoes):
        codigo_operacao = linhas[linha_atual].strip()
        conjunto1 = set(linhas[linha_atual + 1].strip().split(','))
        conjunto2 = set(linhas[linha_atual + 2].strip().split(','))

        resultado = realizar_operacao(codigo_operacao, conjunto1, conjunto2)
        print(f"Resultado da operação {codigo_operacao}: {resultado}")

        linha_atual += 3

# Troque aqui o nome do arquivo que deseja processar, incluindo a extensão .txt. OBRIGADO!.
nome_arquivo = 'operacoes.txt'
processar_arquivo(nome_arquivo)