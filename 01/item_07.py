list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in list_of_numbers]
print(squares)

squares_too = map(lambda x: x ** 2, list_of_numbers)
print(list(squares_too))
