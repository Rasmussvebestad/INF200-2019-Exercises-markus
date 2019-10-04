def bubble_sort(data):

    data = list(data)
    length = len(data) - 1
    for i in range(length):
        for j in range(length - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data