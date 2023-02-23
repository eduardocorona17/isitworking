for value in range(1, 5):
    print(value)
for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers) 
even_nums = list(range(2, 11, 2))
print(even_nums)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

oddies = [value for value in range(1, 21, 2)]
print(oddies)

cubos = [value ** 3 for value in range(1, 11)]
print(cubos)