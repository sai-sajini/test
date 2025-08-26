from calculator.operations import add, subtract, multiply, divide

def display_menu():
    print("Simple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ")
        if choice == '1':
            a, b = get_numbers()
            result = add(a, b)
            print(f"Result: {a} + {b} = {result}\n")
        elif choice == '2':
            a, b = get_numbers()
            result = subtract(a, b)
            print(f"Result: {a} - {b} = {result}\n")
        elif choice == '3':
            a, b = get_numbers()
            result = multiply(a, b)
            print(f"Result: {a} * {b} = {result}\n")
        elif choice == '4':
            a, b = get_numbers()
            try:
                result = divide(a, b)
                print(f"Result: {a} / {b} = {result}\n")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.\n")
        elif choice == '5':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.\n")

if __name__ == "__main__":
    main()
