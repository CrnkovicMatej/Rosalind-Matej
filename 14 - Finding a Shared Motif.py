f1=open("rosalind_lcsm.txt", "r")
ak=f1.read()
f1.close()
listOfNames=[]
listOfStrings=[]
i=0
newname =""
newstring=""
while (i<len(ak)):
    if(ak[i]==">"):
        newname = ""
        while((ak[i]!='\n') and (i<len(ak))):
            newname+=ak[i]
            i+=1
        listOfNames.insert(len(listOfNames), newname)
    newstring=""
    while((ak[i]!=">")):
        newstring+=ak[i]
        i+=1
        if(i==len(ak)):
            break
    newstring=newstring.replace('\n','')
    listOfStrings.insert(len(listOfStrings), newstring)
lcsb=""
for i in range(len(listOfStrings[0])):
    if((i+len(lcsb)) <= len(listOfStrings[0])):
        for j in range(i+len(lcsb), len(listOfStrings[0])):
            newLcsb=listOfStrings[0][i:j+1]
            flag=0
            for k in range(1, len(listOfStrings)):
                if(newLcsb not in listOfStrings[k]):
                    flag=1
                    break
            if (flag==0 and len(newLcsb)>len(lcsb)):
                lcsb=newLcsb
    else:
        break
print(lcsb)

