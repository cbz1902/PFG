def escribir_txt(path,data):
    """Funcion que escribe los archivos txt
    @path: directorio dónde va escribir el archivo
    @data: datos a escribir"""
    try:
        with open(path, 'w') as File:
            for i in data:
                File.write(str(i)+"\n") 
    except:
        print("path de escritura "+path+" incorrecto..")
        exit(0)
    File.close()

def escribir_archivo_positivo_pl(lista_combinada):
    """Método que escribe la lista de sustantivo combinado
    @lista_combinada: lista de sustantivo combinad
    """
    f = open('data/ejemplos_positivos.pl', 'w')
    f.write('%Ejemplos positivos' + '\n')
    for elemento in lista_combinada:
        line = ', '.join(str(x) for x in elemento)
        f.write('combinado_con(' + line + ').' + '\n')
    f.close()

def leer_txt(path):
    """Método que lee un archivo txt
    @path: direcctorio dónde se encuentra el archivo txt a ser leido
    @lista: lista que contiene los datos del archivo"""
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