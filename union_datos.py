
def unir():
    ejemplos_positivos= open ('data/ejemplos_positivos.pl','r')
    conocimiento_sustantivo= open ('data/es_sustantivos.pl','r')
    dataset = open ('dataset.pl','w')
    dataset.write(ejemplos_positivos.read())
    dataset.write('%Conocimiento Base' + '\n')
    dataset.write(conocimiento_sustantivo.read())
    return dataset

unir()

