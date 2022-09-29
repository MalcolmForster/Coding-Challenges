# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
# answer taken from https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
# was out of my comfort zone and uses different items such as << (bitshift) and yield

numset = [1,2,3,4,5,6,7]
output = [[]]

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]        
    
print(list(powerset(numset)))