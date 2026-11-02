def analyze_numbers(numbers):
    print("--- Number Analysis ---")
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")

sample_numbers = [10, 15, 22, 33, 40]

# Calling the function
analyze_numbers(sample_numbers)
print("-----------------------")
print("Practice completed successfully!")