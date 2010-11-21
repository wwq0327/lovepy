#!/usr/bin/env python
import mailbox

def main(mailbox_path):
    addresses = {}
    mb = mailbox.PortableUnixMailbox(file(mailbox_path))
    for msg in mb:
        toaddr = ms.getaddr('To')[1]
        addresses[toaddr] = 1
    addresses = addresses.keys()
    addresses.sort()
    for address in addresses:
        print address

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
