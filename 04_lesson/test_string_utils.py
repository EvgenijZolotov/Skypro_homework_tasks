import pytest
from string_utils import StringUtils

class TestStringUtils:
    @pytest.fixture
    def utils(self):
        return StringUtils()

    @pytest.mark.parametrize("input,expected", [
        # Позитивные
        ("тест", "Тест"),                # Кириллица
        ("123", "123"),                   # Числа как строка
        ("04 апреля 2023", "04 апреля 2023"),  # С пробелами

        # Негативные
        ("", ""),                         # Пустая строка
        (" ", " "),                       # Строка с пробелом
        (None, None)                      # None (должен обрабатываться)
    ])
    def test_capitilize(self, utils, input, expected):
        if input is None:
            with pytest.raises(AttributeError):
                utils.capitilize(input)
        else:
            assert utils.capitilize(input) == expected

    def test_to_title_case(self, utils):
        # Позитивные
        assert utils.to_title_case("hello world") == "Hello World"
        assert utils.to_title_case("04 апреля 2023") == "04 Апреля 2023"
        assert utils.to_title_case("123 abc") == "123 Abc"

        # Негативные
        assert utils.to_title_case("") == ""
        assert utils.to_title_case(" ") == " "
        with pytest.raises(AttributeError):
            utils.to_title_case(None)

    def test_contains(self, utils):
        # Позитивные
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("04 апреля 2023", "апреля") is True
        assert utils.contains("123", "2") is True

        # Негативные
        assert utils.contains("", "") is True
        assert utils.contains(" ", " ") is True
        with pytest.raises(TypeError):
            utils.contains(None, "a")

    @pytest.mark.parametrize("string,symbol,expected", [
        # Позитивные
        ("SkyPro", "k", "SyPro"),
        ("04 апреля 2023", " ", "04апреля2023"),
        ("123", "2", "13"),

        # Негативные
        ("", "a", ""),
        (" ", " ", ""),
        (None, "a", None)
    ])
    def test_delete_symbol(self, utils, string, symbol, expected):
        if string is None:
            with pytest.raises(TypeError):
                utils.delete_symbol(string, symbol)
        else:
            assert utils.delete_symbol(string, symbol) == expected

    def test_starts_with(self, utils):
        # Позитивные
        assert utils.starts_with("SkyPro", "S") is True
        assert utils.starts_with("04 апреля", "0") is True
        assert utils.starts_with(" 123", " ") is True

        # Негативные
        assert utils.starts_with("", "") is True
        assert utils.starts_with(" ", " ") is True
        with pytest.raises(TypeError):
            utils.starts_with(None, "a")

    def test_end_with(self, utils):
        # Позитивные
        assert utils.end_with("SkyPro", "o") is True
        assert utils.end_with("04 апреля", "я") is True
        assert utils.end_with("123 ", " ") is True

        # Негативные
        assert utils.end_with("", "") is True
        assert utils.end_with(" ", " ") is True
        with pytest.raises(TypeError):
            utils.end_with(None, "a")

    @pytest.mark.parametrize("string,expected", [
        # Позитивные
        ("тест", False),
        ("123", False),
        ("04 апреля 2023", False),

        # Негативные
        ("", True),
        (" ", True),
        (None, True)
    ])
    def test_is_empty(self, utils, string, expected):
        if string is None:
            with pytest.raises(TypeError):
                utils.is_empty(string)
        else:
            assert utils.is_empty(string) == expected

    @pytest.mark.parametrize("lst,delimiter,expected", [
        # Позитивные
        (["тест", "123"], ", ", "тест, 123"),
        ([1, 2, 3], "-", "1-2-3"),
        (["04", "апреля", "2023"], " ", "04 апреля 2023"),

        # Негативные
        ([], ", ", ""),
        (None, ",", None)
    ])
    def test_list_to_string(self, utils, lst, delimiter, expected):
        if lst is None:
            with pytest.raises(TypeError):
                utils.list_to_string(lst, delimiter)
        else:
            assert utils.list_to_string(lst, delimiter) == expected
