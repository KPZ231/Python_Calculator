import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.HEADER + "Welcome to the calculator!" + bcolors.ENDC)
num_1 = float(input(bcolors.BOLD + "Enter first number: "))    
num_2 = float(input(bcolors.BOLD + "Enter second number: "))

def runMath():
    # Addition
    print(bcolors.OKBLUE + "Sum: " + bcolors.ENDC + str(num_1 + num_2))
    # Subtraction
    print(bcolors.OKBLUE + "Difference: "+ bcolors.ENDC + str(num_1 - num_2))
    # Multiplication
    print(bcolors.OKBLUE + "Product: "+ bcolors.ENDC + str(num_1 * num_2))
    # Division
    if num_2 == 0:
        print(bcolors.FAIL + "Division: Cannot divide by zero")
    else:
        print(bcolors.OKBLUE + "Quotient: " + bcolors.ENDC + str(num_1 / num_2))
    # Square Root
    print(bcolors.OKBLUE + "Square Root: " + bcolors.ENDC + str(math.sqrt(num_1)))
    print(bcolors.OKBLUE + "Square Root: "+ bcolors.ENDC + str(math.sqrt(num_2)))
    # Cosinus
    print(bcolors.OKBLUE + "Cosinus: "+ bcolors.ENDC + str(math.cos(num_1)))
    print(bcolors.OKBLUE + "Cosinus: "+ bcolors.ENDC + str(math.cos(num_2)))
    # Sinus
    print(bcolors.OKBLUE + "Sinus: "+ bcolors.ENDC + str(math.sin(num_1)))
    print(bcolors.OKBLUE + "Sinus: "+ bcolors.ENDC + str(math.sin(num_2)))
    # Tangent
    print(bcolors.OKBLUE + "Tangent: "+ bcolors.ENDC + str(math.tan(num_1)))
    print(bcolors.OKBLUE + "Tangent: "+ bcolors.ENDC + str(math.tan(num_2)))

    print(bcolors.OKCYAN + "Thank you for using the calculator!")

runMath()
