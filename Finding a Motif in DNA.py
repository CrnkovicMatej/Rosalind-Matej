f2=open("rosalind_subs.txt", "r")
s=f2.readline().replace("\n","")
t=f2.readline().replace("\n","")
f2.close()
##print(s)
##print(t)
list=[]
for i in range(len(s)):
    if(s[i:i+len(t)]==t):
        list.append(i+1)
        i+=len(t)
for i in list:
    print(i, end=" ")
        

