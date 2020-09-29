f1=open("RNA_codonTable.txt","r")
cod=f1.readlines()
f1.close()
for i in range (len(cod)):
    cod[i]=cod[i].replace("\n","")
    cod[i]=cod[i].split(" ")
    while(("") in cod[i]):
        cod[i].remove("")

rnaString=""
protein=""
f2=open("rosalind_prot.txt", "r")
bla=f2.read().replace(" ","")
f2.close()

for i in range (1,(len(bla)+1)):
    if((i%3)==0):
        rnaString+=bla[i-1]
        for j in range (len(cod)):
            if(rnaString==cod[j][0]):
                protein+=cod[j][1]
        rnaString=""
    else:
        rnaString+=bla[i-1]
print(protein.replace("Stop",""))
