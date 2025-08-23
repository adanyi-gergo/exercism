def rebase(input_base, digits, output_base):
    check_input_errors(input_base, output_base)
    if check_for_empty_or_all_zero_list(digits):
        return [0]
    decimal = to_decimal(input_base, digits)
    return from_decimal(output_base, decimal)


def to_decimal(base, digits):
    total = 0
    for index, num in enumerate(reversed(digits)):
        if 0 <= num < base:
            total += num * (base ** index)
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    return total


def from_decimal(output_base, decimal):
    output = []
    while decimal > 0:
        output.append(decimal % output_base)
        decimal //= output_base

    output.reverse()
    return output


def check_input_errors(input_base, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")


def check_for_empty_or_all_zero_list(digits):
    return not digits or all(d == 0 for d in digits)
