import module

# user_ipv4_input = input(
#     "Input An Ipv4 Address which you want to get the range of its IP Address?e.g 192.168.0.1/24:\n"
# )


# print(module.isValidIpv4Address(user_ipv4_input))
# print(module.generateBinaryNumberOfTheIpAddress(user_ipv4_input.split("/")[0]))
# print(module.generateSubnetMaskOfTheIpAddress(24))




print(module.convertBinaryToReadableIpFormat(module.generateSubnetMaskOfTheIpAddress(24)))
