import pytest

from transpose_longest_word.main import main

command_template = 'tlw-cli {}'


class TestTlpCli:
    def test_against_test_data(self, capsys, test_data):
        expected = test_data.expected_std_out

        with test_data.write_to_file() as input_file:
            command = command_template.format(input_file.absolute())
            main(command.split())

        std = capsys.readouterr()

        assert not std.err, 'Error: {}'.format(std.err)
        assert std.out == expected, "Error: {} is not expected {}"\
            .format(std.out, expected)

    def test_missing_path_prints_help(self, capsys):
        with pytest.raises(SystemExit):
            main(['tlw-cli'])

        std = capsys.readouterr()

        assert not std.out, "Error: unexpected output: {}".format(std.out)

        assert 'usage: ' in std.err
        assert ' [-h] input_file' in std.err
        assert 'error: the following arguments are required: input_file'\
               in std.err

    def test_invalid_path_throws_error(self, capsys):
        command = command_template.format('/invalid/path')
        with pytest.raises(FileNotFoundError) as err:
            main(command.split())
            assert err.message == "No such file or directory: '/invalid/path'"
