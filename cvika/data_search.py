lengths_input = input()
data_input = input()
requests_input = input()

def read_numbers(data, number_count, seps = [" "]):
    i = 0 #count of numbers added to the list
    number = ""
    numbers_list = []
    for char in data:
        if i < number_count:
            if char in seps:
                numbers_list.append(int(number))
                number = ""
                i += 1
            else:
                number += char
        else:
            break
    if i < number_count:
        numbers_list.append(int(number))

    return numbers_list

lengths = read_numbers(lengths_input, 2)
len_data, len_requests = lengths[0], lengths[1]

data = read_numbers(data_input, len_data)


requests = read_numbers(requests_input, len_requests)

def binary_search(data, searched): # returns mathematical index of searched item or 0
    bottom = 0
    top = len(data) - 1
    index = (top + bottom) // 2
    while bottom <= top:
        index = (top + bottom) // 2
        if searched == data[index]:
            while searched == data[index-1] and index > 0:
                index -= 1
            return index + 1
        elif searched >  data[index]:
            bottom = index + 1
        else:
            top = index - 1
    else:
        return 0

for request in requests:
    print(binary_search(data, request), end=" ")
