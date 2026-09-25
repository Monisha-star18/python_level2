test_number = int(input("Enter a number : "))

original_number = test_number

count = 0
digit_sum = 0
product = 1
reverse = 0

# Number of digits, sum, product and reverse

while test_number > 0:

    digit = test_number % 10

    count += 1
    digit_sum += digit
    product *= digit

    reverse = reverse * 10 + digit

    test_number = test_number // 10


# Even / Odd

if original_number % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"


# Prime / Not Prime
if original_number < 2:
    is_prime = False
else:
    is_prime = True
    i = 2

    while i * i <= original_number:
        if original_number % i == 0:
            is_prime = False
            break

        i += 1


# Palindrome / Not Palindrome

if original_number == reverse:
    palindrome = "Palindrome"
else:
    palindrome = "Not Palindrome"


# Armstrong / Not Armstrong

temp = original_number
armstrong_sum = 0

while temp > 0:

    digit = temp % 10

    armstrong_sum += digit ** count

    temp = temp // 10


if armstrong_sum == original_number:
    armstrong = "Armstrong"
else:
    armstrong = "Not Armstrong"


# Output

print("Number of digits :", count)
print("Sum of digits    :", digit_sum)
print("Product of digits:", product)
print("Reverse          :", reverse)
print("Even/Odd          :", even_odd)
print("Prime/Not Prime   :", "Prime" if is_prime else "Not Prime")
print("Palindrome        :", palindrome)
print("Armstrong         :", armstrong)