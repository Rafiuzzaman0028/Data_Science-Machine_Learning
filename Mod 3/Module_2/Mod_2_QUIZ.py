# salary = 8000
#
# def prinisalary():
#     salary = 12000
#     print("salary:", salary)
#
# prinisalary()
# print("salary:", salary)
#
# def fun1(name, age = 20):
#     print(name, age)
#
# fun1("Emma")
#
# alist = [4, 8, 12, 16, ]
# alist[1:4] = [20, 24, 28, ]
#
# print(alist)
#
# for num in range(-2, -5, -1):
#     print(num, end=',')

def hour_to_minutes(hours):
    minutes = hours * 60
    return minutes
#    return hours * 60

hours = float(input("Enter HOURS: "))
#minutes = hour_to_minutes(hours)
print(f"{hours} hours is equal to {hour_to_minutes(hours)} minutes.")
#print(f"{hours} hours is equal to {minutes} minutes.")