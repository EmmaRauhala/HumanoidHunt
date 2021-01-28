import numpy as np
from math import sqrt, inf
import csv
from queue import PriorityQueue

# read data (saved as csv)
data = open('data3.csv','r')
data = csv.reader(data, delimiter=',', quotechar='|')

# here, assuming tha size of the maze is not greater than 200x200
matrix = np.ones((200,200))
startpoint = tuple()
endpoints = []

# go through all the neural strands constructing a binary matrix representing possible routes
# please note that here zeros represent routes/connections and ones represent "walls" 
for line in data:

    # starting point
    x = int(line[0])
    y = int(line[1])
    matrix[x][y] = 0

    # following the directions
    for char in line[2:]:
        if char == 'D':
            y = y+1
        elif char == 'U':
            y = y-1
        elif char == 'R':
            x = x+1
        elif char == 'L':
            x = x-1
        # listing also the endpoints
        elif char == 'F':
            endpoints.append((x,y))
        # and finding the starting point
        elif char == 'S':
            startpoint = (x,y)
        # adding resulting routes to the matrix    
        matrix[x][y] = 0

# find out if a state is a goal state
def isgoal(loc:tuple):
    return loc in endpoints

# find out the possible successor-states of a state
def successors(loc:tuple):
    x,y = loc
    succ = []
    for i in [('R',(x+1,y)),('L',(x-1,y)),('D',(x,y+1)),('U',(x,y-1))]:
        if matrix[i[1][0]][i[1][1]]==0:
            succ.append(i)
    return succ

################## Using the A* algorithm to find an optimal solution ##################

# Heuristic function: euclidean distance to the closest goal state
def h(loc:tuple):
    x,y = loc
    return min(list(map(lambda z: sqrt((x-z[0])**2 + (y-z[1])**2),endpoints)))

predecessor = {} 
g = {}
Q = PriorityQueue()

def f(state):
    return g[state] + h(state)

# Initialize best cost with inf
shortest_length = inf
shortest_end = None

# Starting state:
s = startpoint

# Put start state in queue
Q.put((h(s),s))

# and in g and predecessor
g[s] = 0
predecessor[s]=(None,None)

# While the queue is non-empty do:
while not Q.empty():

    curr = Q.get()[1]

    if f(curr) < shortest_length:

        for act,succ in successors(curr):

            if ((not succ in g) or ((g[curr]+ 1) < g[succ])):
                g[succ]=g[curr]+ 1
                predecessor[succ] = (act,curr)

                if not isgoal(succ):
                    Q.put((f(succ),succ))

                elif g[succ]<shortest_length:
                    shortest_length = g[succ]
                    shortest_end = succ

actions = ''

if shortest_end is not None:

    currstate = shortest_end
    
    while currstate != s:
        action = predecessor[currstate][0]
        actions= action+actions
        currstate = predecessor[currstate][1]


print(actions)
