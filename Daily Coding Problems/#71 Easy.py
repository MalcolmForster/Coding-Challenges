#Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
#https://stackoverflow.com/questions/137783/expand-a-random-range-from-1-5-to-1-7

from random import random

def rand7():
    return int(random()*7+1)

def rand5():
    vals = [
        [1,2,3,4,5,1,2],
        [3,4,5,1,2,3,4],
        [5,1,2,3,4,5,1],
        [2,3,4,5,1,2,3],
        [4,5,1,2,3,4,5],
        [1,2,3,4,5,1,2],
        [3,4,5,0,0,0,0]
    ]
    result = 0
    while(result ==0):
        i = rand7()
        j = rand7()
        result=vals[i-1][j-1]
    return result

one = 0
two = 0
three = 0
four = 0
five = 0


for i in range(100000):
    ran = rand5()
    if ran == 1:
        one += 1
    if ran == 2:
        two += 1
    if ran == 3:
        three += 1
    if ran == 4:
        four += 1
    if ran == 5:
        five += 1


print("1 : " + str(one) + "| 2 : "+ str(two) +"| 3 : " + str(three) +"| 4 : " + str(four) +"| 5 : " + str(five))