# -*- coding: utf-8 -*-

__author__ = 'Markus Ola Granheim'
__email__ = 'mgranhei@nmbu.no'

# Task A


def bubble_sort(data):
    data = list(data)
    length = len(data) - 1
    for i in range(length):
        for j in range(length - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def test_empty():
    assert bubble_sort([]) == []


def test_single():
    for a in [1, 'alt', 3.1234]:
        assert bubble_sort([a]) == [a]


def test_sorted_is_not_original():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data


def test_original_unchanged():
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    data = [6, 5, 2, 7]
    sorted_data = bubble_sort(data)
    assert bubble_sort(sorted_data) == sorted_data


def test_sort_reversed():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == [1, 2, 3]


def test_sort_all_equal():
    data = [1, 1, 1, 1, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == data


def test_sorting():
    data = ['a', 'a', 'c', 'b', 'a', 'h', 's', 'e']
    assert bubble_sort(data) == ['a', 'a', 'a', 'b', 'c', 'e', 'h', 's']
    data2 = [1.123, 1.1, 1.0001, 2.15, 1.67]
    assert bubble_sort(data2) == [1.0001, 1.1, 1.123, 1.67, 2.15]
    data3 = ['alpha', 'albert', 'agronom', 'a', 'ask', 'at']
    assert bubble_sort(data3) == ['a', 'agronom', 'albert', 'alpha', 'ask', 'at']

