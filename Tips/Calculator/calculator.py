# Menu Calculator
def menu():
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def makeOperation(opt, fn, sn):
    match opt:
        case 1:
            print(f"Resultado: {fn} + {sn} = {add(fn, sn)}")
            
        case 2:
            print(f"Resultado: {fn} - {sn} = {substract(fn, sn)}")
            
        case 3:
            print(f"Resultado: {fn} * {sn} = {multiply(fn, sn)}")
            
        case 4:
            print(f"Resultado: {fn} / {sn} = {divide(fn, sn)}")
            
        case 5:
            return

# Functions 
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2