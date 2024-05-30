#!/usr/bin/env python3


def return_evens(num_list):
    if not num_list:
        return []
    else:
        return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    if not sentence_list:
        return []  # return empty list is empty
    else:
        return [s + "!" for s in sentence_list]
