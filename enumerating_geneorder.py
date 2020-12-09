import itertools
n = 6

l = list(range(1,n+1))
print(len(list(itertools.permutations(l))))
perm = list(itertools.permutations(l))

for i in range(0,len(perm)):
  s = perm[i]
  s = str(s).translate(None, '[],\'')
  s = str(s)[1:-1]
  print(s)