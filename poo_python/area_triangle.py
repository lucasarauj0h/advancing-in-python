from entities import Triangle
import random
import math

x = Triangle
x.a = random.randrange(1,10)
# print(x.a)
x.b = random.randrange(1,10)
# print(x.b)
x.c = random.randrange(1,10)
# print(x.c)
p = (x.a+x.b+x.c)/2
# print(p)
# result = math.sqrt(p*(p-x.a)*(p-x.b)*(p-x.c));
# print(result)
print(x.area())