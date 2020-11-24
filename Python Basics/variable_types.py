my_integer = 3
my_float = 3.14159
my_string = "Hello"

print(type(my_integer))
print(type(my_float))
print(type(my_string))

#############################################
# Integers

addition = 3 + 2  # 5
print(addition)

subtraction = 3 - 2  # -1
print(subtraction)

multiplication = 3 * 2  # 6
print(multiplication)

division = 11 / 4  # 2.75
print(division)  # division always returns floating point number

floor_division = 11 // 4  # 2
print(floor_division)

modulo = 11 % 4  # 3
print(modulo)
print(floor_division * 4 + modulo)

power = 2 ** 4  # 16
print(power)

power2 = 2.5 ** 3.5
print(power2)

#############################################
# Strings

str_ex = "This doesn\'t matter"
print(str_ex)
str_ex = "This also doesn't matter"
print(str_ex)
str_ex = "These are\ntwo lines"
print(str_ex)

name = "Alice"
fstring = f"Hello {name}. Did you know that 2+2={2 + 2}."
print(fstring)

print("C:\some\name")  # creates a new line
print("C:\some\\name")  # either add another slash
print(r"C:\some\name")  # or add an r before the string

a = "adding "
b = "strings"
print(a + b)

word = "Python"
print(word[0])
print(word[2])
print(word[0:2])
print(len(word))
