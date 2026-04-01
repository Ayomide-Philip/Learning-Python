import ipaddress


def isValidIpv4Address(address):
    """This function would check if the inputted ip address is an ipv4"""
    if address.count(".") > 3:
        print(f"An ipv4 Address is supposed to have 3 dots")
        return False
    try:
        ipaddress.IPv4Address(address)
        print(f"{address} its an ipv4 Address")
        return True
    except ipaddress.AddressValueError:
        print(f"{address} is not a valid ipv4 Address")
        return False
