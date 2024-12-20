def readInputFile(filename, test=False):
    if (test):
        return open('testData/day' + filename + '.txt').read();
    return open('data/day' + filename + '.txt').read();

def splitStringIntoNumbers(string):
    return [int(x) for x in string.split()]