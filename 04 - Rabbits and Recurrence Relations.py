f1=open("rosalind_fib.txt","r")
ak=f1.readline()
f1.close()
ak=ak.split(" ")
n=int(ak[0])
k=int(ak[1])
def rabbits (n,k):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return k+1
    else:
        return rabbits(n-1,k)+k*rabbits(n-2,k)
print(rabbits(n,k))
