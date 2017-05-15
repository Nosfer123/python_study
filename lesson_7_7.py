import datetime


def shout(word='yes'):
    return word.upper()+'!!!'


def whisper(word='yes'):
    return word.lower()+"..."

def wrap(func):
    print("Action before")
    print(func())
    print("Action after")

wrap(shout)
wrap(whisper)
wrap(datetime.datetime.now)
print(datetime.datetime.now())