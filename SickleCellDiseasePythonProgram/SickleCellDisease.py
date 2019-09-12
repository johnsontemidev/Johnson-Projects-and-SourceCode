

# ================= INTRODUCTION TO PROGRAMMING - TASK 25 ====================
# ================= JOHNSON TEMILOLA - [02/04/2019] ==========================

# =========== PROGRAM DESCRIPTION ===========================
# Code to translate the DNA sequence to a sequence of Amino acids where each Amino acid is represented by a unique letter
'''
   a function called ‘translate’ that, when given a DNA sequence of arbitrary length,
the program identifies and returns the amino acid sequence of the DNA using the
amino acid SLC code found in that table.
E.g DNA Input: ATTATTATT
Output: III (representing: Isoleucine, Isoleucine, Isoleucine )
 There are many different amino acids, so this may get a bit repetitive. Just do the first
five Amino Acids (i.e I, L, V, F M) and make any other codon be printed as the amino
acid 'X' . So basically, you would use an if - elif - elif .... else structure to translate each
codon of DNA into the correct Amino Acid.
  Note that the program must be able to handle DNA sequences that are not of a length
divisible by 3.
'''

# open the file and in read mode.
# the text file contains some unformatted hidden characters by default
# characters as “/n” or “/r” needs to be formatted and removed. So we use replace() function and get the altered DNA sequence txt file from the Original txt file.

input_file = "DNA.txt"
f = open (input_file, "r")
seq = f.read()

seq = seq.replace("\n", "")
seq = seq.replace("\r", "")

# define a function called 'translate'
def translate(seq): 
    # Table just for reference   
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
    } 
    protein = ""

    # DNA sequence to check if divisible by 3
    # Form codons and match them with amino acids in the table
    # The variable called 'Protein' which forms Amino Acid sequence and return it
    
    for i in range(0, len(seq), 3): 
            codon = seq[i:i + 3]
            if codon in table:
                protein += table[codon]
            else:
                protein += 'X'

                
    return protein


# ==================== TASK 2 =========================
'''
  Define a function called 'mutate()'
     open the file (DNA.txt) in read mode
     open the another file (normalDNA.txt) as the first file in a write mode
     open the another file (mutatedDNA.txt) as the second file in a write mode

     If the variable 'f'.mode is equal to the read mode
        for each line in f.readlines
           if 'a' is in the line
             replace the "a" with "A", and write this result to the first file called "normalDNA.txt"
             replace the "a" with "T", and write this result to the second file called "mutatedDNA.txt"
           otherwise
             write line to the first file
             write line to the second file
     close the file

'''

def mutate():
    f = open("DNA.txt", "r")
    file_one = open("normalDNA.txt","w+")
    file_two = open("mutatedDNA.txt","w+")

    if f.mode == 'r':
        for line in f.readlines():
            if 'a' in line:
                file_one.write(line.replace('a', 'A'))
                file_two.write(line.replace('a', 'T'))
            else:
                file_one.write(line)
                file_two.write(line)

    f.close()

'''
  Define a txtTranslate() function called Translate
  txtTranslate() function reads from 'NormalDNA.txt' as first file, and the second file as mutatedDNA.txt
  pass the dna_string sequence in 'normalDNA.txt' and then 'mutatedDNA.txt' to the translate() function
  call the mutate() function, and txtTranslate() function
'''

dna_string_one = ""
dna_string_two = ""

def txtTranslate():
    
    file_one = open("normalDNA.txt","r")
    file_two = open("mutatedDNA.txt","r")

    dna_string_one = translate(file_one.read())
    dna_string_two = translate(file_two.read())


    print (dna_string_one)
    print (dna_string_two)

    file_one.close()
    file_two.close()

mutate()
txtTranslate()
            

    
        









