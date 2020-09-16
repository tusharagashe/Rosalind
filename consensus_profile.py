

array = []

fp = open('rosalind_cons.txt', 'r')
lines = fp.readlines()
 
string = ""
first = True
for line in lines:
  if ">" in line:
    if first:
      first = False
      continue
    string = string.replace('\n','')
    array.append(string)
    string = ""
    continue
  string = string + line

print(array)

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

consensus_str = ""

for i in range(len(array[0])):
  consensus_char = 'A'
  common_num = 0
  for pro in map:
    if map[pro][i] > common_num:
      common_num = map[pro][i]
      consensus_char = pro
  consensus_str = consensus_str + consensus_char

if len(consensus_str) == len(array[0]):
  print(consensus_str)


for pro in map:
  print(pro + ":"),
  for i in range(len(array[0])):
    print(map[pro][i]),
  print("")

