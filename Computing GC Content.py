f1=open("rosalind_gc.txt","r")
ak=f1.read()
f1.close()
highest_content=0
hig = ""
def GC_content (s):
    num=0
    for i in range(len(s)):
        if(s[i]=="C" or s[i]=="G"):
            num+=1
    return num/len(s)*100
for i in range(len(ak)):
    if ak[i]==">":
        new=ak[i+1:i+14]
        i=i+14
        new1=""
        while (i<len(ak) and ak[i]!= '>'):
            if(ak[i]=='\n'):
                i+=1
            else:
                new1+=ak[i]
                i+=1
        if(GC_content(new1)>highest_content):
            highest_content=GC_content(new1)
            hig=new
print(hig)
print(highest_content)

