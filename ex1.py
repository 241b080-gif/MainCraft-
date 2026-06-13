#qus1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
print(f"The sum is: {total}")

#qus2
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

#qus3
n = int(input("Enter a number to find its factorial: "))
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")

#qus4
n_terms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1, end=" ")
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1
    print() # Prints a newline at the end

#qus5
user_string = input("Enter a string to reverse: ")

reversed_string = user_string[::-1]
print(f"Reversed string: {reversed_string}")

#qus6
word = input("Enter a word: ")

# Convert to lowercase to handle capitalization like "Racecar"
clean_word = word.lower()

if clean_word == clean_word[::-1]:
    print(f"'{word}' is a Palindrome.")
else:
    print(f"'{word}' is not a Palindrome.")

#qus7
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#qus8
num = int(input("Enter a number: "))

# Find the number of digits (the power)
order = len(str(num))
temp = num
sum_val = 0

# Calculate the sum of the digits raised to the 'order' power
while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if num == sum_val:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")