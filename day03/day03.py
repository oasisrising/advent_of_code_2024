import re;

# Load data
# file = open('day03/test_input.txt').read();
file  = open('day03/input.txt').read();

commands = re.findall(r'mul\((\d+),(\d+)\)', file);

# print(commands);

total = 0;
for command in commands:
    total += int(command[0]) * int(command[1]);

print(total);

# Part 2
commands = re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))', file);

# print(commands);

shouldDo = True;

total = 0;
for command in commands:
    cleanCommand = list(filter(lambda x: len(x) > 0,command));
    # print(cleanCommand);
    if (cleanCommand[0] == "do()"):
        shouldDo = True;
    elif (cleanCommand[0] == "don't()"):
        shouldDo = False;
    elif (shouldDo):
        total += int(cleanCommand[0]) * int(cleanCommand[1]);

print(total);