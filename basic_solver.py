def parse_scientific(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Use formats like: 1.5e3, -2.7E-4, 0.5, 3")

def pick_operation():
    ops = {"1": "add", "2": "subtract", "3": "multiply", "4": "divide"}
    print("  Select operation:")
    print("    1. Add")
    print("    2. Subtract")
    print("    3. Multiply")
    print("    4. Divide")
    while True:
        choice = input("  Enter 1-4: ").strip()
        if choice in ops:
            return ops[choice]
        print("  Invalid choice. Enter 1, 2, 3, or 4.")

def solve():
    print("=== Basic Solver ===\n")

    op = pick_operation()
    print()

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
