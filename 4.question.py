# Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 for salary
def employee(name, salary=9000):
    print(f"El empleado se llama: {name} y tiene un salario de: {salary}")

employee("Elide", 50000)