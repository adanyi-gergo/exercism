def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    decimal = sum(d * (input_base ** i) for i, d in enumerate(digits[::-1]))
    output = []
    while decimal > 0:
        decimal, remainder = divmod(decimal, output_base)
        output.insert(0, remainder)

    return output if output else [0]