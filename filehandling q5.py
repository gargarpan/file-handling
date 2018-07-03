import random
afile = open("Random.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 9))
    afile.write(line)
    print(line)
afile.close()

f1=open("Random.txt","r")
lines=f1.read()
for l in  lines:
    words=l.split()
    print(words)
f1.close()

f2=open("Random.txt","r")
line=f2.read()
data=sorted(line)
print(data)
f3=open("SortData.txt","w")
f3.write(str(data))
f3.close()
f2.close()
