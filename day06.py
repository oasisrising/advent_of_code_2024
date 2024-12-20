import re;

# Load data
# file = open('day06/test_input.txt').read();
file  = open('day06/input.txt').read();

rows = file.splitlines();

FACING_UP = '^';
FACING_DOWN = 'v';
FACING_LEFT = '<';
FACING_RIGHT = '>';
FACINGS = [FACING_UP, FACING_RIGHT, FACING_DOWN, FACING_LEFT];
UP = (-1, 0);
DOWN = (1, 0);
LEFT = (0, -1);
RIGHT = (0, 1);
MOVES = [UP, RIGHT, DOWN, LEFT];

x = re.search(r'([\^v<>])', file);

facing = FACINGS.index(x.group());
startingPosition = [0,0,0]; # row, column, facing
occupiedSpaces = set(());
path = [];
    
class Board:
    def __init__(self, board):
        self.rows = board.splitlines();
        
    def __eq__(self, other):
        return self.rows == other.rows;
    
    def __hash__(self):
        return hash(self.rows);
    
    def __str__(self):
        return '\n'.join(self.rows);
    
    def isWall(self, row, column):
        return self.rows[row][column] == '#' or self.rows[row][column] == '0';
    
    def isInbounds(self, row, column):
        return row >= 0 and row < len(self.rows) and column >= 0 and column < len(self.rows[row]);
    
    def placeNewObject(self, position, object):
        rowToChange = self.rows[position[0]];
        self.rows[position[0]] = rowToChange[:position[1]] + object + rowToChange[position[1] + 1:];

    def removeObstacle(self, position):
        rowToChange = self.rows[position[0]];
        self.rows[position[0]] = rowToChange[:position[1]] + '.' + rowToChange[position[1] + 1:];
        
class Guard:
    def __init__(self, row, column, facing):
        self.row = row;
        self.column = column;
        self.facing = facing;
        
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column and self.facing == other.facing;

    def __hash__(self):
        return hash((self.row, self.column, self.facing));
    
    def turn(self):
        self.facing = (self.facing + 1) % len(FACINGS);
        
    def move(self, board):
        newPosition = self.getNextPosition();
        if (board.isInbounds(newPosition[0], newPosition[1]) and board.isWall(newPosition[0], newPosition[1])):
            self.turn();
        else:
            self.row = newPosition[0];
            self.column = newPosition[1];
            
    def getNextPosition(self):
        return [self.row + MOVES[self.facing][0], self.column + MOVES[self.facing][1]];


            
# Process data, find the guard position and direction
for i in range(len(rows)):
    try:
        index = rows[i].index(FACINGS[facing]); 
        print("Guard position: ", i, index);
        startingPosition = [i, index, facing];
        break;
    except:
        continue;
    
def savePosition(guard):
    occupiedSpaces.add((guard.row, guard.column));

def savePath(guard):
    path.append((guard.row, guard.column, guard.facing));   

def Part1():
    guard = Guard(startingPosition[0], startingPosition[1], startingPosition[2]);
    board = Board(file);

    while (board.isInbounds(guard.row, guard.column)):
        savePosition(guard);
        savePath(guard);
        guard.move(board);
    print ("Total: ", len(occupiedSpaces));
    
Part1();

def Part2():
    testSet = {(6,3), (7,6), (7,7), (8,1), (8,3), (9,7)};
    obstacleRecord = set(());
    obstaclesWithLoops = set(());
    
    def savePath(guard, path):
        path.append((guard.row, guard.column, guard.facing));  
    # print (path)
    for i in range(1, len(path)):
        newPath = [];
        # step to the next position
        checkPosition = path[i];
        # has this obstacle been checked?
        if ((checkPosition[0], checkPosition[1]) in obstacleRecord):
            continue;
        
        newObstacle = checkPosition; #path[i];
        
        # is the obstacle on the original guard location?
        if ((newObstacle[0] == startingPosition[0] and newObstacle[1] == startingPosition[1])):
            continue;
        
        obstacleRecord.add((newObstacle[0], newObstacle[1]));
                
        board = Board(file);

        board.placeNewObject(newObstacle, '0');
       # print("Obstacle: ", newObstacle);
        guard = Guard(startingPosition[0], startingPosition[1], startingPosition[2]);
        guard.move(board);
        while (board.isInbounds(guard.row, guard.column)):
            
          #  board.placeNewObject((guard.row, guard.column), FACINGS[guard.facing]);
          #  print("Board state");
          #  print(board)
            try:
                if (newPath.index((guard.row, guard.column, guard.facing))>= 0):
                    # found a loop!
                   # print("Loop at: ", guard.row, guard.column);
                    
                    obstaclesWithLoops.add((newObstacle[0], newObstacle[1]));
                    break;
            except:
                savePath(guard, newPath);
                guard.move(board);
                continue;
        board.placeNewObject(newObstacle, '.');
    print("Total loops: ", len(obstaclesWithLoops));
   # print('Expected: ', testSet);
   # print("Not found: ", testSet.difference(obstaclesWithLoops));
   # print("False positive: ", obstaclesWithLoops.difference(testSet));
Part2();