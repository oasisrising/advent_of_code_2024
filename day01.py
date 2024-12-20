# Load data
file = open('day01/test_input.txt').read();
# file  = open('day01/input.txt').read();
print(file);

lines = file.splitlines();
#print(lines);

list1 = [];
list2 = [];
# Prepare data
for line in lines:
    split = line.split();
   # print(split);
    list1.append(split[0]);
    list2.append(split[1]);

#print(list1);
#print(list2);

# Sort data
list1.sort();
list2.sort();

# print(list1);
# print(list2);

distance = 0;
# Find the distances

for i in range(len(list1)):
    distance += abs(int(list1[i]) - int(list2[i]));

print(distance);

# Part 2
distance = 0;
for i in range(len(list1)):
    count = list2.count(list1[i]);
    distance += count * int(list1[i]);

print(distance);