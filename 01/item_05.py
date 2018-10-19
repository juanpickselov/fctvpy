# Know how to slice sequences
the_string = "honda accord"
the_list = ['h', 'o', 'n', 'd', 'a', ' ', 'a', 'c', 'c', 'o', 'r', 'd']
for n in range(13):
    print(the_string[:n])
    print(the_list[:n])

print('To reverse a string use -1 for step: ' + the_string[::-1])
print('To reverse a list use -1 for step: ' + str(the_list[::-1]))

for x in range(13):
    print(the_string[x:])
    print(the_list[x:])

print('Some random slices')
print(the_string[:-1])
print(the_list[:-1])

print(the_string[4:])
print(the_list[4:])

print(the_string[-3:])
print(the_list[-3:])

print(the_string[2:5])
print(the_list[2:5])

print(the_string[2:-1])
print(the_list[2:-1])

print(the_string[-3:-1])
print(the_list[-3:-1])