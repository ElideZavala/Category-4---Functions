# Write a function such that it can accept a variable length of argument and print all arguments value

def nombres_con_E(*names):
    for name in names:
        print(name)

nombres_con_E('Elide', 'Eliceo', 'Eliel', 'Efren', 'Emanuel', 'Edgar', 'Ezequiel')