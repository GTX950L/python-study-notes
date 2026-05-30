"""
Day 1 — Variables & Data Types
Python has several built-in data types. Here are the most common ones.
"""

# --- Numbers ---
age = 25                  # int (integer)
price = 19.99             # float (decimal)
print(f"I'm {age} years old.")
print(f"This costs ¥{price}")

# --- Strings ---
name = "Python Beginner"
greeting = 'Hello'        # Single or double quotes both work
full = greeting + ", " + name  # String concatenation
print(full)

# --- Booleans ---
is_learning = True
is_expert = False
print(f"Learning: {is_learning}, Expert: {is_expert}")

# --- Type checking ---
print(f"age is type: {type(age)}")
print(f"price is type: {type(price)}")
print(f"name is type: {type(name)}")
print(f"is_learning is type: {type(is_learning)}")
