import math
def Euclid(src,dst):
    x1=src[0]
    y1=src[1]
    x2=dst[0]
    y2=dst[1]
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
   


def Mahattan(src,dst):
    x1=src[0]
    y1=src[1]
    x2=dst[0]
    y2=dst[1]
    return abs(x1-x2)+abs(y1-y2)