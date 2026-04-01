import module

user_ipv4_input = input("Input An Ipv4 Address?e.g 192.168.0.1:\n")


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


print(module.isValidIpv4Address(user_ipv4_input))
print(generateBinaryNumberOfTheIpAddress(user_ipv4_input))
