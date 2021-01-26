import textwrap

data = open('data1.txt','r')
data = data.readlines()
print(data)

for line in data:
    numbers = textwrap.wrap(line, 8)
    numbers = [int(item,2) for item in numbers]
    length = len(numbers)
    i = 0
    ii = []
    while numbers[i] > length-1:
        i = i+1
    while i < length:
        i = numbers[i] 
    
    print(chr(i))


