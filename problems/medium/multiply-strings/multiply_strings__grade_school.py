r"""
>>> from multiply_strings__grade_school import multiply
>>> multiply("2", "3")
'6'
>>> multiply("123", "456")
'56088'
>>> multiply("0", "0")
'0'
>>> multiply("999", "999")
'998001'
"""


def multiply(num1: str, num2: str) -> str:
    """Multiply two numbers represented as strings."""
    if num1 == "0" or num2 == "0":
        return "0"

    n1 = len(num1)
    n2 = len(num2)
    result = [0] * (n1 + n2)

    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10

    start = 0
    while start < len(result) and result[start] == 0:
        start += 1

    return "".join(str(d) for d in result[start:])
