# Simple Calculator in Python

print("---- Simple Calculator ----")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thank you for using the calculator!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if choice == '1':
            print("✅ Result:", num1 + num2)

        elif choice == '2':
            print("✅ Result:", num1 - num2)

        elif choice == '3':
            print("✅ Result:", num1 * num2)

        elif choice == '4':
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!")
            else:
                print("✅ Result:", num1 / num2)
    else:
        print("❌ Invalid choice! Please select from 1 to 5.")
