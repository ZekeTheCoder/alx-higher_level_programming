#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt = text[:]

    for char in ".?:":
        list_text = txt.split(char)
        txt = ""

        for elem in list_text:
            elem = elem.strip(" ")
            txt = elem + char if txt is "" else txt + "\n\n" + elem + char

    print(txt[:-3], end="")
