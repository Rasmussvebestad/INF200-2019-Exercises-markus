def comp_by_loop(n):
    new_list = []

    for k in range(len(n)):
        if k % 3 == 1:
            new_list.append(n[k] ** 2)

    return (new_list)


def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]