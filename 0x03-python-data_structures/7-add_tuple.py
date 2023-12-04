#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    answer = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    answer1 = tuple_1[0] + tuple_2[0]
    answer2 = tuple_1[1] + tuple_2[1]
    answer = answer1, answer2
    return answer
