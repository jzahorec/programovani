len_a = int(input())
a = input().strip().split()
len_b = int(input())
b = input().strip().split()

for i in range(len_a):
    a[i] = int(a[i])

for i in range(len_b):
    b[i] = int(b[i])

counter_a = 0
counter_b = 0

for i in range(len_a + len_b):
    if counter_a < len_a and counter_b < len_b:
        if a[counter_a] < b[counter_b]:
            print(a[counter_a], end=" ")
            counter_a += 1
        else:
            print(b[counter_b], end=" ")
            counter_b += 1
    elif counter_a == len_a:
        print(b[counter_b], end=" ")
        counter_b += 1
    else:
        print(a[counter_a], end=" ")
        counter_a += 1
