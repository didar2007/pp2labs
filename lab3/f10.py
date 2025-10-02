def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:   
            result.append(item)
    return result