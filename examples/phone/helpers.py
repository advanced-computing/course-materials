from time import sleep


def normalize_number(input_phone):
    if input_phone[3] == "-" and input_phone[7] == "-":
        return input_phone

    return f"{input_phone[0:3]}-{input_phone[3:6]}-{input_phone[6:11]}"


def get_data():
    # mimicking a slow API call
    sleep(5)
