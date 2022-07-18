from cgitb import text
import os
from typing import Dict
from nltk.tokenize import word_tokenize
from nltk.cluster import cosine_distance
from operator import itemgetter
from PIL import ImageTk, Image
import numpy as np
from BagOfWord import Processamento, Tokenizacao
from Documentos import PrintArquivosResultado
from gensim.models.doc2vec import Doc2Vec
import pandas as pd
from tkinter import *


def similarity(modelSave,tokens,tokens_seach):
    similarity_array = []
    for doc in tokens:
        sim = modelSave.similarity_unseen_docs(tokens_seach,doc)
        similarity_array.append(sim)
    return similarity_array

def getFileName(path):
    name = os.path.basename(path)
    return os.path.splitext(name)[0]

def loadDocData():
    documentos_df = pd.DataFrame(columns=['Nome', 'Similaridade', 'Texto', 'Tokens'])
    docs_folder = os.path.join(os.getcwd(), 'docs')
    files_path = [] # conterá os caminhos absolutos de todos os arquivos dentro da pasta docs
    for root, dirs, files in os.walk(docs_folder):
        for file in files:
            if file.endswith(".txt"):
                files_path.append(os.path.join(root, file))
    files_names = []
    for path in files_path:
        files_names.append(getFileName(path))
    documentos_df['Nome'] = files_names
    doc_texts = []
    for file in files_path:
        with open(file, mode='r') as f:
            doc_texts += [f.read()]
    documentos_df['Texto'] = doc_texts
    tokens = []
    for text in doc_texts:
        tokens.append(Processamento(word_tokenize(text)))
    documentos_df['Tokens'] = tokens
    return documentos_df, tokens



def main() -> None:
        janela = Tk()
        janela.title("SRI JPedro e Vinnycios")
        janela.geometry("1280x720")
        img = PhotoImage(file="/home/pedro/Documentos/sri/assets/logo.png")
        label_image = Label(janela, image=img)
        label_image.grid(column=0,row=0)
        texto_busca = Label(janela, text='Procurar:')
        texto_busca.grid(column=1, row=0)
        entrada = Entry(janela, width=50)
        entrada.grid(column=1, row=0)

        def recebe_entrada():
                input = entrada.get()
                print(input)
                tokens_search = Processamento(word_tokenize(input)) #Tokenizar e formatar busca

                #carregando o modelo
                model = Doc2Vec.load('word2vec_2.model')

                #preparando os arquivos
                documents_df, tokens= loadDocData() # Lista com Arquivos
                similarity_array = similarity(model, tokens, tokens_search)
                documents_df['Similaridade'] = similarity_array
                filtered_df = documents_df.query("`Similaridade` >= 0.80")
                dict_doc = dict(zip(filtered_df['Texto'], filtered_df['Similaridade']))
                if len(dict_doc) == 0:
                    results = ['sem resultados']
                else:
                    results = PrintArquivosResultado(dict_doc)
                    print(len(results))
                label = Label(janela, text=results, width=150, font="arial 10")
                label.grid(column=0, row=2)
        
        botao = Button(janela, text='Buscar', command=recebe_entrada)
        botao.grid(column=2, row=0)
        janela.mainloop()

        #Pesquisa = input('Busca:') # Valor que quero buscar
        """Pesquisa = recebe_entrada()
        PesquisaFormatada = Processamento(word_tokenize(Pesquisa)) #Tokenizar e formatar busca
        TokenPesquisa = Token(PesquisaFormatada)
        Arquivos = GetArquivos() # Lista com Arquivos
        Tokens = Tokenizacao(Arquivos) # Map <Texto,Token>
        CossenoDistancia = CossenoDistance(TokenPesquisa,Tokens)

        PrintArquivosResultado(CossenoDistancia)"""


if __name__ == '__main__':
        main()    