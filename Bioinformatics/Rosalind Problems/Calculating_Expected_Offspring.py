# the inputs are the number of mating pairs of each type
def expectedOffspring(a, b, c, d, e, f):

  # a) AA-AA
  # b) AA-Aa
  # c) AA-aa
  # d) Aa-Aa
  # e) Aa-aa
  # f) aa-aa

  # probability of dominant gene in single offspring from each pairs as per mendells law
  # for this problem it has been calculated manually
  prob_AA = 1
  prob_AA_Aa = 1
  prob_AA_aa = 1
  prob_Aa_Aa = 3/4
  prob_Aa_aa = 1/2
  prob_aa = 0

  # we are given each couple produces exactly two offspring
  E_dom = 2*(prob_AA * a + prob_AA_Aa * b + prob_AA_aa * c + prob_Aa_Aa * d + prob_Aa_aa * e +  prob_aa * f)

  return E_dom

# test case
expectedOffspring(16230, 19580, 17764, 18129, 19555, 16230)

# Output:
# 153896.5
