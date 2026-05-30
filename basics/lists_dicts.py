"""
Day 3 — Lists, Tuples & Dictionaries
Python's built-in data structures for organizing data.
"""

# ============================================
#  LISTS — ordered, mutable, allows duplicates
# ============================================
print("=== LISTS ===")
fruits = ["apple", "banana", "orange"]
fruits.append("grape")              # Add to end
fruits.insert(1, "mango")           # Insert at position
fruits.remove("banana")             # Remove by value

print(f"Fruits: {fruits}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}")
print(f"Count: {len(fruits)}")

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle: {numbers[3:7]}")

# ============================================
#  TUPLES — ordered, immutable, allows duplicates
# ============================================
print("\n=== TUPLES ===")
point = (3, 4)
rgb = (255, 128, 64)
print(f"Point: x={point[0]}, y={point[1]}")
print(f"RGB color: {rgb}")
# point[0] = 5  # ← This would ERROR! Tuples can't be changed.

# ============================================
#  DICTIONARIES — key-value pairs
# ============================================
print("\n=== DICTIONARIES ===")
student = {
    "name": "Xiao Ming",
    "age": 22,
    "scores": {"math": 95, "english": 88, "python": 92}
}

print(f"Name: {student['name']}")
print(f"Python score: {student['scores']['python']}")

# Loop through dictionary
print("\nAll scores:")
for subject, score in student['scores'].items():
    print(f"  {subject}: {score}")

# Add/update values
student['grade'] = "A"
print(f"Grade added: {student['grade']}")
