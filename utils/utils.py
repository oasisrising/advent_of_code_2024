def readInputFile(filename, test=False):
    if (test):
        return open('testData/day' + filename + '.txt').read();
    return open('data/day' + filename + '.txt').read();

def splitStringIntoNumbers(string):
    return [int(x) for x in string.split()]

def getDistance(pointA, pointB):
    return (pointA[0] - pointB[0], pointA[1] - pointB[1]);

def addPoints(pointA, pointB):
    return (pointA[0] + pointB[0], pointA[1] + pointB[1]);

def subtractPoints(pointA, pointB):
    return (pointA[0] - pointB[0], pointA[1] - pointB[1]);

def isInBounds(point, width, height):
    return point[0] >= 0 and point[0] < height and point[1] >= 0 and point[1] < width;