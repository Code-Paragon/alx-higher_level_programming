#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists.

    Args:
        my_list_1: can contain any type (integer, string, etc.)
        my_list_2: can contain any type (integer, string, etc.)
        list_length: length of list

    Returns:
         a new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        else:
            new_list.append(div)
        finally:
            continue
    return (new_list)
