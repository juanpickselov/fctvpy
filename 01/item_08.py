the_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in the_matrix for x in row]
squared_matrix = [[x**2 for x in row] for row in the_matrix]
my_lists = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
]

flat_too = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat_too.extend(sublist2)

print(flat)
print(squared_matrix)
print(flat_too)
