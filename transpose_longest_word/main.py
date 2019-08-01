import argparse
import sys
from transpose_longest_word import lib


def main(sys_argv=sys.argv):
    """
    Program entry point, which will parse the input, call the appropriate
    back end functions, and print the output.

    sys.argv is parameterized to simplify testing.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to input file.")
    args = parser.parse_args(sys_argv[1:])

    words = lib.read_words_from_file(args.input_file)
    longest_word = lib.get_longest_word(words)
    transpose = lib.transpose_word(longest_word)

    print(longest_word)
    print(transpose)


if __name__ == '__main__':
    main()
