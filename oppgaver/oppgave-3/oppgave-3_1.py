ip_input = input("Please enter IPv4 IP-address: ")

def ip_validator(ip_addr) -> bool:
    """
    Splits and validates user inputted IP-address.
    Checks for:
    - Num of segments
    - Value of segments
    :param ip_addr: User inputted IP-address
    :return: Bool representation of validity of IP-address
    """
    segments = ip_addr.split(".")

    if len(segments) != 4:
        return False

    for segment in segments:
        value = int(segment)

        if not (0 <= value <= 255):
            return False

    return True

print(ip_validator(ip_input))