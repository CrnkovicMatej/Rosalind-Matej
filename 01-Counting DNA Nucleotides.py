
#one possible way
#f1=open("rosalind_dna.txt","r")
#ak=f1.resdline()
#f1.close()

ak="GCGCTAAAAGCTCAGTTCGTTCAGTGGGCTAACCATAAGACTGTGGGGAAAAAGGCCGAACAGAATACTATGCACCTCGGGTTACCAAGAGGTGGACGCACGCAGCGCCGTTCAATCACTACCTGAGGGCACGTTCGGCAATTAAATCTCCTTCCGCGTATTGGACTACGTGCTATTCGCTCCATTGCACCTCCGATACCACGAGATAAGAAATCCTTGTATCAGGGCCTACAAGATGTCCGGAATGAGAATACCGTGCTGTCGAGAGGACATGCGTCGTCCTCCTCGAGTCCATATTTCCTACACGTAATACGTGTTAGCCGGTGCGTCGTTCCATAAAAAGAACTAGCGGCAATAAAGTCGCCTAGCATTAATTGACTCCCGCTTTTCGAGAATGGACCATAATAAAATATGGCATGCACTCGAGTGAGCGTCTATGGATTGCCTTCAGTGGTCGTATCTCTATAAACGAGGGTGAGAACTAATACTCCAGTGTTCGGTGTAGTCCCCTGCGTGCAGGTTCATCCCAGATGCGCTACGACTGATTCGGGGCCATGTAGCGGCTAAGAAAGGTCCGGAGGAATACGTCCCGTCGCCGCCCGTTCCTGAACGATGCTAGACAGGGAAATGATGCTGTTAGGACAGATACTTGTCGCCTCGACCTCGACGCGACCACCTGGGGGAATTCCTAGTGAGCACCACCTCCTTGAGGACCTGTCAGCGAATTACGAATGTTGCGATTTCAGGTTAATAATTGTCACTCGAGTCCCTGACAGCGCGCTCCCCGTGCACGCATGACCGACGCGAGATTTCTCGGATATCGGGAATCAGCAGGAGCTGCTCCCGCCTGTGAGTATCGAGTTGAGCTAAGGGCGCAATTCGTCCTCCGGTTTGC"

sumA=0
sumC=0
sumG=0
sumT=0

for i in range (len(ak)):
    if ak[i]=="A":
        sumA+=1
    elif ak[i]=="C":
        sumC+=1
    elif ak[i]=="G":
        sumG+=1
    else: sumT+=1

print(sumA, sumC, sumG, sumT)
