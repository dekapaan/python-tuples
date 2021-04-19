# Exercise
n = int(input("Number of integers to be inserted: "))  # number of values to be added
print("")
numbers = []
for i in range(n):
    numbers.append(int(input("Enter integer: ")))  # adding values to list
numbers = tuple(numbers)  # converting list to tuple
maxi = max(numbers)
mini = min(numbers)
total = sum(numbers)
numbers1 = list(numbers)  # creating new list
for x in range(3):
    numbers1.append(3*(x + 1))  # adding values to new list
numbers1 = tuple(numbers1)  # converting list to tuple
print("")
print("Maximum value of initial tuple:", maxi)
print("Minimum value of initial tuple:", mini)
print("Sum of tuple:", total)
print("")
print("Initial tuple:", numbers)
print("Resulting tuple:", numbers1)
