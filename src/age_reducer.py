# age_reducer.py
import sys

current_age = None
count = 0

for line in sys.stdin:
    age, num = line.strip().split('\t')
    if age == current_age:
        count += int(num)
    else:
        if current_age:
            print(f"{current_age}\t{count}")
        current_age = age
        count = int(num)

if current_age:
    print(f"{current_age}\t{count}")