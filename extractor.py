#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""************************************SE IMPORTAN LAS LIBRERIAS A UTILIZAR********************************************************************************"""
import spacy
import itertools
from itertools import combinations
import ast
import re
from trabajar_archivos import leer_txt, escribir_txt

exp_reg = '@.|#|.1.|.2.|.0.|.3.|.4.|.5.|.6.|.7.|.8.|.9.' #Variable que define la expresión regular a ser utilizada

def quitar_repetidos(lista):
    """Método que quita las palabras repetidas en una lista
    @lista: lista recibida para limpiar las palabras repetidas
    @lista_nueva: lista retornada con las palabras ya limpiadas
    """
    lista_nueva = []
    for elemento in lista:
        if str(elemento).lower() not in lista_nueva:
            lista_nueva.append(limpiar_acentos(str(elemento).lower()))
    return lista_nueva

def limpiar_acentos(text):
    """Método que elimina los acentos de una cadena
    @text: palabra recibida para eliminar los acentos
    @text_nuevo: palabra ya sin los acentos
    """
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    text_nuevo = text
    for acen in acentos:
        if acen in text:
            text_nuevo = text.replace(acen, acentos[acen])
    return text_nuevo

def extraer_sustantivos(lista):
    """Método que extrae los sustantivos de una lista
    @lista: lista recibida para la extracción de los sustantivos
    @sustantivo: sustantivos que fueron extraidos de la lista recibida
    """
    sustantivo = []
    for i in lista:
        dic = ast.literal_eval(i)
        for j,k in dic.items():
            if k == "NOUN":
                if re.match(exp_reg, str(j),flags=re.IGNORECASE) == None:
                    sustantivo.append(j)
    return sustantivo

if __name__ == "__main__":    
    sust = extraer_sustantivos(leer_txt("data/tweets_parseados.txt"))
    escribir_txt('data/tweets_sustantivos.txt',(sust))

