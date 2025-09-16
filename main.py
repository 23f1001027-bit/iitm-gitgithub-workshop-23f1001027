from sum import add
from difference import subtract
from product import multiply
from division import divide

def main():
    print("Welcome to Arithmetic Calculator!")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"Sum: {add(a, b)}")
    print(f"Difference: {subtract(a, b)}")
    print(f"Product: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")

if __name__ == "__main__":
    main()
