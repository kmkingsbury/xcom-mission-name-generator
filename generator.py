from random import randint

nouns = list()
adjectives = list()

#print 'Start Len: '+ str(len(nouns)) + "\n"
with open('adjectives.txt') as f:
    content = f.readlines()
    for x in content:
         y = x.strip()
         adjectives.append(y)

with open('nouns.txt') as f:
    content = f.readlines()
    for x in content:
         y = x.strip()
         nouns.append(y)

this = randint(0,len(adjectives)-1)
that = randint(0,len(nouns)-1)

#print(nouns)
print("Operation " + adjectives[this] + " " + nouns[that])
