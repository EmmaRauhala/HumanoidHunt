import numpy as np
import csv

# read data (saved as csv)
data = open('data3.csv','r')
data = csv.reader(data, delimiter=',', quotechar='|')


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
#print(matrix)
#print(endpoints)
#print(startpoint)

routematrix = np.zeros((200,200))

def make_step(k):
  for i in range(len(routematrix)):
    for j in range(len(routematrix[i])):
      if routematrix[i][j] == k:
        if i>0 and routematrix[i-1][j] == 0 and matrix[i-1][j] == 0:
          routematrix[i-1][j] = k + 1
        if j>0 and routematrix[i][j-1] == 0 and matrix[i][j-1] == 0:
          routematrix[i][j-1] = k + 1
        if i<len(routematrix)-1 and routematrix[i+1][j] == 0 and matrix[i+1][j] == 0:
          routematrix[i+1][j] = k + 1
        if j<len(routematrix[i])-1 and routematrix[i][j+1] == 0 and matrix[i][j+1] == 0:
           routematrix[i][j+1] = k + 1

# initialize the starting point of the route
routematrix[startpoint[0]][startpoint[1]] = 1

k = 0
while all([routematrix[end[0]][end[1]] == 0 for end in endpoints]):
    k += 1
    make_step(k)

print(all([routematrix[end[0]][end[1]] == 0 for end in endpoints]))

# find the endpoint we ended up in
endpoint = (0,0)
for end in endpoints:
    if routematrix[end[0]][end[1]] != 0:
       endpoint = (end[0],end[1])
       print(endpoint)

i, j = endpoint
k = routematrix[i][j]
path = [(i,j)]
while k > 1:
  if i > 0 and routematrix[i - 1][j] == k-1:
    i, j = i-1, j
    path.append((i, j))
    k-=1
  elif j > 0 and routematrix[i][j - 1] == k-1:
    i, j = i, j-1
    path.append((i, j))
    k-=1
  elif i < len(routematrix) - 1 and routematrix[i + 1][j] == k-1:
    i, j = i+1, j
    path.append((i, j))
    k-=1
  elif j < len(routematrix[i]) - 1 and routematrix[i][j + 1] == k-1:
    i, j = i, j+1
    path.append((i, j))
    k -= 1



path.reverse()

print(path)

instructions = ""

curr = path[0]

for cell in path:
    if cell[0] > curr[0]:
        instructions = instructions + 'R'
    if cell[0] < curr[0]:
        instructions = instructions + 'L'
    if cell[1] > curr[1]:
        instructions = instructions + 'D'
    if cell[1] < curr[1]:
        instructions = instructions + 'U'
    curr = cell

print(instructions)
