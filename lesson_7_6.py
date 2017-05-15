def get_talk(talk_type='shout'):
    def shout(word='yes'):
        return word.upper()+'!!!'

    def whisper(word='yes'):
        return word.lower()+"..."

    if talk_type == 'shout':
        return shout
    else:
        return whisper

talk = get_talk()

print(talk('hello'))
talk = get_talk(talk_type='whisper')
print(talk('TSSSsss'))