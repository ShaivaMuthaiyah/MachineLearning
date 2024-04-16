def lcsMultiple(sequence_list):
    # let the first item be the base to compare the others with
    base = sequence_list[0]
    n = len(sequence_list)

    # the lcs will be empty to build upon, incase of no lcs we return blank
    lcs = ""

    # iterate over each character in the base
    for i in range(len(base)):
        for j in range(i + len(lcs) + 1, len(base) + 1):
          # the sub is for every possible sub segment from the string
            sub = base[i:j]
            # check if the sub is in all the sequences in the list
            if all(sub in seq for seq in sequence_list[1:]):
              # if it is found update the lcs
                lcs = sub
    return lcs
