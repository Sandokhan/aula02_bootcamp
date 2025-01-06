# Get user name

name = input("Enter your name: ")
while name == "" or any(char.isdigit() for char in name):
    name = input("Invalid name, name could not be empty or have numbers. \nPlease enter a valid name: ")

salary = float(input(f"{name.capitalize()}. What is your salary? "))
while salary == "" or salary < 0:
    salary = input(f"{name.capitalize()} your salary could not be empty or negative. \nPlease enter a valid salary: ")

bonus = float(input(f"{name.capitalize()}. What is your bonus percentage?? "))
while bonus == "" or bonus < 0:
    bonus = input(f"{name.capitalize()} your bonus could not be empty or negative. \nPlease enter a valid salary: ")

print(f"Hello, {name.capitalize()}! Your total salary + bonus is is {int(1000 + (salary * bonus)):.2f}")