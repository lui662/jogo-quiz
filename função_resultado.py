import json
lista_pontuação = []
#-----------------------------------------------------------------------------------------------------------
#CRIANDO A LISTA DE DICIONARIO
def listando_pontuação(nome, pontuação):
    dicionario = {"nome":nome, "pontuação":pontuação}
    lista_pontuação.append(dicionario)
    return lista_pontuação
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#ADICIONANDO AO ARQUIVO JSON
def salvando_pontuação(dicionario):
    with open ('pontuacao.json', 'r', encoding="utf-8") as documento:
        arq = json.load(documento)
        arq.append(dicionario)
    with open ('pontuacao.json', 'w', encoding="utf-8") as pontuação:
        json.dump(arq, pontuação, indent=2, ensure_ascii=False)

#-----------------------------------------------------------------------------------------------------------
#TABELA DE PONTUAÇÃO
def tabela_pontuação():
    with open ('pontuacao.json', 'r', encoding="utf-8") as pontos:
        pontuação_lista = json.load(pontos)
    pontuação_lista.sort(key=lambda x: x["pontuação"], reverse=True)
    print('-'*30)
    print('TABELA DE PONTUAÇÃO'.center(30))
    print('-'*30)
    print(f'\033[32m{"NOME"}\t\t{"PONTUAÇÃO":>14}\033[0m')
    for valor in pontuação_lista:
        print(f'{valor["nome"].upper():<10}\t{valor["pontuação"]:>12}PT')
    print('-'*30)
#-----------------------------------------------------------------------------------------------------------
#pontuação_lista.sort(key=lambda x: x["pontuação"], reverse=True)
#preciso aprender a usar melhor a função lambda, esse pequeno trexo
#foi pesquisando como fazia 