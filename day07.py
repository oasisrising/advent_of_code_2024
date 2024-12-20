from utils.utils import *

def multiply(x, y):
    return x * y;

def add(x, y):
    return x + y;

def concat(x, y):
    return int(str(x) + str(y));

file = readInputFile('07');

rows = file.splitlines();

operators = [multiply, add, concat];

def calculateTotalPart01(total, input, expectedOutput):
    # base case
    if (len(input) == 0):
        return total == expectedOutput;
    
    return (calculateTotalPart01(operators[0](total, input[0]), input[1:], expectedOutput) or calculateTotalPart01(operators[1](total, input[0]), input[1:], expectedOutput));

def part1():
    total = 0;
    for row in rows:
        parts = row.split(': ')
        expectedOutput = int(parts[0]);
        input = splitStringIntoNumbers(parts[1]);

        if (calculateTotalPart01(input[0], input[1:], expectedOutput)):
            total += expectedOutput;
            
    print("Total: ", total);

part1();

def calculateTotalPart02(total, input, expectedOutput):
    # base case
    if (len(input) == 0):
        return total == expectedOutput;
    
    return (calculateTotalPart02(operators[0](total, input[0]), input[1:], expectedOutput) or calculateTotalPart02(operators[1](total, input[0]), input[1:], expectedOutput) or calculateTotalPart02(operators[2](total, input[0]), input[1:], expectedOutput));

def part2():
    total = 0;
    for row in rows:
        parts = row.split(': ')
        expectedOutput = int(parts[0]);
        input = splitStringIntoNumbers(parts[1]);

        if (calculateTotalPart02(input[0], input[1:], expectedOutput)):
            total += expectedOutput;
            
    print("Total part 2: ", total);
    
part2();