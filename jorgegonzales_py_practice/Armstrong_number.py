# Armstrong Number
#
#     Learn about armstrong numbers here.
#     Define a function that allows the user to check whether a given number is armstrong number or not.
#     Hint: To do this, first determine the number of digits of the given number. Call that n. Then take every digit in the number and raise it to the nth power. Add them, and if your answer is the original number then it is an Armstrong number.
#     Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634. So 1634 is an Armstrong number.
#     Tip: All single digit numbers are Armstrong numbers.


def armstrong_number(n):
    digits_sum = 0
    for number in str(n)[:]:  # we go through all digits in number
        digits_sum += int(number) ** len(str(n))  # we summarize numbers in power of number's length
    return "YES" if n // 10 == 0 or n == digits_sum else "NO"  # all 1 digit numbers are armstrong's numbers


while True:
    print("Please enter a number to check(must be integer)")
    n = input()
    try:
        val = int(n)
        break
    except ValueError:
        print("Wrong input type, input  is:", n)

print(armstrong_number(val))
