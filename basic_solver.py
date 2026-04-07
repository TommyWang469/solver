import math

def parse_scientific(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Use formats like: 1.5e3, -2.7E-4, 0.5, 3")

def pick_operation():
    ops = {"1": "add", "2": "subtract", "3": "multiply", "4": "divide", "5": "neg_log", "6": "pow10"}
    print("  Select operation:")
    print("    1. Add")
    print("    2. Subtract")
    print("    3. Multiply")
    print("    4. Divide")
    print("    5. -log(x)")
    print("    6. 10^x")
    while True:
        choice = input("  Enter 1-6: ").strip()
        if choice in ops:
            return ops[choice]
        print("  Invalid choice. Enter 1, 2, 3, 4, 5, or 6.")

def solve():
    print("=== Basic Solver ===\n")

    op = pick_operation()
    print()

    if op == "pow10":
        x = parse_scientific("  x = ")
        print(f"\n  10^x = {10**x:.5e}")
    elif op == "neg_log":
        x = parse_scientific("  x = ")
        if x <= 0:
            print("\n  -log(x) = undefined (x must be greater than 0)")
        else:
            print(f"\n  -log(x) = {-math.log10(x):.5e}")
    else:
        print("Enter two numbers in scientific notation (e.g. 1.5e3, -2.7E-4)\n")
        a = parse_scientific("  a = ")
        b = parse_scientific("  b = ")

        if op == "add":
            print(f"\n  a + b = {a + b:.5e}")
        elif op == "subtract":
            print(f"\n  a - b = {a - b:.5e}")
        elif op == "multiply":
            print(f"\n  a * b = {a * b:.5e}")
        elif op == "divide":
            if b == 0:
                print("\n  a / b = undefined (division by zero)")
            else:
                print(f"\n  a / b = {a / b:.5e}")

while True:
    solve()
    print()
    again = input("Calculate again? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye.")
        break
    print()
