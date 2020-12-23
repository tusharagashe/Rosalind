from itertools import permutations, product

#implementation from 
# https://github.com/ZhangQiuxue/Rosalind/blob/master/029_SIGN.py

def signedPerm(number):
  signed_ints =[]
  for i in xrange(1, number+1):
	  signed_ints.append([-1*i,i])
  product_list = map(list,list(product(*signed_ints)))
  perm_list = []
  for prod in product_list:
	  perm_list += map(list,list(permutations(prod)))
  print len(perm_list)
  for perms in perm_list:
    print ' '.join(map(str,perms))

signedPerm(3)