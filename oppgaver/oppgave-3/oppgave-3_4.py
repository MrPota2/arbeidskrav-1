def number_multiplication(first_num: int, second_num: int) -> int:
    return first_num * second_num

def verify_multiplication(function, expected_result) -> bool:
    return True if function == expected_result else False

print(verify_multiplication(number_multiplication(5,5), 25))