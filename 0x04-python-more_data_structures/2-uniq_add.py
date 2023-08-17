#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_values = set()
    return sum(num for num in my_list
               if num not in unique_values and not unique_values.add(num))
