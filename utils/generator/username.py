from random import randint


def generate_username(name: str, str_len: int = 5, total_len: int = 10):
    assert(total_len > str_len)

    # Get the first str_len of name
    name = name.replace(" ", "")
    first = name[:min(str_len, len(name))]

    # Generate random number with n digits
    n = total_len - len(first)
    range_start = 10**(n-1)
    range_end = (10**n)-1

    # Concatenate sliced name and generated random number
    return first + str(randint(range_start, range_end))
