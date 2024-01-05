def find_max_element(lst):
    if not lst:
        return None
    else:
        max_element = lst[0]
        for element in lst:
            if element > max_element:
                max_element = element
        return max_element


number_list = [10, 5, 20, 3, 2, 8, 20, 2]
max_value = find_max_element(number_list)

print(f"The maximum element in the list is: {max_value}")
