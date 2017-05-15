#f = open('input.txt', 'r')
#for line in f:
#    print(line, end="")
#f.close()


with open('input.txt', 'r') as f: #check to close file automatically
    for line in f:
        print(line, end="")


f.read()