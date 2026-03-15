import ipaddress

def normalize_ip(address):
    ip_list = []
    address_list = address.split()

    """Check if the given string is a valid IPv6 address."""
    for address in address_list:
        try:
            ipaddress.IPv4Address(address)
            ip_list.append(address)
        except ValueError:
            try:
                ipaddress.IPv6Address(address)
                ip_list.append(address)
            except ValueError:
                pass

    if len(ip_list)==0:
        return ""
    elif len(ip_list)==1:
        return ip_list[0]
    else:
        return ip_list

if __name__ == "__main__":
    # Example usage:
    print(f"'2001:db8::1' is : {normalize_ip('2001:db8::1')}")
    print(f"'fe80::1234%1' is : {normalize_ip('fe80::1234%1 fe80::1234%1 fe80::1234%1 fe80::1234%1 fe80::1234%1 fe80::1234%1')}")
    print(f"'192.168.1.1' is : {normalize_ip('192.168.1.1')}")
    print(f"'not an ip' is : {normalize_ip('not an ip')}")


    print(f"'2001:db8::1' is : {normalize_ip('2001:db8::1')}")
    print(f"'fe80::1234%1' is : {normalize_ip('fe80::1234%1')}")
    print(f"'192.168.1.1' is : {normalize_ip('192.168.1.1')}")
    print(f"'192.168.1.1' is : {normalize_ip('192.168.1.1 192.168.1.2 192.168.1.3 192.168.1.1 192.168.1.1 192.168.1.1 192.168.1.1')}")
    print(f"'not an ip' is : {normalize_ip('not an ip')}")
