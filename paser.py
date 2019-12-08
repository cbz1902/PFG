import spacy
import csv
from spacy.lang.es.examples import sentences

def procesar(data):
    nlp = spacy.load('es_core_news_sm')
    dic2 = {}
    for text in data:
        dic1 = {}    
        doc = nlp(text)
        for token in doc:            
            dic1[token.text] = token.pos_
        dic2[text]=dic1

    return dic2
        
        

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

def escribir_txt(path,data):
    try:
        with open(path, 'w') as File:
            for i in data:
                File.write(str(i)+'\n')
    except:
        print("path de escritura "+path+" incorrecto..")
        exit(0)
    File.close()

if __name__ == "__main__":    
    result = leer_txt("data/tweets_capturados.txt")
    result2 = procesar(result)
    l = []
    for i in result2.values():
        l.append(i)
        
    escribir_txt('data/tweets_parseados.txt',l)
