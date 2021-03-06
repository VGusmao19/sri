from cgitb import text
import math
from typing import Dict
from nltk.tokenize import word_tokenize
from nltk.cluster import cosine_distance
from operator import itemgetter
from PIL import ImageTk, Image
import numpy as np
from BagOfWord import Processamento, Tokenizacao
from Documentos import GetArquivos, PrintArquivosResultado

from tkinter import *

def Token (Keys): # Cria um map <Palavra,Peso>s
        Contador = {}
        for key in Keys:
                Contador[key] = 0
        return Contador

def computeTF(Vetor,BagOFWord):
        Resultado = []
        count = len(BagOFWord)
        for valor in Vetor:
                Resultado.append(valor / count)
        return Resultado

def computeIDF(BagOFWord,Arquivos):
        Resultado = {}
        for word in BagOFWord:
                Resultado[word] = math.log(len(Arquivos)/DocsComTermo(word,Arquivos))
        return Resultado        
              
def DocsComTermo(Termo,Arquivos):
        count = 0
        for key,value in Arquivos.items():
                if Termo in value:
                        count += 1
        return count

def computeTF_IDF(Vetor,BagOfWord,Arquivos):
        Resultado = []
        index = 0
        TF = computeTF(Vetor,BagOfWord)
        IDF = computeIDF(BagOfWord,Arquivos)
        for key,value in IDF.items():
                Resultado.append(TF[index] * value)
                index += 1
        return Resultado


def Similaridade(TokenPesquisa,Tokens,Arquivos): # Calculo da Similaridade
        Chaves = list(TokenPesquisa.keys()) #Lista com as chaves da pesquisa
        TodasPalavras = list(set(Chaves + Tokens)) #Lista com todas as palavras (Pesquisa + Documento)
        Vetor1 = [0] * len(TodasPalavras)
        Vetor2 = [0] * len(TodasPalavras)
        for palavra in Chaves:  #Calcular vetor de quantidade de termo para Chave
                 Vetor1[TodasPalavras.index(palavra)] += 1
        for palavra in Tokens:  #Calcular vetor de quantidade de termo para Documento
                 Vetor2[TodasPalavras.index(palavra)] += 1
        Vetor1 = computeTF_IDF(Vetor1,TodasPalavras,Arquivos)
        Vetor2 = computeTF_IDF(Vetor2,TodasPalavras,Arquivos)
        #print(Vetor1)
        #print(Vetor2)
        #print()
        return (cosine_distance(Vetor1,Vetor2))

def CossenoDistance(TokenPesquisa,Arquivos):
        Resultado = {}
        for key,value in Arquivos.items():
                Resultado[key] = Similaridade(TokenPesquisa,value,Arquivos)
        Ordenado = sorted(Resultado.items(),key=itemgetter(1))
        #print(Ordenado)
        return Resultado



def main() -> None:
<<<<<<< HEAD
        janela = Tk()
        janela.title("Goospel by JPedro e Vinnycios")
=======
        """janela = Tk()
        janela.title("SRI JPedro e Vinnycios")
>>>>>>> 2ebed87518054c07d3fb7c9f294fc46f6ea41703
        janela.geometry("1280x720")
        img = PhotoImage(file="C:/Users/vinny/Desktop/engInfo/imagens/imagem.png")
        label_image = Label(janela, image=img)
        label_image.grid(column=0,row=0)
        texto_busca = Label(janela, text='Procurar:')
        texto_busca.grid(column=1, row=0)
        entrada = Entry(janela, width=50)
        entrada.grid(column=1, row=0)

        def recebe_entrada():
                input = entrada.get()
                print(input)
                Pesquisa = input
                PesquisaFormatada = Processamento(word_tokenize(Pesquisa)) #Tokenizar e formatar busca
                TokenPesquisa = Token(PesquisaFormatada)
                Arquivos = GetArquivos() # Lista com Arquivos
                Tokens = Tokenizacao(Arquivos) # Map <Texto,Token>
                try:
                        CossenoDistancia = CossenoDistance(TokenPesquisa,Tokens)
                        print(CossenoDistancia)
                        resultados = PrintArquivosResultado(CossenoDistancia)
                        print(type(resultados))
                except ZeroDivisionError:
                        resultados = ['sem resultados']
                #PrintArquivosResultado(CossenoDistancia) 
<<<<<<< HEAD
                label = Label(janela, text=resultados, width=150, font="arial 5")
=======
                resultados = PrintArquivosResultado(CossenoDistancia)
                label = Label(janela, text=resultados, width=150, font="arial 7")
>>>>>>> 2ebed87518054c07d3fb7c9f294fc46f6ea41703
                label.grid(column=0, row=2)
        
        botao = Button(janela, text='Buscar', command=recebe_entrada)
        botao.grid(column=2, row=0)
        janela.mainloop()"""

        Pesquisa = input('Busca:') # Valor que quero buscar
        #Pesquisa = recebe_entrada()
        PesquisaFormatada = Processamento(word_tokenize(Pesquisa)) #Tokenizar e formatar busca
        TokenPesquisa = Token(PesquisaFormatada)
        Arquivos = GetArquivos() # Lista com Arquivos
        Tokens = Tokenizacao(Arquivos) # Map <Texto,Token>
        CossenoDistancia = CossenoDistance(TokenPesquisa,Tokens)
        #PrintArquivosResultado(CossenoDistancia)

if __name__ == '__main__':
        main()    