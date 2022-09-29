#Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

from random import random

def rand7():
    return int(random()*7+1)

def rand5():
    return int(random()*5+1)

print(rand7())
print(rand5())