#The probability that two randomly selected mating organisms will produce an 
# individual possessing a dominant allele (and thus displaying the dominant 
# phenotype). Assume that any two organisms can mate.

homo_d = 25 #individuals homozygous dominant
heter = 29 #individuals heterozygous 
homo_r = 23 # individuals homozygous recessive
pop = homo_d + heter + homo_r
mate_pop = pop - 1
mate_heter = heter - 1 
mate_homo_r = homo_r - 1

prob_heter = heter/float(pop)
prob_rec = homo_r/float(pop)
#heter tree
rec_outcome = (prob_heter*(mate_heter/float(mate_pop))*0.25)+(prob_heter*(homo_r/
              float(mate_pop))*0.5)

#recessive tree
rec_outcome = rec_outcome+(prob_rec*(mate_homo_r/float(mate_pop)))+(prob_rec*
              (heter/float(mate_pop)*0.5))


print(1-rec_outcome)