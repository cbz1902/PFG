
def unir():
    ejemplos_positivos= open ('ejemplos_positivos.pl','r')
    ejemplos_negativos= open ('ejemplos_negativos.pl','r')
    dataset = open ('dataset.pl','w')
    dataset.write(ejemplos_positivos.read())
    dataset.write(ejemplos_negativos.read())
    return dataset

unir()

