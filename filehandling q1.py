n=int(input("Enter Lines You Want to Read from last:"))
with open('import.txt','r') as f:
    cc=f.readlines()[-n:]
    for line in cc:
        print(line)
