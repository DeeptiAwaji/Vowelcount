

# Program to count vowels in a string

string = input("Enter a string: ") if __name__ == "__main__" else ""

vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
