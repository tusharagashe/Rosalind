

s = "GTTTATAACTGGTTGCCCGCTGATATGGGTGCAATGCCCGTTGCACACAGCTACTACTCCGATCCTTATAAATGCTCAGGAGCTATAACCTGATCAACCTATGCCTAGCTAGTCCTTACATGGATCAGACGGCTTGCTGGTGGTAGACAATCGAGGCAGATCACTTTTATGTTAGACCCCATGTTGGGATGCTCTCTGGAGACTGTTACCTAATAGGTCCTTCAAGTCTACGGATCAAAGTCGCGCTGACCCTATTTCGGTAGGAACGATAGTTGCGTTATGGCTGAGGCTGTTGCAGCCTGTCTTAATGTGCCGGCGGTACGTATCATCTCCCGAAACTCTGTATTGTTACGAGGTGGGGTTACTACCACCCAGTGGAACCGTCCAGAGGGTTGTCGAGGCTCTTGACCGATCTATAAGTGCGGAAGGATATGATCCCTTCCTTGACACCGTGGAATGGAATCCGTACGACTTTCCGTCGGCGCCAAAGACGTTCGCATGTTGGGTCGCTAAATGCATACACGTAAAGCTTTATTCTCACGGCGACCCCACTTGCACCGTGGCGGTTCTGTCAACGAGAAGTAAGCCCCGTGATGACTGGTAGTGAGCCCATGACGTTTCCTAAGCACATTCGAAGAAAGAGCAGATAGGCGGTTTCTCACAGGTTGAAGGACCAGATCCGAGTGCGGATGTTACCCCAATACGCCAGCGGGCCTGAGTTCTGTGTACGTAATCATAAATCATACATATCAATAAGAGTGCCATTAACACGGGGACTTAGAGTTGGGATACATTCGCGTATTGGGACGCAACCACCGCCGCTCAACTTTAACTTCAGGGGCTGAAGGATGGTAATCTCCTAATCGACCGATTGCATTAAAGTAATCGTTTTGCCGCTTACGTCGTCCCACAGTAAAGCAGCAATTGTCTGGAGCGGACTTTTCTTTGATCTCGGCCTG"
s1 = "GTTGGTGACTGGCTGTTCGATTATATCGTAACGCCGTGCCTAGCACGCGGCTGATCATAGGTTCCTGTAAACTGGTCATGTCTTAAACCCAGATAAATCCAGCCATGGCCGCTCCAAACCTGCATGTCCGGGGTTGTAGGCTGACGACAAGAGCGGCAACTAACCACTATCGCGGAACGTGGACAGATATGCTCTACTGGGGTTAAAGCCCGAGGGCTATAAAACCCATCAGATTCACCGTACCGACGAGCATATTTGTGTAGGAACGATACGTGCGTATGGGCTTACGTTCTGGCAGCGTGTCTTAATGGCCCTGGTTTATGGATGATCGATCGAATCTGAGTATTTTGACCAGGACCTGTCTCAAGCATGCCTAGGGTCTCTTAAGTAGGAAGCTATATCAATCCCTCTATCACTCACCCCGCTACCAGAAAAGCAGGTCCGATCCATTTTAGAATATAATCCGTCCGAATAGCGCTGTGCGAAAAATGCATTCGTACGTTGAGCATCTGTAATTCAAGAAGCATGGGACAATTCCGACGGTTCTAGGATTACGTCGGCGGCGGATCATTGCACGGACAGTTCTGCCTGCGCGCACTAGAATAGAGATCTGGCTTGTTCTTAGGGTAGCGCGTAGTAGGGTCAATGTGAAGACTTTTACCAAAATAAAGGTCAAGTGCAGTATTGATATGGTACCAAAATAGGTCAGCGCGCGCCCAGGCGCTGAGGCTCCATATAAATCGTGTATGTCAACCTCAGGGTGAGTTTCACATTTCCATAGGGCTTCGTTACGTTCGAGTCATGGCAAGCAACCGCCCTTGATCGGCTTTTTCTACAGAGATTACATGGACCTTAGCTCCAGATAGGGAGTTTGCTTTGACCTAGACGCCTTATATCTCTCGCACATTCAGATCACTACATCAATTACCTTCTGCAGAACTCTGATTGTGGCCGCCCTG"

count = 0;

if s == s1:
  print 0;

for x in range(0, len(s)):
  if s[x] != s1[x]:
    count += 1
  

print(count);


