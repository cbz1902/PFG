import  itertools
from itertools import combinations

def leer():
    diferencias = []
    for item in open('archivos_txt/noepidemia.txt'):
        if item not in open('archivos_txt/epidemia.txt'):
            line = item.rstrip("\n")
            diferencias.append(line)
    return (diferencias)


#funcion que permite eliminar los duplicados y realizar las combinaciones
def combinar_sustantivos(lista_sustantivos):
    lista_nueva = []
    for elemento in lista_sustantivos:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    combinaciones = list(itertools.combinations(lista_nueva, 2))  # iterador que realiza las combinaciones
    return combinaciones
def leer_txt(path):
    lista = []
    try:
        with open(path,'r') as File:
            for item in File:
                line = item.rstrip("\n")
                lista.append(line)
            
    except:
       print("path de lectura "+path+" incorrecto..")
       exit(0)
    File.close()
    return lista

def escribir_archivo(lista_combinada):
    f = open('ejemplos_negativos.pl', 'w')
    f.write('%Ejemplos negativos' + '\n')
    for elemento in lista_combinada:
        line = ','.join(str(x) for x in elemento)
        f.write('combinado_con(' + line + ')' + ':- fail.' + '\n')
    f.close()


def escribir_archivo_positivo(lista_combinada):
    f = open('ejemplos_positivos.pl', 'w')
    f.write('%Ejemplos positivos' + '\n')
    for elemento in lista_combinada:
        line = ','.join(str(x) for x in elemento)
        f.write('combinado_con(' + line + ')' + ':- fail.' + '\n')
    f.close()

escribir_archivo_positivo(combinar_sustantivos(leer_txt('data/tweets_sustantivos.txt')))
escribir_archivo(combinar_sustantivos(leer()))

