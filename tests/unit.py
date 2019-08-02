import pytest

from transpose_longest_word import lib


class TestReadWordsFromFile:
    def test_get_expected_word_list(self, mocker, test_data):
        file_data = '\n'.join(test_data.word_list)
        mocker.patch('builtins.open', mocker.mock_open(read_data=file_data))

        actual = lib.read_words_from_file('test/file')

        # this will ignore issues with the join above, which loses trailing
        # empty strings
        assert ''.join(actual) == ''.join(test_data.word_list)

    def test_none_raises_error(self, mocker):
        mocker.patch('builtins.open', mocker.mock_open(read_data='filler'))

        with pytest.raises(AssertionError) as err:
            lib.read_words_from_file(None)
            assert err.message == 'File path is required.'

    def test_removes_expected_whitespace(self, mocker):
        test_data = [' leading_space', 'split word', 'trailing_space ']
        file_data = '\n'.join(test_data)
        mocker.patch('builtins.open', mocker.mock_open(read_data=file_data))

        word_list = lib.read_words_from_file('test/file')

        assert ' '.join(word_list) == 'leading_space split word trailing_space'


class TestGetLongestWord:
    def test_get_expected_word(self, test_data):
        expected = test_data.expected[0]
        actual = lib.get_longest_word(test_data.word_list)
        assert actual == expected

    def test_none_raises_error(self):
        with pytest.raises(TypeError) as err:
            lib.transpose_word(None)
            assert err.message == "'NoneType' object is not reversible"


class TestTransposeWord:
    def test_expected_reverse(self, test_data):
        actual = lib.transpose_word(test_data.expected[0])
        assert actual == test_data.expected[1]

    def test_none_raises_error(self):
        with pytest.raises(TypeError) as err:
            lib.transpose_word(None)
            assert err.message == "'NoneType' object is not reversible"
