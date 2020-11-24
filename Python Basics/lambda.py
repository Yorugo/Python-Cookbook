# Small anonymous functions can be created with the lambda keyword.
# Lambda functions can be used wherever function objects are required.

def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(type(f))
print(f(0))
print(f(2))
print(f(3))


# An example in use is the following
# Let's say we want to make a quick function that reads user input
# and it tests to see if it satisfies certain conditions (this is where the lambda is used).
def read(text, tp, conditions, failtext=None):
    """Example:\n
read("firsttext", int, lambda x: x < 10, "lasttext")"""
    inp = input(text)
    while True:
        try:
            inp = tp(inp)
        except ValueError:
            pass
        else:
            if conditions(inp):
                break
        if failtext:
            inp = input(failtext)
        else:
            inp = input(text)
    return inp


opening_text = "What is your favourite positive integer smaller than 10?\nPlease type your integer: "
type_of_input = int
condition = lambda x: 0 < x < 10  # Condition is positive integer smaller than 10.
fail_text = "You did not type in a positive integer smaller than 10.\nPlease type your integer: "
fave_number = read(opening_text, type_of_input, condition, fail_text)
print(fave_number)

# or type in the lambda directly
fave_number = read(opening_text, int, lambda x: 0 < x < 10, fail_text)
print(fave_number)
