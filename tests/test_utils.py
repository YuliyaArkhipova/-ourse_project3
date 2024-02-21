import pytest
from func.utils import load_operations_list
from func.utils import operation_data
from func.utils import format_date
from func.utils import format_number
from func.utils import last_operations


@pytest.fixture
def data_test():
    return [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
             "operationAmount": {"amount": "31957.58",
                                 "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
             "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
            {"id": 710136990, "state": "CANCELED", "date": "2018-08-17T03:57:28.607101",
             "operationAmount": {"amount": "66906.45",
                                 "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации",
            "from": "Maestro 1913883747791351", "to": "Счет 11492155674319392427"}]


def test_load_operations_list(data_test):
    data = load_operations_list("tests/data_test.json")
    assert data == data_test


def test_operation_data(data_test):
    assert operation_data(data_test) == [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                                          "operationAmount": {"amount": "31957.58",
                                                              "currency": {"name": "руб.", "code": "RUB"}},
                                          "description": "Перевод организации",
                                                           "from": "Maestro 1596837868705199",
                                                           "to": "Счет 64686473678894779589"}]


def test_format_number():
    assert format_number("1596837868705199") == "1596 83** **** 5199"
    assert format_number("64686473678894779589") == "**9589"


def test_format_date():
    assert format_date({"date": "2019-08-26T10:50:58.294041"}) == "26.08.2019"


@pytest.fixture
def data_test2():
    return [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
             "operationAmount": {"amount": "31957.58",
                                 "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
             "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]


def test_last_operations(data_test2):
    assert last_operations(data_test2) == ('26.08.2019 Перевод организации\n'
                                           'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                           '31957.58 руб.\n'
                                           '----------------------\n')


@pytest.fixture
def data_test3():
    return [{"id": 893507143, "state": "EXECUTED", "date": "2018-02-03T07:16:28.366141",
             "operationAmount": {"amount": "90297.21",
                                 "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Открытие вклада", "to": "Счет 37653295304860108767"}]


def test_last_operations2(data_test3):
    assert last_operations(data_test3) == ('03.02.2018 Открытие вклада\n'
                                           'Unknown -> Счет **8767\n'
                                           '90297.21 руб.\n'
                                           '---------------------\n')
