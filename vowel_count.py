

# Program to count vowels in a string

import sys

if len(sys.argv) > 1:
    string = " ".join(sys.argv[1:])
else:
    string = "Hello World"

vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Input String:", string)
print("Number of vowels:", count)
