########## Printing Numbers ##########
from typing import final

# n = 0
# while n<10:
#     n += 1
#     print(n)

######### Factorial Calculation #########

# num = int(input("Enter your number :"))
#
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = 1
#     while num > 0:
#         result *= num
#         num -= 1
# #    print(f"The factorial of{num} is {result}")
#     print("The Factorial of", num ,"is", result)

####### Fibonacci Sequence ######

# num_terms = int(input("Enter the number of terms: "))
#
# if num_terms <= 0:
#     print("The number of terms must be positive.")
# elif num_terms == 1:
#     print("The Fibonacci sequence for 1 term is : 0")
# else:
#     fib_sequence =[0, 1]
#     while len(fib_sequence) < num_terms:
#         next_term = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_term)
#     print(f"The Fibonacci sequence for {num_terms} terms is: {fib_sequence}")

########## Summation from 1 to n #############

# n = int(input("Enter your number: "))
#
# num = 0
# result = 1
#
# while num <= n:
#     result += num
#     num += 1
#     print("it is", result)
# print("summation is ", result)

########## Sum of Digits ###########

# num = int(input("Enter a number: "))
#
# if num < 0:
#     num = abs(num)
# sum_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_digits += digit
#     num //= 10
#     print(f"The sum of digits of {num} is {sum_digits}")
# #print(f"The sum of digits of {num} is {sum_digits}")

########## Palindrome Check ################

# input_value = str(input("Enter a value to check for palindrome: "))
#
# left = 0
# right = len(input_value) - 1
#
# while left < right:
#     if input_value[left] != input_value[right]:
#         print(f"{input_value} is not a palindrome.")
#         break
#     left += 1
#     right -=1
# else:
#     print(f"{input_value} is a palindrome.")


############# INTERMEDIATE ################

########## GCD calculator #############
 ####### Greatest Common Divisor ########
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second numbe: "))
#
# while num2 != 0:
#     num1, num2 = num2, num1%num2
# print(f"The GCD of {num1} and {num2} is {num1}")

############# PRIME Number check ##############

# num = int(input("Enter a number: "))
#
# if num <= 1:
#     print(num, "is not a prime number.")
# elif num <= 3:
#     print(num, "is a prime number.")
# elif num % 2 == 0 or num % 3 == 0:
#     print(num, "is not a prime number.")
# else:
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             print(num, "is not a prime number.")
#             break
#         i += 6
#     else:
#         print(num, "is a prime number.")

########### Armstrong Number Check ##################
          ##### Interesting ONE ######

# num = int(input("Enter a number: "))
#
# original_num = num
# sum_of_cubes = 0
#
# while num > 0:
#     digit = num % 10
#     sum_of_cubes += digit ** 3
#     num //= 10
# if original_num == sum_of_cubes:
#     print(f"{original_num} is an Armstrong number. ")
# else:
#     print(f"{original_num} is not an Armstrong number.")

######### Reverse a Number ##########

# num = int(input("Enter number to reverse: "))
#
# reverse_num = 0
#
# while num > 0:
#     digit = num % 10
#     reverse_num = reverse_num * 10 + digit
#     num //=10
# print(f"The reversed number is: {reverse_num}")



####### Matrix Multiplication #############
### Multiply two matrices using nested while loops ####


row_A = int(input("Enter the number of rows of matrx A: "))
col_A = int(input("Enter the number of columns of matrix A: "))

matrix_A = []
for i in range(row_A):
    row = []
    for j in range(col_A):
        element = int(input(f"Enter element A[{i}][{j}]: "))
        row.append(element)
    matrix_A.append(row)

row_B = int(input("Enter the number of rows of matrix B: "))
col_B = int(input("Enter the number of columns of matrix B: "))

matrix_B = []
for i in range(row_B):
    row = []
    for j in range(col_B):
        element = int(input(f"Enter element B[{i}][{j}]: "))
        row.append(element)
    matrix_B.append(row)

if col_A != row_B:
    print("Matrix multiplication invalid .The number of columns of A and rows in B must be equal. ")
else:
    result_matrix = []
    for i in range(row_A):
        row = []
        for j in range(col_B):
            element = 0
            k = 0
            while k < col_A:
                element += matrix_A[i][k] * matrix_B[k][j]
                k += 1
            row.append(element)
        result_matrix.append(row)

    print("The result matrix is: ")
    for row in result_matrix:
        print(row)

















