"""
Day 3 — Functions
Reusable blocks of code — define once, use many times.
"""

# --- Basic function ---
def greet(name):
    """Say hello to someone."""  # This is a docstring — documents the function
    return f"Hello, {name}!"

print(greet("World"))
print(greet("Python Learner"))


# --- Function with default parameter ---
def power(base, exponent=2):
    """Raise base to exponent (default: square)."""
    return base ** exponent

print(f"5² = {power(5)}")          # Uses default exponent=2
print(f"2³ = {power(2, 3)}")       # Custom exponent
print(f"10⁴ = {power(10, 4)}")


# --- Function that does something (no return) ---
def print_multiplication_table(n):
    """Print multiplication table for number n."""
    print(f"\nMultiplication table of {n}:")
    for i in range(1, 10):
        print(f"  {n} × {i} = {n * i}")

print_multiplication_table(7)
