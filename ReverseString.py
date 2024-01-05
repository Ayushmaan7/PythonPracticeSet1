def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string


original_string = "I am learning Python"
reversed_result = reverse_string(original_string)

print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_result}")