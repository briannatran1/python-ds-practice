def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    # figure out another method to count
    # use dir or help
    # count = 0
    # lower_word = word.lower()

    # for char in lower_word:
    #     if char == letter:
    #         count += 1

    # return count

    return word.lower().count(letter.lower())
