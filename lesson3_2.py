name = ['Illia', 'Dima', 'Denis']

for name in names:
    answer = input('Your name  is {}?(y/n)'.format(name))
    if answer == 'y':
        print ('Yes')
        break