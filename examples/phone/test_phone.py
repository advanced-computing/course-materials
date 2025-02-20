# phone numbers


def normalize_number(input_phone):
    if input_phone[3] == "-" and input_phone[7] == "-":
        return input_phone

    return f"{input_phone[0:3]}-{input_phone[3:6]}-{input_phone[6:11]}"


# dashes and not


def test_with_dashes():
    # if normalize_number("123-456-7890") == "123-456-7890":
    #     print("good")
    # else:
    #     print("error")
    assert normalize_number("123-456-7890") == "123-456-7890"


def test_without_dashes():
    # if normalize_number("5556667777") == "555-666-7777":
    #     print("good")
    # else:
    #     print("error")
    assert normalize_number("5556667777") == "555-666-7777"


# result = normalize_number("1234567890")
# if result == "123-456-7890":
#     print("good")
# else:
#     print("error:", result)

# parentheses
"(123) 456-7890"  # -> "123-456-7890"
# spaces
"123 456 7890"  # -> "123-456-7890"
# country code
"+1 (123) 456-7890"  # -> "123-456-7890"
"+64 (123) 456-7890"  # -> error
# number of digits
"6"  # error
# non-numeric
"abc"  # error
"+100000000"  # error
"000000000"  # error

# loop through digits
# if not an int, throw an error
