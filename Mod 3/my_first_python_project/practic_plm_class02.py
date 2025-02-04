# ####    Make a program that receives an integer "n",
# #####   calculate the sum of 1 to n, then shows the sum.
#
# n = int(input("Enter integer n:"))
#
# num = 1
# total = 0
#
# while num <= n:
#     total = total + num
#     num = num + 1
#     print("sum of all ", total)
#
# print("sum of 1 to", n ,"is", total)


##### Make a program that takes numbers until it finds zero.
##### Shows the result of multiplication of all the numbers taken.

#n = int(input("Enter your Number :"))

product = 1

while True:
    num = int(input("Enter your number(0 to stop):"))
    if num == 0:
        break
    product *= num
print("The product of all entered number :", product)

# num1 = int(input("Enter a number:"))
# product = num1
#
# while True:
#     num2 = int(input("Enter number (o to stop):"))
#     if num2 == 0:
#         break
#     product *= num2
# print("The product is", product)