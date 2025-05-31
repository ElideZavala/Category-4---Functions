# Assign a different name to a function and call it with the new name
def first_name(name):
    return f"Hola Hombre, {name}"

second_name = first_name

result = second_name('Marcos')

print(result)