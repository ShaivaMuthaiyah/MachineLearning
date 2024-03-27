# given k is homozygous dominant so AA, m is heterozygous Aa and n is homozygoes recessive aa
def mendelsFirst(k, m, n):

  # total number of organisms
  total = k + m + n

  # also given any two organisms can mate
  # probability of atleast 1 dominant is (1 - probability of both recessive)

  # to get both recessive we need to mate (m x m), (m x n) and (n x n)
  # probability of getting a homozygous recessive is given below
  # (m x m) is 1/4, (n x n) is 1 and (m x n) is 1/2

  # probability of getting the homozygous recessive from each combination
  prob_mxm = ((1/4) * ((m/total) * ((m - 1)/(total - 1))))
  prob_nxn = ((n/total) * ((n - 1)/(total -1)))
  prob_mxn = ((m/total) * (n/(total - 1)))

  # total probability of getting a homozygous recessive organism
  prob_2r =  prob_mxm + prob_nxn + prob_mxn

  # probability of getting organism with atleast 1 dominant gene
  prob_1R2R = round(1 - (prob_2r), 5)

  return prob_1R2R

# test case
mendelsFirst(15, 29, 17)

# Output:
# 0.73552
