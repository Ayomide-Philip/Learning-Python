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


def getNetworkClass(ipAddress=""):
    """This function is used to get the class an ip address, which range from 'A','B','C','D' and 'E', it uses a function
    isValidIp44Address to check whether the ip address inputted is a valid ip, then returns the correct class if its valid
    """
    if not module.isValidIpv4Address(ipAddress):
        return None

    first_part_of_ip_address = ipAddress.split(".")[0]

    if len(first_part_of_ip_address) == 0:
        return None

    ipClass = ""
    if 0 <= int(first_part_of_ip_address) <= 127:
        ipClass = "A"
    elif 128 <= int(first_part_of_ip_address) <= 191:
        ipClass = "B"
    elif 192 <= int(first_part_of_ip_address) <= 223:
        ipClass = "C"
    elif 224 <= int(first_part_of_ip_address) <= 239:
        ipClass = "D"
    elif 240 <= int(first_part_of_ip_address) <= 255:
        ipClass = "E"
    else:
        return None

    return {"class": ipClass}


print(getNetworkClass("192.168.0.1"))
