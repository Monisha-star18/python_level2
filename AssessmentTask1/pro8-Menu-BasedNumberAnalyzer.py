number = int(input("Enter a number: "))

while True:

    print()
    print("===== NUMBER ANALYZER =====")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Palindrome")
    print("4. Check Armstrong")
    print("5. Reverse Number")
    print("6. Sum of Digits")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            if number % 2 == 0:
                print("The number is Even")
            else:
                print("The number is Odd")

        case 2:
            if number < 2:
                is_prime = False
            else:
                is_prime = True
                i = 2

                while i * i <= number:
                    if number % i == 0:
                        is_prime = False
                        break

                    i += 1

            if is_prime:
                print("The number is Prime")
            else:
                print("The number is Not Prime")

        case 3:
            original_number = number
            temporary_number = number
            reverse = 0

            if number < 0:
                print("The number is Not Palindrome")
            else:
                while temporary_number > 0:
                    digit = temporary_number % 10
                    reverse = reverse * 10 + digit
                    temporary_number = temporary_number // 10

                if original_number == reverse:
                    print("The number is Palindrome")
                else:
                    print("The number is Not Palindrome")

        case 4:
            original_number = number
            temporary_number = number
            digit_count = 0
            armstrong_sum = 0

            if number < 0:
                print("The number is Not Armstrong")
            else:
                if temporary_number == 0:
                    digit_count = 1
                else:
                    while temporary_number > 0:
                        digit_count += 1
                        temporary_number = temporary_number // 10

                temporary_number = number

                while temporary_number > 0:
                    digit = temporary_number % 10
                    armstrong_sum += digit ** digit_count
                    temporary_number = temporary_number // 10

                if armstrong_sum == original_number:
                    print("The number is Armstrong")
                else:
                    print("The number is Not Armstrong")

        case 5:
            temporary_number = number
            reverse = 0

            if temporary_number < 0:
                temporary_number = -temporary_number

                while temporary_number > 0:
                    digit = temporary_number % 10
                    reverse = reverse * 10 + digit
                    temporary_number = temporary_number // 10

                reverse = -reverse
            else:
                while temporary_number > 0:
                    digit = temporary_number % 10
                    reverse = reverse * 10 + digit
                    temporary_number = temporary_number // 10

            print("Reverse Number:", reverse)

        case 6:
            temporary_number = number
            digit_sum = 0

            if temporary_number < 0:
                temporary_number = -temporary_number

            while temporary_number > 0:
                digit = temporary_number % 10
                digit_sum += digit
                temporary_number = temporary_number // 10

            print("Sum of Digits:", digit_sum)

        case 7:
            print("Thank you for using Number Analyzer!")
            break

        case _:
            print("Invalid choice. Please select 1-7.")