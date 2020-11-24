def greet_user():
    """Generic greeting for users"""
    print("Hello!")
    print("Welcome")


def greet_user_by_name(name="user", greeting="Hello"):
    """Customised greeting"""
    print(f"{greeting}, {name}")


def cube(base_number):
    """Multiplies a number with itself 3 times"""
    cubed_value = base_number**3
    return cubed_value


greet_user()
greet_user_by_name()
greet_user_by_name("Yorugo", "Welcome")
greet_user_by_name(greeting="Welcome", name="Yorugo")
greet_user_by_name(input("What is your name? "))
print(cube(3))