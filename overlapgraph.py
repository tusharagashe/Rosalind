#https://gitlab.com/RebelCoder/rosalind-problems/-/blob/master/stronghold/GC_Content.py

def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

FASTAFile = readFile("")
FASTADict = {}
FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

def overlap(FastaDict,k):
  pairs = {}
  

  return 






