from pathlib import Path
from typing import List, Tuple


input_data = [
    ['a', 'ab', 'abc', 'abcd', 'abcde'],
    ['', 'ab', '', '', 'abcd', 'abcde', ''],
    ['abc', 'bcd', 'cde'],
    [],
    ['', '', ''],
    ['!@#$%^&*()'],
]

expected_outputs = [
    ('abcde', 'edcba'),
    ('abcde', 'edcba'),
    ('abc', 'cba'),
    ('', ''),
    ('', ''),
    ('!@#$%^&*()', ')(*&^%$#@!'),
]


class TestData:
    _word_list: List[str]
    _expected: Tuple[str, str]
    _tmp_path: Path

    def __init__(self, word_list, expected, tmp_path):
        self._word_list = word_list
        self._expected = expected
        self._tmp_path = tmp_path

    @property
    def word_list(self) -> List[str]:
        return self._word_list

    @property
    def expected(self) -> Tuple[str, str]:
        return self._expected

    @property
    def expected_std_out(self) -> str:
        return '{}\n{}\n'.format(self.expected[0], self.expected[1])

    def write_to_file(self) -> Path:
        tmp_file = self._tmp_path / 'sample_data.txt'
        tmp_file.write_text('\n'.join(self.word_list))
        return tmp_file
