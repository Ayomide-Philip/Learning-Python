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


def totalNumberOfHostInANetwork(subnet=""):
    if int(subnet) > 32:
        print("The scope of an ipv4 can't pass 32 bit")
        return None

    totalNumberOfHostBit = generateSubnetMaskOfTheIpAddress(subnet).count("0")
    print(totalNumberOfHostBit)
    totalNumberOfHost = 2**totalNumberOfHostBit
    totalNumberOfUsableHost = totalNumberOfHost - 2

    return {
        "totalNumberOfHostBit": format(totalNumberOfHostBit, ","),
        "totalNumberOfHost": format(totalNumberOfHost, ","),
        "totalNumberOfUsableHost": format(totalNumberOfUsableHost, ","),
    }


print(totalNumberOfHostInANetwork("30"))


print(
    module.totalNumberOfSubnetInANetwork(
        generateBinaryNumberOfTheIpAddress("255.255.255.252")["ipv4_list"]
    )
)
