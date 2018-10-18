from urllib.parse import parse_qs


my_values = parse_qs('red=115&blue=12&green=7', keep_blank_values=True)


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


the_red = get_first_int(my_values, 'red')
the_green = get_first_int(my_values, 'green')
the_blue = get_first_int(my_values, 'blue')
print(the_red, the_green, the_blue)
