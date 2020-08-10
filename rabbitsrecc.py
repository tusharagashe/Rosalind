

n = 31   
k = 4
g_pairs = 1
i = 2
t_pairs = 1

while (i < n):
  og_pairs = t_pairs
  t_pairs = (g_pairs*k) + t_pairs
  g_pairs = og_pairs
  i += 1


print(t_pairs)