from Crypto.Util.number import *
with open('flag.txt','rb') as f:
    flag = f.read().strip()

e=65537
p=getPrime(128)
q=getPrime(128)
n=p*q

c = 2680665419605434578386620658057993903866911471752759293737529277281335077856
phi = (p-1) * (q-1)
d = inverse(e,phi)

m=bytes_to_long(flag)

ct=pow(c,d,n)


print (hex(ct)[2:-1])
