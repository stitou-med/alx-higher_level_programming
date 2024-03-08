#!/usr/bin/python3

"""A module for text indentation"""


def text_indentation(text):
    """``text_indentation``:
            a function that prints newline when it sees `.`, `:`, `?`

    Args:
        text(string): A string to be pinted and indented those character
        where seen adds a blankline
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        i = 0
        while i < len(text):
            print(text[i], end="")
            if text[i] == '.' or text[i] == ':' or text[i] == '?':
                print('\n')
                if i == len(text) - 1:
                    break
                if text[i + 1] == ' ':
                    i += 1
                while text[i] == ' ' and text[i+1] == ' ' and i+1 < len(text):
                    i += 1
            i += 1
