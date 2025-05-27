"""
Create an inner function to calculate the addition in the following way:
    Create an outer function that will accept two parameters, a and b
    Create an inner function inside the outer function that will calculate the addition of a and b
    At last, the outer function will add 5 to the addition and return it
"""

def outer_func(a, b):

    def inner_func(a, b):
        return a + b
    
    add = inner_func(a, b)
    return add + 5

result = outer_func(5, 10)
print(result)



# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x + factorial(x - 1))
    
# # x ira disminuyendo
# # x + return del resultado de la suma, hasta llegar a 1
    
# print(factorial(4)) # 12, 6, 2, 1