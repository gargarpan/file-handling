with open('import.txt', 'r') as f1:
    with open('Copy2.py', 'w') as f2:
        for line in f1:
            f2.write(line)
