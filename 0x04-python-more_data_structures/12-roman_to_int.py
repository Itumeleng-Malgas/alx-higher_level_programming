def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    def calculate_subtraction(subtract_list):
        max_value = max(subtract_list)
        return max_value - sum(value for value in subtract_list
                               if max_value > value)

    result = 0
    previous_value = 0
    subtract_list = [0]

    for symbol in roman_string:
        if symbol in roman_numerals:
            if roman_numerals[symbol] <= previous_value:
                result += calculate_subtraction(subtract_list)
                subtract_list = [roman_numerals[symbol]]
            else:
                subtract_list.append(roman_numerals[symbol])

            previous_value = roman_numerals[symbol]

    result += calculate_subtraction(subtract_list)
    return result
