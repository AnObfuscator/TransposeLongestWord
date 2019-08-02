from typing import List


def read_words_from_file(file_path: str) -> List[str]:
    """
    Reads the list of words from the specified file path. Each line will be
    considered a single word. Interior whitespace will be preserved, while
    leading/trailing whitespaces will be stripped.

    :param file_path: Relative or absolute path to the input file
    :return: list of words in the file
    """
    assert file_path, 'File path is required.'
    with open(file_path) as the_file:
        the_words = [word.strip() for word in the_file.readlines()]
    return the_words


def get_longest_word(word_list: List[str]) -> str:
    """
    Do a simple linear search to find the longest word in the inputted list.
    If there are multiple words of the same length, this will return the first
    word with the largest length.

    :param word_list: List of strings
    :return: First string with the largest length
    """
    the_longest = ''
    for word in word_list:
        if len(word) > len(the_longest):
            the_longest = word
    return the_longest


def transpose_word(word: str) -> str:
    """
    Return the transpose of the inputted string.

    :param word: input string
    :return: reverse of word
    """
    return ''.join(reversed(word))
