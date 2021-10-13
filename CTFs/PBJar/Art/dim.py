import os
import binascii
import struct

misc = open("art.png","rb").read()

for i in range(65535):
    for j in range(65535):
        data = misc[12:16] + struct.pack('>i',i)+ struct.pack('>i',j)+misc[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == 0x60444cb6:
            print(i,j)
