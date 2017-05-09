def input_phrase():
    return input('Enter your phrase: ')

def input_letter():
    return input('Enter your letter: ')

def count_letters():
    counter = 0
    phrase = input_phrase()
    let = input_letter()
    for letter in phrase:
        if letter == let:
            counter +=1
    counter=str(counter)
    print('Your phrase have ' + counter + ' such letters')

count_letters()

