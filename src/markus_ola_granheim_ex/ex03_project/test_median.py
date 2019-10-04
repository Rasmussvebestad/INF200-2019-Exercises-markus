# -*- coding: utf-8 -*-

__author__ = 'Markus Ola Granheim'
__email__ = 'mgranhei@nmbu.no'

# Importing pytest for the test_empty_list function
import pytest


def median(data):
    sdata = sorted(data)
    n = len(sdata)
    if n % 2 == 1:
        return sdata[n//2]
    elif n == 0:
        raise ValueError
    else:
        return 0.5 * (sdata[n//2 - 1] + sdata[n//2])


def test_one_element():
    assert median([2]) == 2


def test_odd():
    data = [1, 2, 5, 6, 9]
    assert median(data) == 5


def test_even():
    data = [1, 3, 7, 8]
    assert median(data) == 5


def test_ordered():
    data = [1, 5, 9]
    assert median(data) == 5


def test_reversed():
    data = [9, 5, 1]
    assert median(data) == 5


def test_unordered():
    data = [5, 1, 9]
    assert median(data) == 5


def test_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    data = [1, 5, 9]
    median(data)
    assert data == [1, 5, 9]


def test_tuples():
    data = (1, 2, 3, 4, 5)
    assert median(data) == 3
