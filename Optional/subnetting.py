import module

# user_ipv4_input = input(
#     "Input An Ipv4 Address which you want to get the range of its IP Address?e.g 192.168.0.1/24:\n"
# )


# print(module.isValidIpv4Address(user_ipv4_input))
# print(module.generateBinaryNumberOfTheIpAddress(user_ipv4_input.split("/")[0]))
# print(module.generateSubnetMaskOfTheIpAddress(24))


def convertBinaryToReadableIpFormat(binary=""):
    """This function convert binary back to ip address, and it also validates the new ip format generated to check if
    it's a valid ip address by calling the function isIpAddressValid
    """
    binaryList = binary.split(".")
    if len(binaryList) > 4:
        print("An ipv4 Address cant have more than 3 dots")
        return None
    ipAddressList = []
    for binary in binaryList:
        binaryToInt = int(binary, 2)
        ipAddressList.append(str(binaryToInt))
    ipAddrInStr = ".".join(ipAddressList)
    if module.isValidIpv4Address(ipAddrInStr):
        return ipAddrInStr
    else:
        return None


print(convertBinaryToReadableIpFormat(module.generateSubnetMaskOfTheIpAddress(24)))
