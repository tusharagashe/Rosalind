

array = ["ATCCAGCT", "GGGCAACT", "ATGGATCT", "AAGCAACC", "TTGGAACT",
"ATGCCATT", "ATGGCACT"]

map = {'A' : [0 for _ in range(len(array[0]))], 'C' : [0 for _ in range(len(array[0]))], 
'G' : [0 for _ in range(len(array[0]))], 'T' : [0 for _ in range(len(array[0]))]}

for dna in array:
  count = 0 
  for c in dna:
    if c == 'A':
      map['A'][count] += 1
    if c == 'C':
      map['C'][count] += 1
    if c == 'G':
      map['G'][count] += 1
    if c == 'T':
      map['T'][count] += 1
    count += 1



for pro in map:
  print(map[pro])
