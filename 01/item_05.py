# Know how to slice sequences
the_string = "honda accord"

for n in range(13):
    print(the_string[:n])
print('To reverse a string use -1 for step: ' + the_string[::-1])
for x in range(13):
    print(the_string[x:])
print('Some random slices')
print(the_string[:-1])
print(the_string[4:])
print(the_string[-3:])
print(the_string[2:5])
print(the_string[2:-1])
print(the_string[-3:-1])
