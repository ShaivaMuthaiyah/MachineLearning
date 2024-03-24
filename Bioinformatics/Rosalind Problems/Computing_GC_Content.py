# function to get the gcContent from a sequence
def gcContent(seq):

  # get a rounded value of gc content upto 4 decimal places
  gc_content = round(((seq.count("G") + seq.count("C"))/len(seq)) * 100, 4)

  return gc_content

# example path which was used in google colab
path = "/content/rosalind_gc.txt"

def fastaDictionary(path):
  # open the file to read all the lines as a list
  with open(path, "r") as file:
    fasta = file.readlines()

  # stores a dictionary with labels corresponding to the sequences
  fasta_dict = {}

  # iterate through each item in the list
  for line in fasta:
    # if it stars with a '>' it means it is a label
    if ">" in line:
      fasta_label = line.strip()
      fasta_dict[fasta_label] = ""
    else:
      fasta_dict[fasta_label] += line.strip()

  return fasta_dict

# assign the dictionary to this variable
fasta_dict = fastaDictionary(path)

# function to get the largest gc value from the read fasta file
def largestGC(fasta_dict):

  # create a new dictionary with corresponding labels and gc values
  # call the earlier function for gcContent
  gc_dict = {key: gcContent(value) for key, value in fasta_dict.items()}

  largest = ""
  gc_value = 0

  # get maximum value by iterating through the dictionary
  for key, value in gc_dict.items():
    if gc_dict[key] > gc_value:
      largest = key
      gc_value = gc_dict[key]

  return (largest, gc_value)

print(largestGC(fasta_dict))


# Output: 
# ('>Rosalind_9680', 51.2931)
