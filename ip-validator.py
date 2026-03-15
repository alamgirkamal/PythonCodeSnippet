import ipaddress

def validate_ipv4(address):
    ip_list = []
    address_list = address.split()

    """Check if the given string is a valid IPv6 address."""
    for address in address_list:
        try:
            ipaddress.IPv4Address(address)
            ip_list.append(address)
        except ValueError:
            pass
    return ip_list

def validate_ipv6(address):
    """Check if the given string is a valid IPv6 address."""
    try:
        ipaddress.IPv6Address(address)
        return address
    except ValueError:
        return ""

# Example usage:
print(f"'2001:db8::1' is : {validate_ipv6('2001:db8::1')}")
print(f"'fe80::1234%1' is : {validate_ipv6('fe80::1234%1')}")
print(f"'192.168.1.1' is : {validate_ipv6('192.168.1.1')}")
print(f"'not an ip' is : {validate_ipv6('not an ip')}")


print(f"'2001:db8::1' is : {validate_ipv4('2001:db8::1')}")
print(f"'fe80::1234%1' is : {validate_ipv4('fe80::1234%1')}")
print(f"'192.168.1.1' is : {validate_ipv4('192.168.1.1')}")
print(f"'192.168.1.1' is : {validate_ipv4('192.168.1.1 192.168.1.2 192.168.1.3 192.168.1.1 192.168.1.1 192.168.1.1 192.168.1.1')}")
print(f"'not an ip' is : {validate_ipv4('not an ip')}")
