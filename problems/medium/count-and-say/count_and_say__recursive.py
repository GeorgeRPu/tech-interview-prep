r"""
>>> from count_and_say__recursive import countAndSay
>>> countAndSay(1)
'1'
>>> countAndSay(4)
'1211'
"""


def countAndSay(n: int) -> str:
    """Return the ``n``-th count-and-say string."""
    if n == 1:
        return "1"

    count_and_say = ""
    digits = countAndSay(n - 1)
    previous_digit = digits[0]
    count = 0
    for digit in digits:
        if digit == previous_digit:
            count += 1
        else:
            count_and_say += f"{count}{previous_digit}"

            previous_digit = digit
            count = 1

    count_and_say += f"{count}{previous_digit}"

    return count_and_say
