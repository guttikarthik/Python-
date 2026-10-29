# Case Study 27: Advanced Numeric Pattern Generator

total_rows = int(input("Enter pattern dimension N (1 to 9): "))

if total_rows < 1 or total_rows > 9:
    print("Invalid dimension! Please enter an integer between 1 and 9.")
else:
    print("\n--- Symmetric Palindromic Number Pyramid ---")
    for current_row in range(1, total_rows + 1):
        # Print leading spaces
        print(" " * (total_rows - current_row), end="")
        
        # Ascending numbers
        for number in range(1, current_row + 1):
            print(number, end="")
            
        # Descending numbers
        for number in range(current_row - 1, 0, -1):
            print(number, end="")
            
        print()  # Move to next line
