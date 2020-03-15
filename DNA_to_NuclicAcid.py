
#Translate function
''' Return the translated seq of nuclic acid from DNA'''

def translate(seq):

    
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',              
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
            }
    print(len(seq))
    if len(seq)%3 == 0:
        print("div by 3")
        
        protein = ""
        
        for i in range(0, len(seq), 3):
            codon   = seq[ i:i+3]
            protein = protein + table[codon]
            
        return protein
    else:
        print("Invalid input Sequence")


'''def read_seq(inputfile):
    with open(inputfile, "r") as f:
            seq = f.read()
            seq = seq.replace("\n", "")
            seq = seq.replace("\r", "")
            return seq'''

#Main program
        
inputfile ="D:\mydatabase\dna_seq_org.txt"
f = open(inputfile, "r") 
raw_data = f.read()
print(len(raw_data))

result=translate(raw_data)
print(result)
f.close()
rr=result

f=open('Converted_NucicAcid.txt','w+')
f.write(rr)
f.close()






