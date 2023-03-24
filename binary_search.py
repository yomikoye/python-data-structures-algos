def binary_search(list, target):
    """
    Return target and index position if found, else return None
    """

    first_element = 0
    last_element = len(list) - 1

    while first_element <= last_element:
        middle_element = (first_element + last_element) // 2
        if list[middle_element] == target:
            return f"target {list[middle_element]} exists at position {middle_element} in the list"
        elif list[middle_element] < target:
            first_element = middle_element + 1
        else:
            last_element = middle_element - 1
    return None

# example
list = [9, 8, 7, 10, 6, 5, 4, 3, 2, 1, 0]
target = 10
target_2 = 17
print(binary_search(sorted(list), target))
print(binary_search(sorted(list), target_2))




