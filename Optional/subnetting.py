import ipaddress

user_ipv4_input = input("Input An Ipv4 Address?e.g 192.168.0.1:\n")


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


def generateBinaryNumberOfTheIpAddress(ipAddress=""):
    if ipAddress.count(".") > 3:
        print("A valid Ipv4 Address should have 3 dots")
        return ""
    splitIpToList = ipAddress.split(".")
    binaryIpList = []
    binaryIpAddress = ""
    for address in splitIpToList:
        binaryIpList.append(format(int(address), "08b"))
        if splitIpToList[-1] == address:
            binaryIpAddress += f'{format(int(address), "08b")}'
        else:
            binaryIpAddress += f'{format(int(address), "08b")}.'

    return {"ipv4": binaryIpAddress, "ipv4_list": binaryIpList}


# print(isValidIpv4Address(user_ipv4_input))
print(generateBinaryNumberOfTheIpAddress(user_ipv4_input))
