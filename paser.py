#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""************************************SE IMPORTAN LAS LIBRERIAS A UTILIZAR********************************************************************************"""
import spacy
import csv
from spacy.lang.es.examples import sentences
from trabajar_archivos import leer_txt, escribir_txt

def procesar(data):
    """Método que parsea los tweets
    @data: lista de tweets
    @dic2: diccionario de tweets parseados
    """
    nlp = spacy.load('es_core_news_sm')
    dic2 = {}
    for text in data:
        dic1 = {}    
        doc = nlp(text)
        for token in doc:            
            dic1[token.text] = token.pos_
        dic2[text]=dic1

    return dic2
        
if __name__ == "__main__":    
    result = leer_txt("data/tweets_capturados.txt")
    result2 = procesar(result)
    l = []
    for i in result2.values():
        l.append(i)
    escribir_txt('data/tweets_parseados.txt',l)
