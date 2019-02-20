import re
input = open("input.txt", "r")
gene = input.read()
g_result = re.findall(r'G', gene)
c_result = re.findall(r'C', gene)
gc_result = re.findall(r'GC', gene)

output = open("output.txt", "w+")

output.write("C count: " + str(len(g_result)))
output.write("\nG count: " + str(len(c_result)))
output.write("\nGC count: " + str(len(gc_result)))

