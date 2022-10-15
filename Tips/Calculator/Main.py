from optparse import Option
from calculator import *

# Factorial of n using recursion
def main():

    fin = True
    
    while (fin) :
        # Show menú
        menu()
    
        # Get option from console
        option = int(input("Choose an option: "))

        # Verify if input is a valid option
        if option not in range(1, 6):
            print("Please, select a valid option")
            continue

        if (option == 5):
            fin = False
            break
        else:
            n1 = int(input("Indique el primer número: "))
            n2 = int(input("Indique el segundo número: "))
            makeOperation(option, n1, n2)


if __name__ == "__main__":
    main()
