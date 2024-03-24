# function to find hamming distance between two sequences 
def hammingDistance(seq1, seq2):

  # intial distance is 0
  hamming_distance = 0

  # since the length of both of the strings are same we can compare them at each index
  for i in range(0, len(seq1)):

    # increment when we encounter dissimilar elements
    if seq1[i] != seq2[i]:
      hamming_distance += 1

  return hamming_distance

seq1 = "CCAAGGGTCGCCGCGGTTCCTGTGAGACAGGGCGTCCAGTCGTTAAACTGCATCCTTTACGAGGAATGACACGCGTTAGGTGACGAAATACTACAGGGAAGCCCTCACCCTTTCCGGAGCGGTAGTCCCAAAGGGGGCGCACTTCGGACTAGATGATAGCCGACGCTCGTAGTAGCACGATGGGGTTTTGCGACGCGCCACCATTGTAAACCGGCCACCACGATAGATACCTTTTGGCGCATCATCAAAGAACAATAGGAACGTGGAGGCCGCATTTTTGGGTCTTTCTCCGAATAACCTTGGTCCAGGATGAGGTCATGATGGTTAGCGCGCCTGTAGTGCTCTAATCAAATTTCTGGGCAAGCGGGCTAGGTTTATAACTAAAATCTCCTGTACGAGCCGAACCTTACCAGGAGTGGCTGAAGGGTCGCAATGGACTATTATGAGCAATTATGTGAGCGACGCTTAACCCTGCCGGCGGTTAGGAGTATTGCTTCTTTGTACCAATAGTCATTTGCTATTCACCGTAAAGTTAATCTACATTACGGACTGCGGGTTATACGTCCTGCTAGGCGGCTTGCTGGCTAGTCATTGCACCCTCAATTGTTTAAAGAATCCCACTAACTAGAAAACGATTATTGTAGAGATGTGGAAAGTTGTATACCAAATGTAGGGGACCATTTCAATAATATATCGTTAAATATTTAAACAAGCTCGGCTTGGGGTTGATACTGAATTTTGAGTCCACACTTGCGTAACTTCTGATCCTTAATGATAGTGTTAAGGTATGCGCCGCATGGAGGTCTAAATCTAACGAGTAAATACAACTTTACCGGCTGGTACGATTCAGTCACACCAACCCGGAGGCAAAAATATAGAGCCAGCGTTGCTTATGCGAGGCAGCCTGTTTACGGACCGATGCGTCGTCCCTTAGAGGTCCACTGGCTGTGTGCATCCCTACATGGATTATACAACCGTACCTCTACGTGTCTCTGCTGCC"
seq2 = "CTCACCAAGGCCCGGCGATCCGATGGGGGTCGTGAACCCACGCTTACCGGCAGTAGCCTCCAGGAAGGTTCCCGTCTCGACAACGAATTCTGACAGCGATCATATAGTATTTTCCGGATCGGCTAACACGGAGTAGGCCCACCTCCGAGAAGTAGCCATCCCAAGCGCGTAGTGGGAACGCGGGAGTTGGTTGCCGTACATAAGTGTTCATCGGACTTTTCGAAACATAGTTTAGACCGCCCAATCACTATATACGCGTCGCTGATTAGGCGCAGATCGTCGTGTTTCCCGGGATAACATTACAGCGTATTTAAGTGGCGCTTGTCGGCTGGCCTGCGATTTAAAATTTGGATGACAGATGCGGCTACCCTGTTATGTAATTAGTAGACCAGAAACGGGCGGAACGCAGCCAGGAGTCTCTCTCGGGTTGAACTGGACTCTGACGAGGAGAACTTATAATAACAAGAACGTCTGCCCATGGTGGTGACTCTTATTTCTTCGAACCCTTGGTGTTTTGCCAAGAAACCGAGGGCTAGTTTACGGCTCGTACAGACAGCTACTCGTAAAGCCGGTCGCCCTGTTCGCTCACCGCTGGACCCACATGCGTTCCCGGATGCACTCCAATCGCCACACGATCCCAGATGACCCGTGTGCACCAACTTAAGAGTGGAGGTGAACCTTCGCTATAATAGGTCCCTCAAGCGCCGCACAAGTGAGGCCTGGGTGGATTACGGAAGAGAGCCTCCAATCTGGCGCGAGCTCCGCTTCTTAATCAACGCGTCCACCACTGTATAGCCTGCATGTCGAAAACTCCCTTCTCAATACCAATGTAACGGATGGCAAGCTGAACCCATCTGAACCGGGCATAAAGGGCGTGAAGAAGGCTTGTTTCCCTGCTGGGCCCCTCTTAGCGATCAGGAGCATCTACTATTAACGGTTCGTTGGCCTCGTGTACGACTCCGTGGCTCATGCACTTTGGGCTCTACGTCATTAATCTGCT"

hammingDistance(seq1, seq2)

# Output:
# 508
