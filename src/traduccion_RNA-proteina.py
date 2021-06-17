'''
NAME
       [traduccion_RNA-proteina].py
VERSION
        [1.0]
AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>
DESCRIPTION
        [Este programa recibe como input una secuencia de RNA y la traduce a una proteina]
CATEGORY
       [Sequence.]
USAGE
       [De uso bioinformático. Corre en python.]
OPTIONS
       [Este programa no tiene opciones.]

EXAMPLES
       [Input: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
        Output: MAMAPRTEINSTRING
LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/traduccion_RNA-proteina.py]
'''

#Pedir al usuario la secuencia que quiere traducir.
rna = input("Introduce la secuencia de RNA que quieres traducir:\n")

#Reemplazar todas los uracilos por timinas.
rna = rna.replace ('U', 'T')

#Identificar la posicion codon de inicio.
start = rna.find("ATG")

#Definir codones como una lista vacía.
codones = []

#Definir el diccionario que contiene los codones y el aminoacido que codifican.
genecode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#Dividir la secuencia en codones y guardar cada codon en la lista que habiamos inicializado.
for i in range (start, (len(rna)-1), 3):
    codon = rna[i:(i+3)]
    codones.append(codon)

#Definir una lista vacia para guardar los aminoacidos.
amino = []

#Comparar los codones de la secuencia con los del codigo genetico, si son iguales, reemplazarlos por el aminoacido que codifican
for j in codones:
    for key, value in genecode.items():
        if j == key:
            amino.append(value)

#Juntar los aminoacidos de la lista en un string
protein = (''.join(amino))

#Obtener solo, los aminoacidos que estan antes del primer codon de paro e imprimirlas.
protein = protein.split("_")
print (f"Tu proteina es la siguiente:\n{protein[0]}")