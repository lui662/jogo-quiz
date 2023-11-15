import json 
import random
import time
import os
pontos = []

#-----------------------------------------------------------------------------------------------------------
#LIMPAR O CONSOLE
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#LAYOUT
def mensagem():
    print(' ____________________________________________________')
    print('|                                                    |')
    print('| Olá a todos sejam muito bem vido ao jogo espero    |')
    print('| que se divirta, mas antes vamos as regras:         |')
    print('| \033[31m1º cada acerto valerá 10 pontos \033[0m                   |')
    print('| \033[31m2º cada erro valerá 00 pontos \033[0m                     |')
    print('| \033[31m3º ao final do jogo você cadastrara a sua\033[0m          |')
    print('| \033[31mpontuação e seu nome\033[0m                               |')
    print('| \033[31m4º o jogo sorteia perguntas e alternativas\033[0m         |')
    print('| \033[31m5º ao final do jogo você poderar ver sua pontuação \033[0m|')
    print('| \033[31mCLARO SE VOCÊ CADASTROU ELA NO SISTEMA \033[0m            |')
    print('|             DESEJO A TODOS UM BOM JOGO             |')
    print('|____________________________________________________|')
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#ENVIANDO O RESULTADO PARA O USUARIO:
def resultado_final(lista, numero_sorteado):
    limpar_console()
    print('-='*30)
    global pontos
    pontuação = 0
    ler_perguntas(lista, numero_sorteado)
    try:
        escolha = int(input('escolha alternativa correta (1, 2, 3, 4): '))
        if not escolha in [1, 2, 3, 4]:
            limpar_console()
            print('você digitou uma opção inexistente'.upper())
            print('1 chance'.upper())
            print('-='*30)
            ler_perguntas(lista, numero_sorteado)
            escolha = int(input('escolha alternativa correta (1, 2, 3, 4): '))
            if not escolha in [1, 2, 3, 4]:
                limpar_console()
                print(f'desperdicou sua chance\nfim do jogo'.upper())
                return
    except:
        limpar_console()
        print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
    else:
        print('-='*30)
        time.sleep(1)
        lista_sorteada = [lista[numero_sorteado]]
        for indice, valor in enumerate(lista_sorteada):
            if valor["resposta_correta"] == valor["alternativas"][escolha-1]:
                print('-'*30)
                print('RESULTADO'.center(30))
                print('-'*30) 
                print(f'RESULTADO:\t\033[32mCORRETA\033[0m')
                print(f'PONTUAÇÃO:\t10pt')
                print(f'RESPOSTA:\t{valor["resposta_correta"].upper()}')
                print('-'*30)
                pontuação += 10
            else: 
                print('-'*30)
                print('RESULTADO'.center(30))
                print('-'*30) 
                print(f'RESULTADO:\t\033[31mERRADA\033[0m')
                print(f'PONTUAÇÃO:\t00pt')
                print(f'RESPOSTA:\t{valor["resposta_correta"].upper()}')
                print('-'*30)
    lista.pop(numero_sorteado)
    pontos.append(pontuação)
    print('-='*30)
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------       
#ADICIONANDO PERGUNTAS AO ARQUIVO JSON:
def adicionando_pergunta():
    alternativas = []
    print('CADASTRANDO PERGUNTA')
    try:
        print('aperte ENTER se deseja sair')
        quantidade = int(input('quantidade de alternativa:'))
        pergunta = input('cadastre a pergunta: ')
        if not quantidade in [2, 3, 4]:
            print('no minimo 2 alternativas e no maximo 4')
            return
    except ValueError:
        limpar_console()
        print('saindo da edição com sucesso')
        time.sleep(1)
        limpar_console()
    except:
        limpar_console()
        print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
    else:
        for contador in range(quantidade):
            alternativas.append(input(f'{contador + 1}º alternativas: '))
        resposta_correta = input('resposta: ')
        dicionario = {"pergunta":pergunta, "alternativas":alternativas, "resposta_correta":resposta_correta}
        try:
            with open ('perguntas.json', 'r', encoding="utf-8") as adicionar:
                lista = json.load(adicionar)
                lista.append(dicionario)
        except FileNotFoundError:
            lista = []
        with open ('perguntas.json', 'w', encoding="utf-8") as lista_perguntas:
            json.dump(lista, lista_perguntas, indent=2, ensure_ascii=False)   
        print('NOVA PERGUNTA ADICIONADA COM SUCESSO' )   
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#DELETANDO UMA PERGUNTA COMPLETAMENTE DA LISTA
def deletando_pergunta(opções):
    limpar_console()
    with open ('perguntas.json', 'r', encoding="utf-8") as lista_perguntas:
        lista = json.load(lista_perguntas)
        del lista[opções - 1]
    with open ('perguntas.json', 'w', encoding="utf-8") as removido:
        json.dump(lista, removido, indent=2, ensure_ascii=False)
    print('PERGUNTA REMOVIDA COM SUCESSO')
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#EDITANDO A PERGUNTA
def editando_pergunta(lista):
    print('QUAL PERGUNTA DESEJA EDITAR')
    try:
        print('aperte ENTER para sair')
        escolha_numero = int(input('resposta: '))
        sub = escolha_numero - 1
        if not sub in range(len(lista)):
            limpar_console()
            print('você digitou uma opção inexistente')
            return
    except ValueError:
        limpar_console()
        print('saindo da edição com sucesso')
        time.sleep(1)
        limpar_console()
    except:
        print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
        time.sleep(1)
        limpar_console()
    else:
        pergunta = input('nova pergunta: ')
        with open ('perguntas.json', 'r', encoding="utf-8") as arquivos:
            lista = json.load(arquivos)
            lista[sub]["pergunta"] = pergunta
        with open ('perguntas.json', 'w', encoding="utf-8") as documento:
            json.dump(lista, documento, indent=2, ensure_ascii=False)
        print('PERGUNTA EDITADA COM SUCESSO')
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#EDITANDO A ALTERNATIVAS
def editando_alternativas(lista):
    alternativas = []
    print('QUAL ALTERNATIVA DESEJA EDITAR')
    try:
        print('aperte ENTER se deseja sair')
        escolha_numero = int(input('resposta: '))
        sub = escolha_numero - 1
        if not sub in range(len(lista)):
            limpar_console()
            print('você digitou uma opção inexistente')
            return
        limpar_console()
        quantidade = int(input('quantidade de resposta: '))
        if not quantidade in [2, 3, 4]:
            print('no minimo 2 alternativas e no maximo 4'.upper())
            quantidade = int(input('quantidade de resposta: '))
    except ValueError:
        limpar_console()
        print('saindo da edição com sucesso')
        time.sleep(1)
        limpar_console()
    except:
        limpar_console()
        print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
    else:
        for contador in range(quantidade):
            alternativas.append(input(f'{contador + 1}º alternativas: '))
        resposta = input('resposta: ')
        with open ('perguntas.json', 'r', encoding="utf-8") as arquivos:
            lista = json.load(arquivos)
            lista[sub]["alternativas"] = alternativas
            lista[sub]["resposta_correta"] = resposta
        with open ('perguntas.json', 'w', encoding="utf-8") as documento:
            json.dump(lista, documento, indent=2, ensure_ascii=False)
        print('ALTERAÇÃO CONCLUIDA COM SUCESSO')
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#EDITANDO APENAS UMA DAS ALTERNATIVAS
def editando_uma_Alternativa(lista):
    print('QUAL DAS ALTERNATIVA DESEJA EDITAR')
    try:
        print('aperte ENTER se deseja sair')
        escolha_numero = int(input('escolha um numero: '))
        sub = escolha_numero - 1
        if not sub in range(len(lista)):
            limpar_console()
            print('você digitou uma opção inexistente')
            return
    except ValueError:
        limpar_console()
        print('saindo da edição com sucesso')
        time.sleep(1)
        limpar_console()
    except:
        limpar_console()
        print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
    else:
        limpar_console()
        print(f'\033[33m{lista[sub]["pergunta"]}\033[0m')
        print('-='*30)
        resultado = lista[sub]["alternativas"]
        for indice, valor in enumerate(resultado):
            print(f'\033[33m{indice + 1}: {valor}\033[0m')
            print('-='*30)
        indice = int(input('qual alternativa deseja mudar: '))
        valor = input('digite a nova resposta: ')
        resultado[indice - 1] = valor
        resposta = input('resposta: ')
        with open ('perguntas.json', 'r', encoding="utf-8") as arquivos:
            lista = json.load(arquivos)
            lista[sub]["alternativas"] = resultado
            lista[sub]["resposta_correta"] = resposta
        with open ('perguntas.json', 'w', encoding="utf-8") as documento:
            json.dump(lista, documento, indent=2, ensure_ascii=False)  
        print('ALTERAÇÃO CONCLUIDA COM SUCESSO')     
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#LISTANDO AS PERGUNTAS E ALTERNATIVAS 
def listar_pergunta(lista):
    print('-='*30)
    for indice, valor in enumerate(lista):
        print(f'\033[31m{indice + 1}: {valor["pergunta"]}\n   {valor["alternativas"]}\033[0m')
        print('-='*30)    
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#SORTEANDO A PERGUNTA UM SIMPLES PRINT
def ler_perguntas(lista, numero_sorteado):
    print(lista[numero_sorteado]["pergunta"])
    for indice, valor in enumerate(lista[numero_sorteado]["alternativas"]):
        print(f'\033[34m[{indice + 1}]:\033[0m {valor.upper()}')
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#PONTUAÇÃO:
def recebendo_pontuação():
    global pontos
    return pontos
#-----------------------------------------------------------------------------------------------------------