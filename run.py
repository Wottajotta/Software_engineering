values = [0, 2, 4, 6, 8, 10]
string = 'hello'
memory = string
counter = 0

while counter != 10:
    if counter in values:
        print(memory)

    if 'world' not in string:
        string = string + ' world'

    if counter > 7:
        print(string + memory)
    else:
        print(string)

    counter += 1