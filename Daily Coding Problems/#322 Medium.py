# Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.
# On the ith jump, you may move exactly i places to the left or right.
# Find a path with the fewest number of jumps required to get from 0 to N.

N = 68 #maxes out at about 200 before becoming vastly to large for laptop
jmpSize = 1

class Node:
    def __init__(self, value, side, path):
        self.value = value
        self.side = side
        self.path = path+side
    def get_value(self):
        return self.value
    def get_path(self):
        return self.path

StartingNode = Node(0,'','')
CurrentNodes = [StartingNode]
jmpSize = 1
found = None
treesCreated = 0

while found == None:
    NewLayer = []
    for n in CurrentNodes:
        a = getattr(n,'value')-jmpSize
        b = getattr(n,'value')+jmpSize
        path = getattr(n,'path')
        if(a == N):
            found = path+'M'
            break
        elif(b==N):
            found = path+'A'
            break
        NewLayer.append(Node(a,'M',path))
        NewLayer.append(Node(b,'A',path))    
    CurrentNodes = NewLayer
    jmpSize += 1
    treesCreated += 1
    print(treesCreated,end ="\r")
   
print(found+" = " + str(N))
operations = '0'
jmp = 1

for c in found:
    if c == 'A':
        operations = operations+"+"+str(jmp)
    elif c == 'M':
        operations = operations+"-"+str(jmp)
    jmp += 1
print(operations+" = " + str(N))