# age_mapper.py
import sys

for line in sys.stdin:
    if "age" in line:  # Skip header
        continue
    age = line.split(',')[2]  # Assuming age is 3rd column
    print(f"{age}\t1")