import module
from module import generateBinaryNumberOfTheIpAddress

# user_ipv4_input = input(
#     "Input An Ipv4 Address which you want to get the range of its IP Address?e.g 192.168.0.1/24:\n"
# )


# print(module.isValidIpv4Address(user_ipv4_input))
# print(module.generateBinaryNumberOfTheIpAddress("255.255.254.0"))
# print(module.generateSubnetMaskOfTheIpAddress(20))


# print(module.convertBinaryToReadableIpFormat("11111111.11111111.11110000.00000000"))


# print(module.totalNumberOfHostInASubNet("20"))


# print(
#     module.totalNumberOfSubnetInANetwork(
#         module.generateBinaryNumberOfTheIpAddress("255.255.248.0")["ipv4_list"]
#     )
# )


# print(module.getNetworkClass("192.168.0.1"))


def subNetANetworkUsingDefaultNetMask(ipAddress="", numberOfNetwork=0):
    """This function is going to get the default subnet mask"""
    if not module.isValidIpv4Address(ipAddress):
        return
    # get the default subnet of the ip address class
    if module.getNetworkClass(ipAddress)["subnet"] == "":
        getIpSubNet = "255.255.255.0"
    else:
        getIpSubNet = module.getNetworkClass(ipAddress)["subnet"]
    # use subnet gotten to generate the binary form
    getBinaryOfTheSubNet = generateBinaryNumberOfTheIpAddress(getIpSubNet)["ipv4"]
    if getBinaryOfTheSubNet.count("1") >= 32:
        return
    numberOfHostBitNeeded = 1
    while 2**numberOfHostBitNeeded < numberOfNetwork:
        numberOfHostBitNeeded += 1
    print(numberOfHostBitNeeded)
    newNumberOfNetworkBit = getBinaryOfTheSubNet.count("1") + numberOfHostBitNeeded
    print(newNumberOfNetworkBit)
    if newNumberOfNetworkBit > 30:
        print(f"You don't have 2 host bit left")
        return


subNetANetworkUsingDefaultNetMask("192.168.0.1", 20)
