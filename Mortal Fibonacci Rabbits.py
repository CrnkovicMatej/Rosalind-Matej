n = 98
m = 16

howManyToLive=[0]*m
howManyToLive[0]=1
for i in range(1,n):
    newBornRabbits=sum(howManyToLive[1:])
    howManyToLive[1:]=howManyToLive[:-1]
    howManyToLive[0]=newBornRabbits
print(sum(howManyToLive))
