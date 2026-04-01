import module
from module import generateBinaryNumberOfTheIpAddress
from module import generateSubnetMaskOfTheIpAddress


# user_ipv4_input = input(
#     "Input An Ipv4 Address which you want to get the range of its IP Address?e.g 192.168.0.1/24:\n"
# )


# print(module.isValidIpv4Address(user_ipv4_input))
# print(module.generateBinaryNumberOfTheIpAddress("255.255.255.224"))
# print(module.generateSubnetMaskOfTheIpAddress(8))


# print(module.convertBinaryToReadableIpFormat(module.generateSubnetMaskOfTheIpAddress(24)))


# def totalNumberOfHostInANetwork(subnet=""):
#     if int(subnet) > 32:
#         print("The scope of an ipv4 can't pass 32 bit")
#         return None
#
#     totalNumberOfHostBit = generateSubnetMaskOfTheIpAddress(subnet).count("0")
#     print(totalNumberOfHostBit)
#     totalNumberOfHost = 2**totalNumberOfHostBit
#     totalNumberOfUsableHost = totalNumberOfHost - 2
#
#     return {
#         "totalNumberOfHostBit": format(totalNumberOfHostBit, ","),
#         "totalNumberOfHost": format(totalNumberOfHost, ","),
#         "totalNumberOfUsableHost": format(totalNumberOfUsableHost, ","),
#     }


# print(totalNumberOfHostInANetwork("8"))


def totalNumberOfSubnetInANetwork(binaryOfSubnetList):
    doesOneExist = "00000000"
    if len(binaryOfSubnetList) > 4:
        print("It can only contain 4 byte of octet")
        return None

    for binary in binaryOfSubnetList:
        if binary.count("1") > 0 and binary.count("0") > 0:
            print(binary)
            doesOneExist = binary
            break
    totalNumberOfSubNet = 2 ** doesOneExist.count("1")
    return totalNumberOfSubNet


print(
    totalNumberOfSubnetInANetwork(
        generateBinaryNumberOfTheIpAddress("255.255.255.252")["ipv4_list"]
    )
)
