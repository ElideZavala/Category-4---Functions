# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call

def calcualtion(num1, num2):
    sum = num1 + num2
    addition = 0
    if num2 > num1:
        addition = num2 - num1
    else:
        addition = num1 - num2

    return f"La suma es {sum} y la besta es {addition}"

print(calcualtion(21, 23))