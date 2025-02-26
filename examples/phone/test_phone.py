# phone numbers


def normalize_number(input_phone):
    if input_phone[3] == "-" and input_phone[7] == "-":
        return input_phone
    return f"{input_phone[0:3]}-{input_phone[3:6]}-{input_phone[6:11]}"


def test_with_dashes():
    assert normalize_number("123-456-7890") == "123-456-7890"


def test_without_dashes():
    assert normalize_number("5556667777") == "555-666-7777"


# Additional test cases
def test_with_parentheses():
    assert normalize_number("(123) 456-7890") == "123-456-7890"


def test_with_spaces():
    assert normalize_number("123 456 7890") == "123-456-7890"


def test_with_country_code():
    assert normalize_number("+1 (123) 456-7890") == "123-456-7890"
    try:
        normalize_number("+64 (123) 456-7890")
    except ValueError:
        assert True


def test_invalid_number_of_digits():
    try:
        normalize_number("6")
    except ValueError:
        assert True


def test_non_numeric():
    try:
        normalize_number("abc")
    except ValueError:
        assert True
    try:
        normalize_number("+100000000")
    except ValueError:
        assert True
    try:
        normalize_number("000000000")
    except ValueError:
        assert True
