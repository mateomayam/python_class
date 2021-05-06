'''
NAME
       fasta_sequences.py

VERSION
        1.0

AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>

DESCRIPTION

       Programa que permite convertir un archivo de secuencias raw a formato FastA
       
CATEGORY
       Genomic sequence.

USAGE

       python fasta_sequences.py
      

OPTIONS
       Ninguna
      
INPUT FILE
       4_dna_sequences.txt: El programa lee el archivo con este nombre y debe estar en el formato correcto
                            El programa busca el archivo en la ruta relativa ../doc/4_dna_sequences.txt
                               a partir de donde se corre el programa
       Formato:
              seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
              seq_2 = "actgatcgacgatcgatcgatcacgact"
              seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"
                                    
OUTPUT FILE
       
        dna_sequences.fasta: Nombre del archivo de salida en formato FastA
        
        Formato:
              > seq_1
              ATCGTACGATCGATCGATCGCTAGACGTATCG
              > seq_2
              ACTGATCGACGATCGATCGATCACGACT
              > seq_3
              ACTGACACTGTACTGTACATGTG          

SOURCE 
       GitHub: https://github.com/MateoMayaM/python_class/blob/master/src/fasta_sequences.py

'''

# Abrir y leer el archivo que contiene las secuencias
input_file = open("../docs/4_dna_sequences.txt")
input_file_lines = input_file.readlines()
input_file.close()

# Crear el archivo de salida para guardar secuencias en formato FastA
output_file = open("dna_sequences.fasta", "w")

# Procesar cada linea del archivo de entrada
for line in input_file_lines:
    line = line.split((" "))
    seq_name = line[0]
    sequence = (line [-1])
    
    # eliminar de la secuencia caracteres [- "]  que no son DNA
    sequence = sequence.replace('-', '')
    sequence = sequence.replace('"', '')
       
    # Formatear secuencias en un mismo estilo, todas a mayusculas
    sequence = sequence.upper()
    
    # Guardar secuencias en formato FastA
    output_file.write("> " + seq_name + "\n" + sequence)

output_file.close()

print ("The FastA file dna_sequences.fasta was created correctly\n")
