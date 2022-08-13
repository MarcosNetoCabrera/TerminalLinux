import code
import subprocess
import subprocess
import platform
import socket
import time
from datetime import datetime
from datetime import date
import os

path = 'C:\\'
print("Terminal SO")

def logDeComandos(comando):
    try:
        nome_arquivo = 'log.txt'
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(u'Arquivo criado pois nao existia')
    # faca o que quiser
    arquivo.close()

def ls(path):
    try:
        diretorio = []
        diretorio = os.listdir(path)
        for i in diretorio:
            if(os.path.isdir(path+'\\'+i)):
                print ('(dir) '+i)
            else:
                print(i)
    except:
        print('Diretório não encontrado')

def pwd(path):
    print(path)

def cd(path,resto):
    if(os.path.isdir(path+'\\'+resto)==True):
        if (path == 'C:\\'):
            return path+resto
        else:
            return path+'\\'+resto
    else:
        print("Este diretório não existe")
        return path


def Entrada(comando):
    txt = comando
    x = txt.split(' ')
    (a, b) = (x[0], ' '.join(x[1:]))

    return (a ,b)

def Hoje():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    print('Data atual: ' + data_em_texto)

def head(path):
    try:
        if(os.path.isfile(path)==True):
            with open(path,"r",encoding="utf-8") as arquivo:
                text = arquivo.read()
                txt = text.split('\n')
                cont = 0
                for i in txt:
                    print(i)
                    if(cont==9):
                        break
                    cont += 1
        else:
            print('Somente arquivos de texto')
    except:
        print('Arquivo não encontrado')

def cat(path):
    try:
        if(os.path.isfile(path)==True):
            with open(path,"r",encoding="utf-8") as arquivo:
                text = arquivo.read()
                print(text)
        else:
            print('Somente arquivos de texto')
    except:
        print(Exception)

def tail(path):
    try:
        if(os.path.isfile(path)==True):
            with open(path,"r",encoding="utf-8") as arquivo:
                text = arquivo.read()
                txt = text.split('\n')
                cont = len(txt)
                if(cont<10):
                    print(text)
                else:
                    for i in txt[cont-10:]:
                        print(i)
        else:
            print('Somente arquivos de texto')
    except:
        print('Arquivo não encontrado')


def clear():
    i=0
    while(i<50):
        print(' ')
        i += 1


while(code!=False):

    code = input(path+'>')
    (comando,dir) = Entrada(code)
    logDeComandos(comando +' '+ dir)

    if(comando=='exit'):
        code = False

    if(comando=='ls'):
        if(len(dir)>0):
            pathTemp = path + dir
            ls(pathTemp)
        else:
            ls(path)

    if(comando == 'pwd'):
        pwd(path)

    if(comando == 'cd'):
        if(dir=='~'):
            path = 'C:\\'
        else:
            path = cd(path,dir)

    if(comando == 'date'):
        Hoje()

    if(comando == 'head'):
        head(path+'\\'+dir)

    if(comando=='cat'):
        cat(path+'\\'+dir)

    if (comando == 'tail'):
        tail(path + '\\' + dir)

    if (comando=='clear'):
        clear()

    if(comando == 'echo'):
        print(dir)









