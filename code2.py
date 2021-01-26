import collections

# read data
data = open('data2.txt','r')
data = data.read()
#print(data)

# find the single most frequently occurring character = first splitchar
splitchar = collections.Counter(data).most_common(1)[0][0]

# initialize password
password = ''

# until the splitchar is ';' do:
while splitchar != ';':
    
    # add splitchar to password
    password = password + splitchar
    # split the data by the previous most frequent character
    splitted = data.split(splitchar)
    # construct a list of following characters, ignoring empty strings
    candidates = [item[0] for item in splitted if item]
    # find the most frequent one
    splitchar = collections.Counter(candidates).most_common(1)[0][0]
    

print(password)

