import math

k=6 ##k-th generation
n=18 ##N Aa Bb organisms

##Aa probability = 1/2 in every iteration
##Bb probability = 1/2 in every iteration
##AaBb probability = (Aa) probability * (Bb) probability because Mendel's second law holds
##AaBb probability = 1/4

totalOfOffsprings = 2**k
allProbabilities = 0

def BinCoeff(n,k):
    return math.factorial(n)/ (math.factorial(k)*math.factorial(n-k))

for i in range (n, totalOfOffsprings+1):
   allProbabilities+= BinCoeff(totalOfOffsprings, i)*((1/4)**i)*((1-1/4)**(totalOfOffsprings-i)) 

print(allProbabilities)


