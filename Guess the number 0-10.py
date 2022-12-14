while True:
    from random import randint
    a = randint(0, 10)
    b = int(input('print your first number (0-10) '))
    if b == a:
        print('Yaaay you win!')
    else:
        print('Sorry, you loose this number is:', a)
