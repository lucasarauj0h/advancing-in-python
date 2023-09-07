#similar ao range, mas no range você o avisa até onde chegar, um limite, um fim;
#o count você avisa aonde começa. 
from itertools import count

c1 = count()
r1 = range(5)
print(next(c1))
print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)

    
c1 = count(54,5) #inicio em 54, passa de 5 em 5
r1 = range(2,38,5) #inicio em 2, até 38, passa de 5 em 5

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)
