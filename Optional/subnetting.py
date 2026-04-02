import module


# user_ipv4_input = input(
#     "Input An Ipv4 Address which you want to get the range of its IP Address?e.g 192.168.0.1/24:\n"
# )


# print(module.isValidIpv4Address(user_ipv4_input))
# print(module.generateBinaryNumberOfTheIpAddress("255.255.254.0"))
# print(module.generateSubnetMaskOfTheIpAddress(8))


# print(module.convertBinaryToReadableIpFormat("11111111.11111111.11110000.00000000"))


print(module.totalNumberOfHostInASubNet("20"))


# print(
#     module.totalNumberOfSubnetInANetwork(
#         module.generateBinaryNumberOfTheIpAddress("255.255.248.0")["ipv4_list"]
#     )
# )


print(module.getNetworkClass("192.168.0.1"))
