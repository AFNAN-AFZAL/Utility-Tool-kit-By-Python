import math 

# 1. Addition
def add_numbers(a, b):
    return a + b

# 2. Temperature Converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 3. Even/Odd Checker
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 4. Simple Interest
def calculate_interest(p, r, t):
    return (p * r * t) / 100

# 5. Square Root (Bonus)
def get_square_root(n):
    return math.sqrt(n)

# 6. Multiplication Table (Bonus)
def show_table(n):
    print(f"\n--- Table of {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# --- Main Function (Home Base) ---
def main():
    while True:
        print("\n" + "="*25)
        print("    UTILITY TOOLKIT")
        print("="*25)
        print("1. Add Two Numbers")
        print("2. Celsius to Fahrenheit")
        print("3. Check Even/Odd")
        print("4. Simple Interest")
        print("5. Square Root")
        print("6. Multiplication Table")
        print("7. Exit")
        
        choice = input("\nSelect a tool (1-7): ")

        if choice == "7":
            print("Exiting. Have a great day!")
            break

        try:
            if choice == "1":
                x = float(input("First number: "))
                y = float(input("Second number: "))
                print(f"Result: {add_numbers(x, y)}")

            elif choice == "2":
                c = float(input("Celsius: "))
                print(f"Fahrenheit: {celsius_to_fahrenheit(c)}")

            elif choice == "3":
                num = int(input("Number: "))
                print(f"Result: {check_even_odd(num)}")

            elif choice == "4":
                p = float(input("Principal: "))
                r = float(input("Rate (%): "))
                t = float(input("Time (Years): "))
                print(f"Interest: {calculate_interest(p, r, t)}")

            elif choice == "5":
                val = float(input("Number: "))
                if val < 0:
                    print("Error: Cannot find square root of negative.")
                else:
                    print(f"Square Root: {get_square_root(val)}")

            elif choice == "6":
                num = int(input("Table of: "))
                show_table(num)

            else:
                print("Invalid choice!")

        except ValueError:
            print("Error: Please enter numbers only.")

if __name__ == "__main__":

    main()

