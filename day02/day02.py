# Load data
#file = open('day02/test_input.txt').read();
file  = open('day02/input.txt').read();

lines = file.splitlines();

# Prepare data
safeLines = 0;
def dampen(levels: list[int]):
    for i in range(len(levels)):
        listWithoutI = levels.copy();
        listWithoutI.pop(i);
        if (isSafe(listWithoutI, 1)):
            return True;
    return False;

def isSafe(levels: list[int], dampenLevel = 0):
    ascending = levels[0] < levels[1];
    for i in range(len(levels)-1):
        if ((levels[i] < levels[i+1]) != ascending):
            if (dampenLevel == 0):
                return dampen(levels);
            return False
        distance = abs(levels[i] - levels[i+1]);
        if (distance == 0 or distance > 3):
            print("Too big", levels[i], levels[i+1], levels);
            if (dampenLevel == 0):
                return dampen(levels);
            return False
    if (dampenLevel == 1):
        print("Safe dampen level ", dampenLevel, levels);
    return True;


for line in lines:
    levels = [int(x) for x in line.split()];
  #  print("-------------------------");
    safe = isSafe(levels);

    if safe:
        #print("Safe", levels);
        safeLines += 1;

print("Safe: ", safeLines)

