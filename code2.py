import collections

data = open('data2.txt','r')
data = data.readline()
#print(data)

first = collections.Counter(data).most_common(1)[0][0]
print(first)
splitword = first
newsplit = '.'
i = 0
while newsplit != ';':
    splitted = data.split(splitword)
    splitted = [x for x in splitted if x]
    candidates = [item[0] for item in splitted]
    newsplit = collections.Counter(candidates).most_common(1)[0][0]
    splitword = newsplit
    print(splitword)
    i = i+1

