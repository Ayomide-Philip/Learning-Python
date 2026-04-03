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
    for address in splitIpToList:
        binaryIpList.append(format(int(address), "08b"))
    binaryIpAddress = ".".join(binaryIpList)
    return {"ipv4": binaryIpAddress, "ipv4_list": binaryIpList}


def generateSubnetMaskOfTheIpAddress(subnet=0):
    """This function generate the subnet of a particular ip Address for example, if you inputted 192.168.0.1/24:
    it takes the /24 and generate the subnet that the network is running on.
    """
    if int(subnet) > 32:
        print("Subnet of an address can't be more than 32 bit")
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


def convertBinaryToReadableIpFormat(binary=""):
    """This function convert binary back to ip address, and it also validates the new ip format generated to check if
    it's a valid ip address by calling the function isIpAddressValid
    """
    binaryList = binary.split(".")
    if len(binaryList) > 4:
        print("An ipv4 Address cant have more than 3 dots")
        return None
    ipAddressList = []
    for b in binaryList:
        try:
            binaryToInt = int(b, 2)
        except ValueError:
            print("Invalid Binary type")
            return None
        ipAddressList.append(str(binaryToInt))
    ipAddrInStr = ".".join(ipAddressList)
    if isValidIpv4Address(ipAddrInStr):
        return ipAddrInStr
    else:
        return None


def totalNumberOfSubnetInANetwork(binaryOfSubnetList=None):
    """This function is used to get the total number of host in a network, it takes in a list as input and check if the
    length of the list is more 4 then it returns an error and if not it get the total network available in that
    particular range of ip address, the output is a string
    """
    if binaryOfSubnetList is None:
        binaryOfSubnetList = []
    doesOneExist = "00000000"

    if len(binaryOfSubnetList) > 4:
        print("It can only contain 4 byte of octet")
        return None

    for binary in binaryOfSubnetList:
        if binary.count("1") > 0 and binary.count("0") > 0:
            doesOneExist = binary
            break
    totalNumberOfSubNet = 2 ** doesOneExist.count("1")
    return {"totalNumberOfSubNet": totalNumberOfSubNet}


def totalNumberOfHostInASubNet(subnet=""):
    """This function returns the total numbers of host (Ip Addresses) available in a using the subnet to get it"""
    if int(subnet) > 32:
        print("The scope of an ipv4 can't pass 32 bit")
        return None
    subNetInBinary = generateSubnetMaskOfTheIpAddress(int(subnet))
    numberOfSubnet = totalNumberOfSubnetInANetwork(subNetInBinary.split("."))
    totalNumberOfHostBit = subNetInBinary.count("0")
    totalNumberOfHost = 2**totalNumberOfHostBit
    totalNumberOfUsableHost = (totalNumberOfHost - 2) * int(
        numberOfSubnet["totalNumberOfSubNet"]
    )

    return {
        "totalNumberOfHostBit": format(totalNumberOfHostBit, ","),
        "totalNumberOfHostPerSubNet": format(totalNumberOfHost, ","),
        "totalNumberOfUsableHostPerSubNet": format(totalNumberOfHost - 2, ","),
        "totalNumberOfUsableHost": format(totalNumberOfUsableHost, ","),
        # "totalNumberOfSubNet": format(numberOfSubnet["totalNumberOfSubNet"], ","),
    }


def getNetworkClass(ipAddress=""):
    """This function is used to get the class an ip address, which range from 'A','B','C','D' and 'E', it uses a function
    isValidIp44Address to check whether the ip address inputted is a valid ip, then returns the correct class if its valid
    """
    if not isValidIpv4Address(ipAddress):
        return None

    first_part_of_ip_address = ipAddress.split(".")[0]

    if len(first_part_of_ip_address) == 0:
        return None

    ipClass = ""
    subnet = ""
    if 0 <= int(first_part_of_ip_address) <= 127:
        ipClass = "A"
        subnet = "255.0.0.0"
    elif 128 <= int(first_part_of_ip_address) <= 191:
        ipClass = "B"
        subnet = "255.255.0.0"
    elif 192 <= int(first_part_of_ip_address) <= 223:
        ipClass = "C"
        subnet = "255.255.255.0"
    elif 224 <= int(first_part_of_ip_address) <= 239:
        ipClass = "D"
    elif 240 <= int(first_part_of_ip_address) <= 255:
        ipClass = "E"
    else:
        return None

    return {"class": ipClass, "subnet": subnet}
