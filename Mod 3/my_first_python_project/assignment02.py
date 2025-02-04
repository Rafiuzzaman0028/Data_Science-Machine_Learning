#####  sum all the odd numbers from 0 to 100 and print it to the screen.

sum_of_odds = 0
num = 1

while num <= 100:
    sum_of_odds += num
    num += 2
print("The sum of all ODD numbers from 0 to 100 is :", sum_of_odds)
#
# sum_of_odds = 0
# for i in range (1, 101, 2):
#     sum_of_odds += i
# print("the sum is ", sum_of_odds)