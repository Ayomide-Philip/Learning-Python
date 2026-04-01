import ipaddress


def isValidIpv4Address(address):
    """This function would check if the inputted ip address is an ipv4"""
    if address.count(".") > 3:
        print(f"An ipv4 Address is supposed to have 3 dots")
        return False
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        print(f"{address} is not a valid ipv4 Address")
        return False


def generateBinaryNumberOfTheIpAddress(ipAddress=""):
    """This function is used to generate the binary address of an ip address and also the subnet of the ip address"""
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


def generateSubnetMaskOfTheIpAddress(subnet = 0):
    if int(subnet) > 32:
        print("Subnet of an address cant be more than 32 bit")
        return None
    binary_code_of_subnet = ""
    for i in range(1, 33):
        if i <= int(subnet):
            binary_code_of_subnet += "1"
            if i % 8 == 0 and i != 32:
                binary_code_of_subnet += "."
        else:
            binary_code_of_subnet += "0"
            if i % 8 == 0 and i != 32:
                binary_code_of_subnet += "."
    return binary_code_of_subnet
