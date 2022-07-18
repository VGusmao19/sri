import heapq
from typing import Text
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from nltk.cluster.util import cosine_distance
import re

def Processamento(Texto): #Formatar documentação (Retorna uma Lista com as palavras formatadas)
        numero = r'[0-9]'
        stemmer = RSLPStemmer() #palavras com radicais
        stopwords = nltk.corpus.stopwords.words('portuguese') #preposições de stopwords
        TextoSemNumero = [data for data in Texto if not data.isdigit()] # remover numeros
        TextoPreFormatado = [data for data in TextoSemNumero if data not in stopwords] # remover stopwords    
        for i in range (len(TextoPreFormatado)):
                TextoPreFormatado[i] = TextoPreFormatado[i].lower() #letra minuscula             
                TextoPreFormatado[i] = TextoPreFormatado[i].rstrip('s') #remover plural
                if TextoPreFormatado[i][-1] == 'a':                        
                        TextoPreFormatado[i] = TextoPreFormatado[i][:-1] + "o" #deixar palavras no masculino
                TextoPreFormatado[i] = re.sub(r'[^\w]', '', TextoPreFormatado[i]) # remover pontuações
                if len(TextoPreFormatado[i]) >= 3: 
                         TextoPreFormatado[i] = stemmer.stem(TextoPreFormatado[i]) #Radical da Palavra
        TextoFormatado = []
        for palavra in TextoPreFormatado:
                TextoFormatado.append(palavra)
        return TextoFormatado

def Tokenizacao(Arquivos): # Tokenizacao de todos os Documentos
        Tokens = {}
        for documento in Arquivos:
                Texto = word_tokenize(documento) #Tokenizar conteudo
                Tokens[documento] = Processamento(Texto)
        return Tokens