def shout(word="yes"):
    return word.upper()+"!!!"

print(shout())
scream = shout
print(scream())

del shout

try:
    print(shout())
except NameError as err:
    print(err)

print(scream())