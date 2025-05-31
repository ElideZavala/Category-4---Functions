# Generate a Python list of all the even numbers between 4 to 30

def numbers_pars( start, end):
    list = []
    for i in range(start, end):
        if (i > 1 & i % 2 == 0) :
            list.append(i)
    return list

pars = numbers_pars(4, 30)
print(pars)

print("\n****************************************")

print(list(range(4, 30, 2)))