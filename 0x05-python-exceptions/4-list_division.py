#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    answer = []
    for i in range(list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            answer.append(divide)
    return answer
