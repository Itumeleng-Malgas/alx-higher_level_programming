#!/usr/bin/python3


def text_indentation(text):
    """
    Splits the string at the occurrence of ., ? and :,
    and replaces the next character with \n\n
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    i = 0

    while i < len(text):
        char = text[i]

        if char in ('.', '?', ':'):
            result.append(char)
            i += 1

            if i < len(text):
                result.append('\n\n')
                i += 1
        else:
            result.append(char)
            i += 1

    # Join the result list into a single string
    result_text = ''.join(result)
    split_result = result_text.split('\n\n')
    final_result = '\n\n'.join(split_result)
    print(final_result)


text_indentation("Hello. My Name is: Itumeleng, Malgas ")
