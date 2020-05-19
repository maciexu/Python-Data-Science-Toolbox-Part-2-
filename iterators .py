""" Iterators vs Iterables
Let's do a quick recall of what you've learned about iterables and iterators. 
Recall from the video that an iterable is an object that can return an iterator, 
while an iterator is an object that keeps state and produces the next value when you call next() on it.
"""
# Example 1
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for x in flash:
    print(x)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))



# Example 2
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3):
    print(i)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10**100))
# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))



""" Iterators as function arguments 
iter() function to get an iterator object, 
next() function to retrieve the values one by one from the iterator object.
list() and sum() functions return a list and the sum of elements, respectively.
"""
# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)



""" enumerate() returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair. """
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)
    
    

""" zip(), which takes any number of iterables and returns a zip object that is an iterator of tuples. 
If you wanted to print the values of a zip object, you can convert it into a list and then print it. 
Printing just a zip object will not return the values unless you unpack it first. 
"""
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)


""" * in a call to zip() to unpack the tuples produced by zip(). """
# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

