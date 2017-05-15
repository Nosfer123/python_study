def talk():
    def whisper(word="Yes"):
        return word.lower()+"..."
    print(whisper())

talk()
talk()


try:
    print(whisper())
except NameError as err:
    print(err)