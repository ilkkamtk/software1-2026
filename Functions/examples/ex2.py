from decimal import MIN_ETINY


def filter_list(strings):
    filtered_strings = []

    for string in strings:
        if len(string) > 5:
            filtered_strings.append(string)

    return filtered_strings


animal_names = ["cat", "dog", "elephant", "lion", "giraffe"]

filtered_list = filter_list(animal_names)

print(animal_names)
print(filtered_list)
