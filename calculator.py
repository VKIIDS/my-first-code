while True:
    a = int(input('print your first number '))
    b = int(input('print your two number '))
    c = input ('what we do? ( +, -, /, //, *, **, %) ---> ')
    if c == '+':
        print (a + b)
    elif c == '-':
        print (a - b)
    elif c == '/':
        print (a / b)
    elif c == '//':
        print (a // b)
    elif c == '*':
        print (a * b)
    elif c == '**':
        print (a ** b)
    elif c == '%':
        print (a % b)
    else:
        print('Wut?')
