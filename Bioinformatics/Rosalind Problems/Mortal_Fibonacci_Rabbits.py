def mortalRabbits(months, lifespan):

  # create a set of rows and columns where rows are months and ages are the columns
  df = [[0]*lifespan for _ in range(0, months)]

  # set the intial condition where we have a pair of newborn rabbits in the 0th (first) month
  df[0][0] = 1

  # we start from the 2nd month as we filled for the first month
  for month in range(1, months):
    for each_age in range(0, lifespan):

      # if age is of a newborn we need to update it with the number
      if each_age == 0:
        # since only mature rabbits can reproduce it will be filled with rabbit offspring from parents
        # who are 1 and 2 month old so we choose from 1st index as 1: avoids the newborn
        df[month][each_age] = sum(df[month -1][1:])
      
      # if the age the same as the lifespan then it will die in the next cycle
      # we need to remove the ones that are at max lifespan and replace them with ones which are a year younger
      # since we look at index from 0 we consider the max age as lifespan - 1
      elif each_age == lifespan - 1:
        df[month][each_age] = df[month - 1][each_age - 1]

      # for other cases we update the current entry with the previous entry as the age increases by 1
      # if we have the age 1 column we need to update the number with the rabbits who are age 0
      else:
        df[month][each_age] = df[month - 1][each_age - 1]

  # return total number of pairs at the end it will be the last row
  return sum(df[-1])


mortalRabbits(85, 20)

# Output:
# 259182962981517626
