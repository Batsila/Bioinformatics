import re

input = open("dna.txt", "r")
output = open("result.txt", "w+")

dna = input.read()
motives_a = re.finditer(r'GC\wGC', dna)

output.write("Motive a in ")
for motive in motives_a:
    output.write(str(motive.start()) + " ")

motives_b = re.finditer(r'ATG[ATGC]{3,1000}[A]{5,10}', dna)

output.write("\nMotive b in ")
for motive in motives_b:
    output.write(str(motive.start()) + " ")

