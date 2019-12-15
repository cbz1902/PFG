import  itertools
from itertools import combinations

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

def escribir_archivo_positivo(lista_combinada):
    f = open('data/ejemplos_positivos.pl', 'w')
    f.write('%Ejemplos positivos' + '\n')
    for elemento in lista_combinada:
        line = ', '.join(str(x) for x in elemento)
        f.write('combinado_con(' + line + ').' + '\n')
    f.close()

def conocimiento_base(data):
    conocimiento_base = []
    for i in data:
        conocimiento_base.append("es_sustantivo_dengue("+i+").")
    return conocimiento_base
def escribir_txt(path,data):
    try:
        with open(path, 'w+') as File:
            for i in data:
                File.write(str(i)+'\n')
    except:
        print("path de escritura "+path+" incorrecto..")
        exit(0)
    File.close()

resp = leer_txt('data/tweets_sustantivos.txt')
escribir_txt('data/es_sustantivos.pl',conocimiento_base(resp))
escribir_archivo_positivo(combinar_sustantivos(resp))
