def fnv1a_32(string: str) -> str:
    """
    returns the hex representation of a given input string
    after running through fnv hash algo
    """
    hash = 0x811c9dc5
    fnv_prime = 0x01000193
    for char in string:
        hash = (hash ^ ord(char)) * fnv_prime
        hash &= 0xffffffff # wrapping math

    return hex(hash)


if __name__ == "__main__":
    strings = [
        "USERNAME=",
        "COMPUTERNAME=",
        "USERDOMAIN=",
        "USERDNSDOMAIN="
    ]

    for string in strings:
        print(f"{fnv1a_32(string)}: {string}")
