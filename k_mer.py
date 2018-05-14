import sys
import glob
from Bio import SeqIO

file_name = sys.argv[1] #get the miRNA .fasta file name
mer_num = int(sys.argv[2])


records = list(SeqIO.parse(file_name,"fasta"))
kmer_file = open("temp_kmer.file",'w')
for i in xrange(0,len(records)):
    temp_records = records[i]
    for j in xrange(0,len(temp_records)-mer_num+1):
        seq_name = ">"+temp_records.name + "_" +str(j+1) + "_to_" + str(j +0+ mer_num)
        kmer_file.write(seq_name)
        kmer_file.write("\n")
        kmer_file.write(str(temp_records.seq[j:j+mer_num]))
        kmer_file.write("\n")

kmer_file.close()

    
    


