calci = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
print(calci)

def add(n1,n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiplay(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiplay,
    "/" : divide,
}

def calucalator():
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick the operation: ")
        num2 = float(input("What's the next number?: "))
        Answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {Answer}")

        choice = input(f"Type 'y' to continue calculating with {Answer}, or type 'n' to start a new calculation: ").lower()
        if choice=="y":
            num1 = Answer
        
        else:
            should_continue = False
            print("\n"*20)
            print(calci)
            calucalator()

calucalator()

