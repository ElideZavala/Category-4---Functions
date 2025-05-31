# Return the largest item from the given list

list = [4, 6, 8, 24, 12, 2]

def more_big(numbers):
    number_more_big = numbers[0]
    
    for number in numbers:
            if number > number_more_big:
                number_more_big = number
    
    return number_more_big

print(more_big(list))
# more_big(list)
