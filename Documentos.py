from os import listdir, name
from os.path import isfile, join
import os

from nltk import text

class Documento:
    def __init__(object,name,text):
        object.name = name
        object.text = text

    def GetText(self):
        return self.text

    def GetName(self):
        return self.name

def text_file(file_path): 
    with open(file_path, 'r', encoding="utf-8") as f:
        Doc = Documento(file_path.replace('/home/pedro/Documentos/sri/docs',''),f.read()) 
        return Doc.text



def GetArquivos(): # Lista com Os Arquivos (nome e conteudo)
    Arquivos = []
    path = '/home/pedro/Documentos/sri/docs'
    arquivos = [f for f in listdir(path) if isfile(join(path, f))] # Nome dos Arquivos
    for file in arquivos: # Percorer a lista
        file_path = f"{path}/{file}"
        Arquivos.append(text_file(file_path))
        #print(text_file(file_path)) 
    return Arquivos


def PrintArquivosResultado(Calculo):
    index = 1
    retorno = []
    for item in sorted(Calculo, key = Calculo.get):
        retorno.append(f'********************************{index}********************************')
        retorno.append(item)
        index += 1
        if (index == 6):
            return retorno
            break
