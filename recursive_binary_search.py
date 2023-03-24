def recursive_binary_search(list, target):
    """
    Return target and index position if found, else return None
    """

    if len(list) == 0:
        return False
    else:
        middle_element = len(list) // 2
        
    if list[middle_element] == target:
        return True
    else:
        if list[middle_element] < target:
            return recursive_binary_search(list[middle_element + 1:], target)
        else:
            return recursive_binary_search(list[:middle_element], target)

# example
list = [9, 8, 7, 10, 6, 5, 4, 3, 2, 1, 0]
target = 10
target_2 = 17
print(recursive_binary_search(sorted(list), target))
print(recursive_binary_search(sorted(list), target_2))
