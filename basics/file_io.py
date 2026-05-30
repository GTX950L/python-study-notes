"""
Day 4 — File I/O (Input/Output)
Reading from and writing to files.
"""
import os

# ============================================
#  WRITING to a file
# ============================================
filename = "sample_notes.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("Python Learning Notes\n")
    f.write("=====================\n")
    f.write("Day 1: Hello World, Variables\n")
    f.write("Day 2: Conditions, Loops\n")
    f.write("Day 3: Functions, Data Structures\n")
    f.write("Day 4: File I/O\n")

print(f"✅ Written to '{filename}'")

# ============================================
#  READING from a file
# ============================================
print(f"\n--- Contents of '{filename}' ---")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line.strip()}")  # strip() removes trailing newline

# ============================================
#  APPENDING to a file
# ============================================
with open(filename, "a", encoding="utf-8") as f:
    f.write("Day 5: Coming soon...\n")

print(f"\n✅ Appended to '{filename}'")

# ============================================
#  Read all lines at once
# ============================================
with open(filename, "r", encoding="utf-8") as f:
    all_lines = f.readlines()
    print(f"\nTotal lines: {len(all_lines)}")

# Clean up — delete the test file
os.remove(filename)
print(f"🗑️  Deleted '{filename}' (clean up)")
