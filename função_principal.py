from função_jogo import *
from função_resultado import *

with open ('perguntas.json', 'r', encoding="utf-8") as perguntas:
    lista = json.load(perguntas)

# EU NÃO CONSEGUI COLOCAR PARA AS ALTERAÇÕES SEREM EM TEMPO REAL
# PARA DA CERTO PRECISA SAIR DO JOGO E INICIAR DE NOVO AI TERÁ 
# ATUALIZADO AS PERGUNTAS E ALTERNATIVAS 

mensagem()
time.sleep(2)
limpar_console()

while True:
    print('''MENU:\033[33m
[1]: JOGAR JOGO DE PERGUNTAS
[2]: ADICIONAR PERGUNTAS
[3]: DELETAR PERGUNTA 
[4]: EDITAR PERGUNTA
[5]: CADASTRAR PONTUAÇÃO
[6]: VER TABELA 
[7]: SAIR DO JOGO\033[0m''') 
    try:  
        opcao = int(input('digite a opção: '))
        if not opcao in [1,2,3,4,5,6,7]:
            print('NÃO EXISTE ESSA OPÇÃO NO MENU')
    except:
        limpar_console()
        print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
    else:
        if opcao == 1:
            while lista:
                numero_sorteado = random.randint(0, len(lista) - 1)
                ler_perguntas(lista, numero_sorteado)
                resultado_final(lista, numero_sorteado)
                try:
                    continuar = int(input('''CONTINUAR JOGANDO:
[1]: SIM
[2]: NAO
Escolha: '''))
                    if not continuar in [1, 2]:
                        print('não existe esse numero no menu')
                        limpar_console()
                except:
                    limpar_console()
                    print('\n\033[31mDIGITE UMA opcao VALIDA\033[0m\n')
                else:
                    if continuar == 2:
                        break
            limpar_console()
            if not lista:
                print('\n\033[31mFIM DO JOGO', end=" ")
                print('VOCÊ RESPONDEU TODAS AS PERGUNTAS\033[0m\n')
            else:
                print('\n\033[31mENCERRANDO O JOGO\033[0m\n') 
                time.sleep(1)
                limpar_console()       
        elif opcao == 2:
            adicionando_pergunta()
        elif opcao == 3:
            listar_pergunta(lista)
            print('\nQUAL DAS PERGUNTAS DESEJA EXCLUIR:')
            try:
                print('aperte ENTER se deseja sair')
                deletando = int(input('resposta: '))
                if not deletando in range(len(lista)):
                    print('você digitou uma opção inexistente')
            except ValueError:
                limpar_console()
                print('saindo da edição com sucesso')
                time.sleep(1)
                limpar_console()
            except:
                limpar_console()
                print('\n\033[31mDIGITE UMA OPÇÃO VALIDA\033[0m\n')
            else:
                deletando_pergunta(deletando)
        elif opcao == 4:
            try:
                menu = int(input('''MENU DE EDIÇÃO: 
[1]: PERGUNTA
[2]: ALTERNATIVAS
sua opcao: '''))
                if not menu in [1, 2]:
                    limpar_console()
                    print('não existe esse numero no menu')
            except:
                limpar_console()
                print('\n\033[31mDIGITE UMA opcao VALIDA\033[0m\n')
            else:
                if menu == 1:
                    print('LISTA:')
                    listar_pergunta(lista)
                    editando_pergunta(lista)
                elif menu == 2:
                    print('''MENU
[1]: TODAS AS ALTERNATIVAS
[2]: SOMENTE UMA''')
                    try:
                        menu_secundario = int(input('escolha: '))
                        if not menu_secundario in [1, 2]:
                            limpar_console()
                            print('não existe esse numero no menu')
                    except:
                        limpar_console()
                        print('\n\033[31mDIGITE UMA opcao VALIDA\033[0m\n')
                    else:
                        if menu_secundario == 1:
                            limpar_console()
                            print('LISTA:')
                            listar_pergunta(lista)
                            editando_alternativas(lista)
                        elif menu_secundario == 2:
                            limpar_console()
                            print('LISTA:')
                            listar_pergunta(lista)
                            editando_uma_Alternativa(lista) 
        elif opcao == 5:
            nome = str(input('digite o seu nome: '))
            resultado = recebendo_pontuação()
            lista = listando_pontuação(nome, sum(resultado))
            salvando_pontuação(lista[0])
        elif opcao == 6:
            tabela_pontuação()
        else:
            print('ate mais, volte sempre...')
            break 



#quando de um erro de diretorio, coloco em workspace da subpasta