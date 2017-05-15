f = open('input.txt', 'w') #w-write
# 'r' - read, 'a' - append, 'r+' - wirte and read

f.write('first line\n')
f.write('second line')
f.close()

f = open('input.txt', 'r')
print(f.read())
f.close()

