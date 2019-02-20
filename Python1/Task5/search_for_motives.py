import re

input = open("dna.txt", "r")
dna = input.read()
motives = re.finditer(r'GC\wGC', dna)

for motive in motives:
    print (str(motive.start()))
