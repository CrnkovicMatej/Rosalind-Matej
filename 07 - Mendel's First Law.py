from math import factorial
def binomial (x, y):
    try:
        binom = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        binom = 0
    return binom
f1=open("rosalind_iprb.txt","r")
ak=f1.readline().split(" ")
f1.close()

##k homozygous for dominant, m are heterozygous, and n are homozygous recessive
##probability is 1 - [(selecting 2 parents from the n group)+(selecting 1 parent
## from the n group and one from the m group)*(1/2)+ (selecting 2 parents
## from the m group)*(1/4)

k=int(ak[0])

m=int(ak[1])

n=int(ak[2])

population_sum=k+m+n
binom=binomial(population_sum,2)

probability =1
probability-=binomial(n,2)/binom
probability-=(m*n/2)/binom
probability-=(binomial(m,2)/4)/binom
print(probability)
