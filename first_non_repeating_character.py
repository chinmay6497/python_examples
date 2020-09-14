# You are given a string ‘S’ consisting of lowercase Latin Letters. Find the first non repeating character in S. If you find all the characters are repeating print the answer as -1

# Input Description:
# You are given a string ‘s’

# Output Description:
# Print the first non occurring character if possible else -1.

# Sample Input :
# apple
# Sample Output :
# a

def first_non_repeating_character(str):
  char_order = []
  ctr = {}

  for i in str:
    if i in ctr:
      ctr[i] += 1
    else:
      ctr[i] = 1 
      char_order.append(i)
  for i in char_order:
    if ctr[i] == 1:
      return i
  return None

print(first_non_repeating_character("Apple"))