import cmath

def parse_scientific(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Use formats like: 1.5e3, -2.7E-4, 0.5, 3")

def solve():
    print("=== Quadratic Solver: ax² + bx + c = 0 ===")
    print("Enter coefficients in scientific notation (e.g. 1.5e3, -2.7E-4)\n")

    a = parse_scientific("  a = ")
    b = parse_scientific("  b = ")
    c = parse_scientific("  c = ")

    if a == 0:
        print("\nError: 'a' cannot be zero (not a quadratic equation).")
        return

    discriminant = b**2 - 4*a*c
    sqrt_d = cmath.sqrt(discriminant)
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)

    print(f"\n  Discriminant = {discriminant:.5e}")
    print()

    if discriminant > 0:
        print("  Two distinct real roots:")
        print(f"  x1 = {x1.real:.5e}")
        print(f"  x2 = {x2.real:.5e}")
    elif discriminant == 0:
        print("  One repeated real root:")
        print(f"  x  = {x1.real:.5e}")
    else:
        print("  Two complex conjugate roots:")
        print(f"  x1 = {x1.real:.5e} + {x1.imag:.5e}i")
        print(f"  x2 = {x2.real:.5e} + {x2.imag:.5e}i")

while True:
    solve()
    print()
    again = input("Solve another? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye.")
        break
    print()
