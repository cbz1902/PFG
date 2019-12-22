#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""************************************SE IMPORTAN LAS LIBRERIAS A UTILIZAR********************************************************************************"""
import  itertools
from itertools import combinations
from trabajar_archivos import leer_txt, escribir_txt, escribir_archivo_positivo_pl

def combinar_sustantivos(lista_sustantivos):
    """Método que realiza las combinaciones de los sustantivos
    @lista_sustantivo: lista de sustantivos a ser combinados
    @combinaciones: lista de combinaciones realizada"""
    lista_nueva = []
    for elemento in lista_sustantivos:
        if elemento not in lista_nueva:
            elemento = elemento.replace('\n','')
            lista_nueva.append(elemento)
    combinaciones = list(itertools.combinations(lista_nueva, 2))  # iterador que realiza las combinaciones
    return combinaciones

def conocimiento_base(data):
    """Método que define el conocimiento base
    @data: lista de sustantivos utilizados para generar el conocimiento base
    """
    conocimiento_base = []
    for i in data:
        i = i.replace('\n','')
        conocimiento_base.append("es_sustantivo_dengue("+i+").")
    return conocimiento_base

def unir():
    """Método utilizado para generar el dataset final
    """
    ejemplos_positivos= open ('data/ejemplos_positivos.pl','r')
    conocimiento_sustantivo= open ('data/es_sustantivos.pl','r')
    dataset = open ('dataset.pl','w')
    dataset.write(ejemplos_positivos.read())
    dataset.write('%Conocimiento Base' + '\n')
    dataset.write(conocimiento_sustantivo.read())
    dataset.close()

if __name__ == "__main__":
    resp = leer_txt('data/tweets_sustantivos.txt')
    escribir_archivo_positivo_pl(combinar_sustantivos(resp))
    escribir_txt('data/es_sustantivos.pl',conocimiento_base(resp))
    unir()