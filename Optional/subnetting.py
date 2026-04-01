import module

# user_ipv4_input = input(
#     "Input An Ipv4 Address which you want to get the range of it's IP Address?e.g 192.168.0.1/24:\n"
# )


def generateSubnetMaskOfTheIpAddress(subnet):
    if int(subnet) > 32:
        print("Subnet of an address cant be more than 32 bit")
        return
    binary_code_of_subnet = ""
    for i in range(1, 33):
        if i <= int(subnet):
            binary_code_of_subnet += "1"
            if i % 8 == 0 and i != 32:
                binary_code_of_subnet += "."
        else:
            binary_code_of_subnet += "0"
    print(binary_code_of_subnet)


# print(module.isValidIpv4Address(user_ipv4_input))
# print(module.generateBinaryNumberOfTheIpAddress(user_ipv4_input.split("/")[0]))
generateSubnetMaskOfTheIpAddress(31)
