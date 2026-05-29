name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Age category using conditionals
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 50:
    category = "an adult"
else:
    category = "a senior"

# Personalized message
print(f"\nHello {name}!")
print(f"You are {age} years old, which means you are {category}.")
print(f"It's cool that you enjoy {hobby}. Keep it up!")
