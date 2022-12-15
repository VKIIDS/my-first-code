#Please my code work
import time
a = 0.5
o = 1.2
k = 2
sum = int(input('how many bux you have? '))
if sum < 10:
    print('sorry you can only buy chips')
print('entering in shop...')
time.sleep(5)
print('please check the list of products')
list = input('want to see list of products? (yes or no) ' )
if list == 'yes':
    print('apples, bananas, potato')
    print('looking for products...')
time.sleep(5)
if list == 'no':
    print('looking for products...')
    time.sleep(5)
ap = input('you want apples, want buy one? ')
if ap == 'yes':
    c = int(input('how many? '))
    b = (a * c)
    l = print('this been cost', str(b), "bux")
    d = (sum - b)
    print('now you have', str(d), "bux")
    print('searching for another products...')
if ap == 'no':
    print('searching for another products...')
lo = input('okay, you found bananas, want buy? ')
if lo == 'yes':
    ls = int(input('how many? '))
    op = (o * ls)
    lo = print ('this been cost', str(op), "bux") 
    lpe = (sum - op)
    print('now you have ', lpe, "bux")
    print('searching for another products...')
if lo == 'no':
    print('searching for another products...')
sss = input('you found potato, want to buy? ')
if sss == 'yes':
    ghoul = int(input('how many? '))
    u = (k * ghoul)
    print('this been cost', u, "bux")
    ssss = (sum - ghoul)
    print('now you have ', ssss ,"bux")
    print ('going to home...')
if sss == 'no':
    print('going to home...')
