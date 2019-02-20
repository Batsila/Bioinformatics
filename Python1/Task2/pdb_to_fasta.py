letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
           'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
           'TYR':'Y','VAL':'V'}
pdb_file = open("frompdb.pdb", "r")
pdb = pdb_file.read()
lines = pdb.split('\n')
prev = '-1'
gene = ""
for line in lines:
    toks = line.split()
    if len(toks)<1: continue
    if toks[0] != 'ATOM': continue
    if toks[3] != prev:
        gene += ('%c' % letters[toks[3]])
    prev = toks[3]

fasta_file = open("tofasta.fasta", "w+")
fasta_file.write(gene)  
