# _________________________________IMPORTANDO BIBLIOTECAS_________________________________
import random
import os
from playsound import playsound
from utilidades import apresentar_programa, azul,verde
# _________________________________LISTAS_________________________________
nomes = ['Julio', 'Guerra', 'Martins', 'Joao', 'Oliveira']
emails = ['juliojvjago@gmail.com', 'julio.guerra.dev@gmail.com', 'xxxx@gmailcom', 'aleatorio_com_cafe@gmail.com', 'ultimo_email_aleatorio@gmail.com']
telefones = [123456789, 234567891, 345678912, 456789123, 567891234]
cidades = ['Plano piloto', 'Sobradinho I', 'Cruzeiro', 'Sao Sebastião', 'Samambaia']
estados = ['Sao Paulo', 'Brasilia-DF', 'Minas Gerais', 'Lima']
#_________________________________Funções_________________________________
def tracejado():
    verde('-' * 30)
def novo_doc_1_2():
    with open('dados_gerados.txt','a') as arquivo:
            arquivo.write('\n' + str(random.choice(nomes)) + '\n' + str((random.choice(emails))))
            print((random.choice(nomes)))
            print((random.choice(emails)))
def novo_doc_1_2_3():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(nomes)) + '\n' +  str((random.choice(emails))) + '\n' +  str((random.choice(telefones))))
        print((random.choice(nomes)))
        print(((random.choice(emails))))
        print((random.choice(telefones)))
def novo_doc_1_2_3_4():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(nomes)) + '\n' +  str((random.choice(emails))) + '\n' +  str((random.choice(telefones))) + '\n' +  str((random.choice(cidades))))
        print((random.choice(nomes)))
        print((random.choice(emails)))
        print(((random.choice(telefones))))
        print((random.choice(cidades)))
def novo_doc_1_2_3_4_5():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(nomes)) + '\n' + str(random.choice(emails)) + '\n' +  str((random.choice(telefones))) + '\n' + str((random.choice(cidades))) + '\n' +  str((random.choice(estados))))
        print((random.choice(nomes)))
        print((random.choice(emails)))
        print(((random.choice(telefones))))
        print(((random.choice(cidades))))
        print(((random.choice(estados))))
def doc_unico_1():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(nomes)))
        print(random.choice(nomes))
def doc_unico_2():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(emails)))
def doc_unico_3():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(telefones)))
def doc_unico_4():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(cidades)))
def doc_unico_5():
    with open('dados_gerados.txt','a') as arquivo:
        arquivo.write('\n' + str(random.choice(estados)))
#_________________________________Loop_________________________________
playsound('teste.wav',block=False)
while True:
    apresentar_programa()
    print('ao Gerador de Dados de Testes - \u001b[31mPara finalizar o programa, digite "parar"\u001b[0m')
    tracejado()
    azul('[1] - Nomes')
    azul('[2] - E-mail''s')
    azul('[3] - telefones')
    azul('[4] - Cidades')
    azul('[5] - Estados')
    opcao = input('\u001b[34mDigite uma(as) das opções: \u001b[0m')
    tracejado()
    if opcao == "parar":
        exit()
    else:
        # _________________________________Dar opção para salvar em arquivos .txt_________________________________
        salvar = input('\u001b[34mGostaria de salvar os dados em um arquivo de texto?(s/n) \u001b[0m')
    if salvar =="s":
        if opcao == "1":
            doc_unico_1()
        elif opcao == "1,2":
            novo_doc_1_2()
        elif opcao == "1,2,3":
            novo_doc_1_2_3()
        elif opcao == "1,2,3,4":
            novo_doc_1_2_3_4()
        elif opcao == "1,2,3,4,5":
            novo_doc_1_2_3_4_5()
        elif opcao == "2":
            doc_unico_2()
        elif opcao == "3":
            doc_unico_3()
        elif opcao == "4":
            doc_unico_4()
        elif opcao == "5":
                doc_unico_5()
    elif salvar == "parar":
            exit()  
    else:
        if opcao == "1":
            print(random.choice(nomes))
        elif opcao == "1,2":
            print(random.choice(nomes))
            print(random.choice(emails))
        elif opcao == "1,2,3":
            print(random.choice(nomes))
            print(random.choice(emails))
            print(random.choice(telefones))
        elif opcao == "1,2,3,4":
            print(random.choice(nomes))
            print(random.choice(emails))
            print(random.choice(telefones))
            print(random.choice(cidades))
        elif opcao == "1,2,3,4,5":
            print(random.choice(nomes))
            print(random.choice(emails))
            print(random.choice(telefones))
            print(random.choice(cidades))
            print(random.choice(estados))
        elif opcao == "2":
            print(random.choice(emails))
        elif opcao == "3":
            print(random.choice(telefones))
        elif opcao == "4":
            print(random.choice(cidades))
        elif opcao == "5":
            print(random.choice(estados))