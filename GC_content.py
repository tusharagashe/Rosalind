
with open('/Users/tusharagashe/Desktop/Workspace/rosalind/rosalind_gc.txt', 'r') as fp:
  code = ""
  DNA = ""
  content = 0.0
  cnt_CG = 0
  line_cnt = 0
  while True:
    curr_code = fp.readline()
    if len(curr_code) == 0:
      break
    curr_DNA = ""
    char = fp.read(1)
    length = 0
    while char != '>':
      if (char == ''):
        break
      curr_DNA = curr_DNA + char
      char = fp.read(1)
      if char != '\n':
        length += 1
    if (len(curr_DNA) == 0):
      break
    for letter in curr_DNA:
      if (letter == 'C' or letter == 'G'):
        cnt_CG += 1
    curr_content = cnt_CG/float(length)
    if (curr_content > content):
      code = curr_code
      content = curr_content
    cnt_CG = 0
  print(code)
  print(content*100)



