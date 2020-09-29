import urllib.request

f1=open("rosalind_mprt.txt", "r")
ak=f1.read().splitlines()
f1.close()

##N-glycosylation motif is written as N{P}[ST]{P}

listOfURLs = []
for i in ak:
    listOfURLs.append('http://www.uniprot.org/uniprot/' + i + '.fasta')
##print(listOfURLs)

listOfFastas = []
for k in listOfURLs:
    file = urllib.request.urlopen(k)
    temp = ""
    for line in file:
        temp += line.decode("utf-8")
    listOfFastas.append(temp)
    ##for line in file:
      ##  temp += str(line)
    ##print(temp)

i=0
for k in listOfFastas:
    index = k.find('\n')
    k = k[index+1:]
    k = k.replace('\n','')
    locations = ""
    for j in range (len(k)-4+1):
        if(k[j]=='N' and k[j+1]!='P' and (k[j+2]in['S','T'])and k[j+3]!='P'):
           locations+=str(j+1)+' '
    if(locations!=''):
           print(ak[i])
           print(locations)
    i+=1

