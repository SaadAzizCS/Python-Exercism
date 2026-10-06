def is_armstrong_number(number):
    total = 0
    array = []
    for number_1 in str(number):
        array.append(number_1)
    for num in array:
        total += int(num) ** len(array)
    if total == number:
        return True
    return False


