f1=open("rosalind_grph.txt", "r")
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
k=len(listOfNames)
for i in range(k):
    for j in range(k):
        if (i==j):
            continue
        if((listOfStrings[i][(len(listOfStrings[i])-3):]) == (listOfStrings[j][0:3])):
            print(listOfNames[i].replace('>','') + ' ' + listOfNames[j].replace('>',''))
        
