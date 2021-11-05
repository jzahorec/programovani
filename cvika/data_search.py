import sys

len_input = input().strip().split()

len_data, len_requests = int(len_input[0]), int(len_input[1])

data_requests_input = sys.stdin.read()

number = ""
seps = [" ", "\n"]
data = []
requests = []
i = 0
for char in data_requests_input:
    if char in seps:
        if i < len_data:
            data.append(int(number))
        elif i < len_data + len_requests:
            requests.append(int(number))
        else:
            break
        i += 1
        number = ""
    else:
        number += char

def binary_search(data, searched): # returns mathematical index of searched item or 0
    bottom = 0
    top = len(data) - 1
    if top < 0: # for empty lists
        return 0
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
