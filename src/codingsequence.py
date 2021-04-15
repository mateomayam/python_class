'''
NOMBRE
       codingsequence.py
VERSION
        [1.0]
AUTOR
        Mateo Maya Martínez <matteo.mayam@icloud.com>
DESCRIPCIÓN
        [Este programa encuentra el fragmento codificante de una secuencia dada. Toma TAC como el codón de inicio y TAA como el codón de paro]
CATEGORÍA
       [Genomic sequence.]
USO

OPCIONES
'''

dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
start = dna.find("TAC")
end = dna.find("TAA")

print ("La secuencia codificante es", dna[start:end + 3])