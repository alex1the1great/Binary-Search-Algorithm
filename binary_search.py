from random import shuffle

# creating list of numbers from 0 to 9.
numbers_list = [i for i in range(10)]
shuffle(numbers_list)  # shuffle the numbers list.


def binary_search(nums_list, search_number):
    nums_list.sort()  # sort the list

    while nums_list:
        mid_index = len(nums_list) // 2  # find the middle index.
        if nums_list[mid_index] == search_number:
            return True
        elif nums_list[mid_index] > search_number:
            nums_list = nums_list[: mid_index]
        elif nums_list[mid_index] < search_number:
            nums_list = nums_list[mid_index + 1:]
    return False


print(binary_search(numbers_list, 17))


