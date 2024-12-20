# Load data
#file = open('day04/test_input.txt').read();
file  = open('day04/input.txt').read();

rows = file.splitlines();

XMAS = 'XMAS';
def isInRange(row, column, word):
    return row < len(rows) and column < len(rows[row]) and row >= 0 and column >= 0;
def isTooSmall(i, word):
    return i < len(word) - 1;
def isTooBig(i, max, word):
    return i > max - len(word);


def searchUp(row, column, word):
    if (isTooSmall(row, word)):
        return False;
    for i in range(len(word)):
        if (rows[row-i][column] != word[i]):
            return False;
    return True;

def searchDown(row, column, word):
    if (isTooBig(row, len(rows), word)):
        return False;
    for i in range(len(word)):
        if (rows[row+i][column] != word[i]):
            return False;
    return True;

def searchRight(row, column, word):
    if (isTooBig(column, len(rows[row]), word)):
        return False;
    for i in range(len(word)):
        if (rows[row][column+i] != word[i]):
            return False;
    return True;

def searchLeft(row, column, word):
    if (isTooSmall(column, word)):
        return False;
    for i in range(len(word)):
        if (rows[row][column-i] != word[i]):
            return False;
    return True;

def searchUpRight(row, column, word):
    if (isTooSmall(row, word) or isTooBig(column, len(rows[row]), word)):
        return False;
    if (not(isInRange(row, column, word))):
        return False;
    for i in range(len(word)):
        if (rows[row-i][column+i] != word[i]):
            return False;
    return True;

def searchUpLeft(row, column, word):
    if (isTooSmall(row, word) or isTooSmall(column, word)):
        return False;
    if (not(isInRange(row, column, word))):
        return False;
    for i in range(len(word)):
        if (rows[row-i][column-i] != word[i]):
            return False;
    return True;

def searchDownRight(row, column, word):
    if (isTooBig(row,len(rows), word) or isTooBig(column,len(rows[row]), word)):
        return False;
    if (not(isInRange(row, column, word))):
        return False;
    for i in range(len(word)):
        if (rows[row+i][column+i] != word[i]):
            return False;
    return True;

def searchDownLeft(row, column, word):
    if (isTooBig(row, len(rows), word) or isTooSmall(column, word)):
        return False;
    if (not(isInRange(row, column, word))):
        return False;
    for i in range(len(word)):
        if (rows[row+i][column-i] != word[i]):
            return False;
    return True;

directions = [searchUp, searchDown, searchLeft, searchRight, searchUpRight, searchUpLeft, searchDownRight, searchDownLeft];

# Search for X
found = 0;
for row in range(len(rows)):
    for column in range(len(rows[row])):
        if rows[row][column] == 'X':
            # print(row, column);
            for direction in directions:
                if (direction(row, column, XMAS)):
                    found += 1;
                   # print("Found", row, column);
print("Found", found);

# Part 2
MAS = 'MAS';
# Search for A
found = 0;
for row in range(len(rows)):
    for column in range(len(rows[row])):
        if rows[row][column] == 'A':
           # print(row, column);
            if ((searchDownRight(row - 1, column - 1, MAS)
                 or searchUpLeft(row + 1, column + 1, MAS))
                 and 
                (searchDownLeft(row - 1, column + 1, MAS) or searchUpRight(row + 1, column - 1, MAS))
                ):
                found += 1;
                #print("Found", row, column);

print("Part 2 Found", found);