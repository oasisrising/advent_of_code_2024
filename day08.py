from utils.utils import *
import re;

file = readInputFile('08');
rows = file.splitlines();
height = len(rows);
width = len(rows[0]);

# process data

def getListOfSignalPositions(row):
    positions = [];
    for i in range(0, len(row)):
        if (row[i] != '.'):
            positions.append(i);
    return positions;

def saveSignal(signal, position, signals):
    if (signal not in signals):
        signals[signal] = [position];
    else:
        signals[signal].append(position);
    return signals;

signals = dict();

# for any alpha/numeric character, add it's coordinate to a dictionary
for i in range(len(rows)):
    result = getListOfSignalPositions(rows[i]);
    for signal in result:
        # print(rows[i][signal], (i, signal), signals);
        saveSignal(rows[i][signal], (i, signal), signals);

        
# print(signals);
def part01():
    anodes = set();
    for signal in signals:
        # calculate the distance between the two points
        locations = signals[signal];
        for i in range(len(locations) - 1):
            for j in range(i + 1, len(locations)):
                distance = getDistance(locations[i], locations[j]);
                # print("Signal: ", signal, "Distance: ",locations[i], locations[j], distance);
                result = addPoints(locations[i], distance);
                if (isInBounds(result, width, height)):
                    anodes.add(result);
                result = subtractPoints(locations[j], distance);
                if (isInBounds(result, width, height)):
                    anodes.add(result);
                    
    print("Anodes: ", len(anodes));
    
part01();

def part02():
    anodes = set();
    for signal in signals:
        # calculate the distance between the two points
        locations = signals[signal];
        for i in range(len(locations) - 1):
            for j in range(i + 1, len(locations)):
                distance = getDistance(locations[i], locations[j]);
                
                # the antenna create anodes
                anodes.add(locations[i]);
                anodes.add(locations[j]);
                
                currentPoint = locations[i];
                while isInBounds(addPoints(currentPoint, distance), width, height):
                    currentPoint = addPoints(currentPoint, distance);
                    anodes.add(currentPoint);
                
                currentPoint = locations[j];
                while isInBounds(subtractPoints(currentPoint, distance), width, height):
                    currentPoint = subtractPoints(currentPoint, distance);
                    anodes.add(currentPoint);
                    
    print("Anodes: ", len(anodes));
    
part02();