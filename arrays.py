new_list = [10, 52, 33, 74, 85, 346, 27, 88, 69]
print(new_list[1:3])
print(new_list[1:])
print(new_list[:3])


if 1 in new_list:
    print("1 exists in the list")
else:
    print("1 does not exist in the list")

for i in range(0, len(new_list)):
    print(i, new_list[i])

