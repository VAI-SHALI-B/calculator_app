def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

"""def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b"""

def main():
    print("=== Menu Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    #print("3. Multiplication") # Added in Push 2
    #print("4. Division")       # Added in Push 2
    
    choice = input("Select operation (1/2/3/4): ").strip()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        """elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")"""
        else:
            print("Invalid option selected.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
