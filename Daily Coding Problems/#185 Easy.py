#Given two rectangles on 2D graph, return the area of their intersection
#If no intersection, return 0

# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }

# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3) # width, height
# }

#will return 6

from this import d


class box:
    def __init__(self,num,topleft, bottomright,dims):
        self.num = num
        self.topleft = topleft
        self.bottomright = bottomright
        self.dims = dims

#start by getting inputs
i=0
boxes = [box,box]
top_left = []
dimensions = []

while(i<2):
    boxes[i].num = i
    print("Type in top left corner of rectangle "+ str(i+1))    
    boxes[i].topleft = [int(numstring) for numstring in (input("X,Y seperated by comma:").replace(' ','').split(','))]
    print("Type in length and height of rectangle "+ str(i+1))
    boxes[i].dims = [int(numstring) for numstring in (input("X,Y seperated by comma:").replace(' ','').split(','))]
    i = i+1


box1 = boxes[0]
box2 = boxes[1]

#Find overlap in each direction, x and y, then find their product
#If overlap in one direction is 0, then area is zero.

box1.bottomright = [box1.topleft[0]+box1.dims[0], box1.topleft[1]+box1.dims[1]]
box2.bottomright = [box2.topleft[0]+box2.dims[0], box2.topleft[1]+box2.dims[1]]




mostleft = min(box1.topleft[0],box2.topleft[0])
mosttop = min(box1.topleft[1],box2.topleft[1])
mostright = max(box1.topleft[0]+box1.dims[0],box2.topleft[0]+box2.dims[0])
mostbottom = max(box1.topleft[1]+box1.dims[1],box2.topleft[1]+box2.dims[1])

dx = mostright-mostleft
dy = mostbottom - mosttop

if(dx>=0) and (dy>=0):
    print(dx*dy)
else:
    print(0)

#NOT WORKING YET