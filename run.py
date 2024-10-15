def find(tup, elem):
    if elem not in tup:
        return ()

    first_index = tup.index(elem)

    try:
        second_index = tup.index(elem, first_index + 1)

        return tup[first_index:second_index + 1]
    except ValueError:
        return tup[first_index:]


result1 = find((1, 2, 3), 8)
result2 = find((1, 8, 3, 4, 8, 8, 9, 2), 8)
result3 = find((1, 2, 8, 5, 1, 2, 9), 8)

print(result1)
print(result2)
print(result3)