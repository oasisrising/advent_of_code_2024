# Load data
#file = open('day05/test_input.txt').read();
file  = open('day05/input.txt').read();

rows = file.splitlines();

# Process data
rules = [];
updates = [];
isProcessingRules = True;
for row in rows:
    if (row == ''):
        isProcessingRules = False;
        continue;
    if (isProcessingRules):
        rules.append([int(item) for item in row.split('|')]);
    else:
        updates.append([int(item) for item in row.split(',')]);

def isUpdateValid(update, fix=False, numFixed=0):
    for rule in rules:
        try:
            indexOfA = update.index(rule[0]);
            indexOfB = update.index(rule[1]);
            if (indexOfB <= indexOfA):
                if (not fix):
                    return False;
               # print("Invalid update: ", update, "Rule: ", rule);
                update.remove(rule[1]);
                update.insert(indexOfA + 1, rule[1]);
               # print("Fixed update: ", update);
                return isUpdateValid(update, True, numFixed + 1);
        except:
            continue;
    return (fix and numFixed > 0 or not fix)

def Part1():
    total = 0;
    # For each update, find any rules that apply
    for update in updates:
        if (isUpdateValid(update)):
            total += update[int(len(update)/2)];
    print("Total: ", total);
     
def Part2():
    totalFixed = 0;
    for update in updates:
        if (isUpdateValid(update, True)):
            totalFixed += update[int(len(update)/2)];

    print("Total Fixed: ", totalFixed);
       
Part2();