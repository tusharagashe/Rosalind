
#probabilities 

offspring_const = 2

num_couples = [17429,17114,19855,19119,16095,16741]


p1 = 1*num_couples[0]*offspring_const
p2 = 1*num_couples[1]*offspring_const
p3 = 1*num_couples[2]*offspring_const
p4 = 0.75*num_couples[3]*offspring_const
p5 = 0.5*num_couples[4]*offspring_const
p6 = 0*num_couples[5]*offspring_const

print(p1+p2+p3+p4+p5+p6)
