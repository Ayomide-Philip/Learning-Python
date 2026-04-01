import ipaddress

user_ipv4_input = input("Input An Ipv4 Address?")


def isValidIpv4Address(address):
    """This function would check if the inputted ip address is an ipv4"""
    try:
        ipaddress.IPv4Address(address)
        print(f"{address} its an ipv4 Address")
    except ipaddress.AddressValueError:
        print(f"{address} is not a valid ipv4 Address")


isValidIpv4Address(user_ipv4_input)
