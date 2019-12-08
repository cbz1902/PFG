import spacy
import itertools
from itertools import combinations
import ast
import re
exp_reg = '@.|#|.1.|.2.|.0.|.3.|.4.|.5.|.6.|.7.|.8.|.9.'
nlp = spacy.load("es_core_news_sm")


def leer_txt(path):
    lista = []
    try:
        with open(path,'r') as File:
            for line in File:
                lista.append(line)
            
    except:
       print("path de lectura "+path+" incorrecto..")
       exit(0)
    File.close()
    return lista

def quitar_repetidos(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva

def extraer_sustantivos(lista):
    sustantivo = []
    for i in lista:
        dic = ast.literal_eval(i)
        for j,k in dic.items():
            if k == "NOUN":
                if re.match(exp_reg, str(j),flags=re.IGNORECASE) == None:
                    sustantivo.append(j)
    return sustantivo

def escribir_txt(path,data):
    try:
        with open(path, 'w+') as File:
            for i in data:
                File.write(str(i)+'\n')
    except:
        print("path de escritura "+path+" incorrecto..")
        exit(0)
    File.close()

sust = extraer_sustantivos(leer_txt("data/tweets_parseados.txt"))
escribir_txt('data/tweets_sustantivos.txt',quitar_repetidos(sust))
