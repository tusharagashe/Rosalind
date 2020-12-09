


months = 2   
life = 3
curr_pair = 1
grown_pair = 0
total_pairs = 1


while (pair < life-1):
  og_pairs = curr_pair
  curr_pair = grown_pair+1
  pair += 1
  total_pairs += pair
  total_pairs = total_pairs-1  

print(total_pairs)