# Write a recursive function to calculate the sum of numbers from 0 to 10
def recursive(num):
    if (num == 1):
        return  1
    else:
        return num + recursive(num - 1)


result = recursive(10)
print(result)


def calculate_sum(num):
    if num:
        return num + calculate_sum(num - 1)
    else:
        return 0 


result2 = calculate_sum(10)
print(result2)