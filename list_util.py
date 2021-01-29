def equals(first_list, second_list):
    result = len(first_list) == len(second_list)
    for a, b in zip(first_list, second_list):
        result &= (a == b)
    return result

def filter_by_list(src_list, filter_list):
    return list(filter(lambda x: x not in filter_list, src_list))

def swap_elements(src_list, first_index, second_index):
    buff = src_list[first_index]
    src_list[first_index] = src_list[second_index]
    src_list[second_index] = buff

def filter_zeros(src_list):
    zero_index = None

    for i in range(len(src_list)):
        if src_list[i] == 0 and zero_index is None:
            zero_index = i
            
        if src_list[i] != 0 and zero_index is not None:
            swap_elements(src_list, i, zero_index)
            zero_index += 1

    for i in range(len(src_list) - zero_index):
        src_list.pop()
    return src_list

    
