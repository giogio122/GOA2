def create_phone_number(n):
    digits = "".join(map(str, n))
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
