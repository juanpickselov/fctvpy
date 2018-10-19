color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

odds = color_list[::2]
evens = color_list[1::2]
backwards = color_list[::-1]
backwards_by_two = color_list[::-2]
backwards_even = color_list[-2::-2]

print(odds)
print(evens)
print(backwards)
print(backwards_by_two)
print(backwards_even)
