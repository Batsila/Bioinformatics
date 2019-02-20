import re
file = open("input.txt","r")
gene = file.read()
g_result = re.findall(r'G', gene)
c_result = re.findall(r'C', gene)
gc_result = re.findall(r'GC', gene)
print ("C count: " + str(len(g_result)))
print ("G count: " + str(len(c_result)))
print ("GC count: " + str(len(gc_result)))

