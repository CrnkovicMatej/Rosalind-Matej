##napomena: kada preuzmes datot,eku ne bude pravilna raspodijela slova po redcima
##pa na kraju od svega treba obrisati onoliko slova/brojeva koliko fali u zadnjem retku pojedinog DNa stringa

f1=open("rosalind_cons.txt","r")
ak=f1.read().split("\n")
##ak=f1.read().split(">") 
f1.close()
onlyDnaStrings = []
oneDNa = []
howBigIsOnlyDNa=-1
where_I_am=0
while (where_I_am<len(ak)):
        if(ak[where_I_am][0]==">"):
##            print("jesam te", ak[where_I_am][10] )
            howBigIsOnlyDNa+=1
            where_I_am+=1
            if(howBigIsOnlyDNa>0):
                onlyDnaStrings.append(oneDNa)
                oneDNa=list(ak[where_I_am].join(""))
        oneDNa.append(ak[where_I_am])
        where_I_am+=1
        if(where_I_am==len(ak)):
            onlyDnaStrings.append(oneDNa)
            break
consensus=""
##print(onlyDnaStrings)
##for i in range (len(onlyDnaStrings)):
##    onlyDnaStrings[i]=onlyDnaStrings[i].join(",")
##print(onlyDnaStrings)
matrica = [[0]*(len(onlyDnaStrings[0])*len(onlyDnaStrings[0][0])) for i in range (4)]
for i in range(len(onlyDnaStrings)):
    for j in range(len(onlyDnaStrings[i])):
        for k in range(len(onlyDnaStrings[i][j])):
           if(onlyDnaStrings[i][j][k]=="A"):
            matrica[0][j*len(onlyDnaStrings[0][0])+k]+=1
           if(onlyDnaStrings[i][j][k]=="C"):
            matrica[1][j*len(onlyDnaStrings[0][0])+k]+=1
           if(onlyDnaStrings[i][j][k]=="G"):
            matrica[2][j*len(onlyDnaStrings[0][0])+k]+=1
           if(onlyDnaStrings[i][j][k]=="T"):
            matrica[3][j*len(onlyDnaStrings[0][0])+k]+=1
simbols=["A","C","G","T"]
for j in range (len(matrica[0])):
    maxbr=0
    ind=0
    for i in range (4):
        if(matrica[i][j]>maxbr):
            maxbr=matrica[i][j]
            ind=i
    consensus+=simbols[ind]
print(consensus)
for i in range (4):
    print(simbols[i]+ ":", end = ' ')
    for j in range (len(matrica[0])):
        print(matrica[i][j], end = ' ')
    print()  

