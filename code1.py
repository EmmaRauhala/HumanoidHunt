import textwrap #to split the input string into pieces of eight bits

# read data line by line
data = open('data1.txt','r')
data = data.readlines()
#print(data)

# initialize password
password = ""

# for each line do
for line in data:
    eightbit = textwrap.wrap(line, 8)               # split line into pieces of length 8
    numbers = [int(item,2) for item in eightbit]    # convert 8-bit encoding to int
    length = len(numbers)                           # find out the length
    i = 0
    # increase i until first valid byte found                                
    while numbers[i] > length-1:
        i = i+1
    # follow the pointers until a new invalid one occurs
    while i < length:
        i = numbers[i]
    # add the corresponding char to password
    password=password+(chr(i))

print(password)