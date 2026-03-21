# Program to calculate average of numbers

numbers = []

for i in range(5):
    num = float(input("Enter number: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)

print("Average is:", average)
