###########################################
# Lists

squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])  # but -6 goes out of range
print(squares[-3:])  # slicing a list

# Notice that when assigning lists, it assigns a reference to that list
new_list = squares
new_list[0] = 0
print(squares)  # squares was changed, when we changed new_list

# If we want to copy the list, we do
squares = [1, 4, 9, 16, 25]
new_list = squares[:]
new_list[0] = 0
print(squares)  # squares wasn't change, when we changed new_list

squares2 = [36, 49, 64, 81, 100]
print(squares + squares2)  # list concatenation; doesn't change values of lists
squares.append(squares2[0])  # we can add values to the end of a list
print(squares)

squares = [1, 4, 9, 16, 25]
squares.append(squares2)  # Notice that appending a list to the end, just ads the whole list
print(squares)
squares2[0] = 1
print(squares[5])  # Prints a copy of squares2, when it was appended.

squares = [1, 4, 9, 16, 25]
squares2 = [36, 49, 64, 81, 100]
squares.extend(squares2)  # We can extend squares with squares 2
print(squares)

print(len(squares))

####################
# Other ways to define lists
x = [0] * 10
x[3] = 1
print(x)

x = [2 * n for n in range(10)]
print(x)

# Be careful when defining 2D lists
x = [[0] * 10] * 10
x[0][1] = 1  # This changes the 2nd value of all lists
print(x)

# One way to create a 2D list is
x = [[0 for _ in range(10)] for _ in range(10)]
x[0][1] = 1
print(x)

###########################################
# Dictionaries
age = {'Alice': 24, 'Bob': 29, 'Carol': 20, 'Dave': 20}
print(age['Alice'])
print(age)
del age['Alice']
print(age)
print(list(age))
print('Bob' in age)  # True
print('Alice' in age)  # False
print(20 in age)  # False

squared = {x: x ** 2 for x in (2, 4, 6)}
print(squared)
