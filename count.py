from itertools import count

c1 = count(step= 8, start= 8)
r1 = range(8,100,8)#conta apartir do 8 ao 100 de 8 em 8

print('c1',hasattr(c1, '__iter__'))
print('c1',hasattr(c1, '__next__'))
print('r1',hasattr(r1, '__iter__'))
print('r1',hasattr(r1, '__next__'))

print('count')

for i in c1:
    if i >= 100:
        break
    print(i)

print()

print('range')

for i in r1:
    print(i)    
    