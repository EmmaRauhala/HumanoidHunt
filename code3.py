import numpy as np
import csv

data = open('data3.csv','r')
data = csv.reader(data, delimiter=',', quotechar='|')

matrix = np.ones((200,200))
endpoints = []

# whatif changes

for line in data:
    x = int(line[0])
    print(x)
    y = int(line[1])
    print(y)
    matrix[x][y] = 0
    for char in line[2:]:
        if char == 'D':
            y = y+1
        if char == 'U':
            y = y-1
        if char == 'R':
            x = x+1
        if char == 'L':
            x = x-1
        if char == 'F':
            endpoints.append((x,y))
        matrix[x][y] = 0
print(matrix)
print(endpoints)

m = np.zeros((200,200))

def make_step(k):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and matrix[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and matrix[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and matrix[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and matrix[i][j+1] == 0:
           m[i][j+1] = k + 1

i,j = 2,2
m[i][j] = 1

k = 0
while all([m[end[0]][end[1]] == 0 for end in endpoints]):
    k += 1
    print(k)
    make_step(k)

print(all([m[end[0]][end[1]] == 0 for end in endpoints]))

#find endpoint
endpoint = (0,0)
for end in endpoints:
    if m[end[0]][end[1]] != 0:
       endpoint = (end[0],end[1])
       print(endpoint)

i, j = endpoint
k = m[i][j]
the_path = [(i,j)]
while k > 1:
  if i > 0 and m[i - 1][j] == k-1:
    i, j = i-1, j
    the_path.append((i, j))
    k-=1
  elif j > 0 and m[i][j - 1] == k-1:
    i, j = i, j-1
    the_path.append((i, j))
    k-=1
  elif i < len(m) - 1 and m[i + 1][j] == k-1:
    i, j = i+1, j
    the_path.append((i, j))
    k-=1
  elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
    i, j = i, j+1
    the_path.append((i, j))
    k -= 1



the_path.reverse()

path = the_path

print(path)

instructions = []

curr = path[0]

for cell in path:
    if cell[0] > curr[0]:
        instructions.append('R')
    if cell[0] < curr[0]:
        instructions.append('L')
    if cell[1] > curr[1]:
        instructions.append('D')
    if cell[1] < curr[1]:
        instructions.append('U')
    curr = cell

print(instructions)
print(''.join(instructions))
text_file = open("Output.txt", "w")

text_file.write(''.join(instructions))

text_file.close()
