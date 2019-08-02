from pytest import fixture
from tests.test_data import TestData, input_data, expected_outputs


@fixture(params=zip(input_data, expected_outputs))
def test_data(request, tmp_path):
    """
    This is a parameteried fixture that will return a TestData object for
    every defined input & expected output pair. It can be used by any test
    case that needs to run over the entire input/output set.

    :param request: pytest request fixture
    :param tmp_path: pytest tmp_path fixture
    :return:TestData object for input and expected response
    """
    return TestData(request.param[0], request.param[1], tmp_path)
