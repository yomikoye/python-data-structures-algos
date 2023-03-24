def linear_search(array, target):
    """
    Return target and index position if found else return None
    """

    for i in range(0, len(array)):
        if array[i] == target:
            return f"target {array[i]} exists at position {i} in the list"
    return None

# example
list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
target = 1
print(linear_search(list, target))