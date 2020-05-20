""" Nested list comprehensions
list comprehension as the output expression of the overall list comprehension:
[[output expression] for iterator variable in iterable]
"""
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for col in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)



""" Using conditionals in comprehensions
create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string.
"""
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)



""" dictionary """
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = { member:len(member) for member in fellowship }

# Print the new dictionary
print(new_fellowship)












