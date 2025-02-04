def myfunc(x):
    return len(x)

name = myfunc("Rimon")
print(name)  


# map function

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))



def square(x):
    return x * x

y = map(square, (1, 2, 3, 4))
print(list(y))


input_text = input("Enter: ")
num = input_text.split()

num2 = []
for a in num:
    num2.append(int(a))

result = list(map(square, num2))
print(result)



def myfunc(x):
    if x < 18:
        return False
    else:
        return True

ages = [5, 12, 17, 18, 24, 32]
adults = list(filter(myfunc, ages))
print(adults)