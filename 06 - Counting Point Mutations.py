f1=open("rosalind_hamm.txt", "r")
ak1=f1.readline()
ak2=f1.readline()
f1.close()
hamming_distance=0
for i in range (len(ak1)):
    if((ak1[i]!=ak2[i])):
        hamming_distance+=1
print(hamming_distance)
