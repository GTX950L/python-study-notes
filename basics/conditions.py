"""
Day 2 — Conditional Statements
if / elif / else — making decisions in code.
"""

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# --- Comparison operators ---
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to

# --- Logical operators ---
# and   both must be True
# or    at least one must be True
# not   reverses True/False

age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive! 🚗")
else:
    print("You cannot drive yet.")
