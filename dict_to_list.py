
def dict_to_list(the_dict):
    the_list = []
    for i in range(0, len(the_dict.keys())):
        the_list.append(the_dict[i])
    return the_list

# depthfirst_to_suffix = {0: 11, 1: 10, 2: 2, 3: 5, 4: 0, 5: 3, 6: 6, 7: 9, 8: 1, 9: 4, 10: 8, 11: 7}

# print(dict_to_list(depthfirst_to_suffix))