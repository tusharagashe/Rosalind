import math


file = open("/Users/tusharagashe/Desktop/Workspace/rosalind/rosalind_prob.txt",'r')
dna = file.readline()
content = list(map(float, file.readline().split()))

cnt_AT = 0
cnt_CG = 0
GC_prob = 0
AT_prob = 0
logs = []
for nuc in dna:
    if (nuc == 'A' or nuc == 'T'):
      cnt_AT += 1
    elif(nuc == 'C' or nuc == 'G'):
      cnt_CG += 1
for cont in content:
  GC_prob = cont/2
  AT_prob = (1-cont)/2
  logs.append(round(math.log10(((GC_prob)**cnt_CG)*((AT_prob)**cnt_AT)), 3))

logs = str(logs).translate(None, '[],\'')
print logs
