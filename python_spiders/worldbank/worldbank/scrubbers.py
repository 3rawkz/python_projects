def is_num(char):
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for element in range(0, len(numbers)):
        if char == numbers[element]:
            return True


def clean_data(dirty_list):
    clean_list = []
    for item in range(0, len(dirty_list)):
        clean_string = ''
        for char in dirty_list[item]:
            if is_num(char):
                clean_string = clean_string + char
            elif char == ',':
                clean_string = clean_string + char
            elif char == '.':
                clean_string = clean_string + char
        clean_list.append(clean_string)
    return clean_list
