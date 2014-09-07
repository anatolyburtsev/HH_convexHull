__author__ = 'onotole'



def crossProduct(a,b): # if > 0 - counterclockwise; if < 0 - clockwise
    return a[0]*b[1]-a[1]*b[0]

def detectSide(x,y,z): # vector from x to y and point z, if > 0 - left side, < 0 - right side
    if x==y or x==z or y==z: return 0
    a = [y[0]-x[0], y[1]-x[1]]
    b = [z[0]-x[0], z[1]-x[1]]
    if crossProduct(a,b) == 0: return 0
    elif crossProduct(a,b) > 0: return 1
    else: return -1

def lookingForInitialPoint(dict): # the most left point
    x_min = dict[1][0]
    number = 1 #number of min
    for point in dict.items(): #[number, [x,y]]
        if point[1][0] < x_min:
            number =point[0]
            x_min = point[1][0]
    return number

def lookingForNextPoint(dict, currentPoint):
    initialPoint = currentPoint
    nextPoint=0
    for point in dict.items():
        if not nextPoint and (point[0] != initialPoint):
            nextPoint=point[0]
        if nextPoint and detectSide(dict[initialPoint], dict[nextPoint], point[1]) < 0:
            nextPoint = point[0]
    #del dict[currentPoint]
    return nextPoint

def convexHull(points):
    dict=points # save original dict
    initialPoint=lookingForInitialPoint(dict)
    seq=[initialPoint]
    currentPoint=initialPoint
    pointsInHull = 0
    while (currentPoint != initialPoint) or (pointsInHull == 0):
        currentPoint = lookingForNextPoint(dict, currentPoint)
        seq.append(currentPoint)
        pointsInHull += 1
    return (seq[:-1])

def inputData(filename):
    dict={}
    f = open(filename, 'r')
    line=f.readline()
    number=1
    while line != '':
        a,b=line.split()
        dict.update({number:[int(a),int(b)]})
        line=f.readline()
        number+=1
    f.close()
    return dict

if __name__ == "__main__":
    filename="data.txt"
    points=inputData(filename)
    print(convexHull(points))





