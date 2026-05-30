"""
Day 2 — Loops
for loops and while loops — repeating things efficiently.
"""

# --- for loop with range ---
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# --- for loop with a list ---
print("\nFruits I like:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"  - {fruit}")

# --- while loop ---
print("\nCountdown:")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Blast off! 🚀")

# --- break and continue ---
print("\nFirst 5 even numbers:")
found = 0
num = 0
while True:
    if num % 2 == 0:
        print(f"  {num}")
        found += 1
    if found >= 5:
        break
    num += 1
