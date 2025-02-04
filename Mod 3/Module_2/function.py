# #### FUNCTION #############
# from zoneinfo import reset_tzpath
#
# from list_practice import numbers, is_pineapple_present
#
#
# # Factorial: Write a function to calculate the factorial of a given number.
# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# num = int(input("Enter factorial: "))
# result = factorial(num)
# print(f"Factorial of {num} is {result}.")
#
# # Fibonacci Sequence: Create a function to generate the Fibonacci sequence up to a given term.
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
#     return fib_sequence
#
# n = int(input("Enter term:"))
# fibonacci_result = fibonacci(n)
# #print(fibonacci_result)
# print(f"The fibonacci series for 10 is {fibonacci_result}")
#
# # prime numbers: Write a function to check if a given number is prime.
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num %2 == 0 or num %3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i ==0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter your number: "))
is_prime_result = is_prime(number)
print(f"{number} is Prime: {is_prime_result}")
