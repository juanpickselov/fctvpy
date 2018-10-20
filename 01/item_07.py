list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in list_of_numbers]
squares_too = map(lambda x: x ** 2, list_of_numbers)
even_squares = [x**2 for x in list_of_numbers if x % 2 == 0]
odd_squares = [x**2 for x in list_of_numbers if x % 2 != 0]
print(squares)
print(list(squares_too))
print(even_squares)
print(odd_squares)

