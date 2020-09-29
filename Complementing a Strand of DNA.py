f1=open("rosalind_revc.txt","r")
ak=f1.readline()
f1.close()
##ak="AAAACCCGGT"
new = ak[::-1]
##not a good solution
##for r in (("A","T"),("T","A"),("C","G"),("G","C")):
##    new.replace(*r)
for i in range (len(new)):
    if(new[i]=="A"):
        new=new[:i]+'T'+new[i+1:]
    elif(new[i]=="T"):
        new=new[:i]+'A'+new[i+1:]
    elif(new[i]=="G"):
        new=new[:i]+'C'+new[i+1:]
    elif(new[i]=="C"):
        new=new[:i]+'G'+new[i+1:]
print(new)
