from Crypto.Util.number import *
with open('flag.txt','rb') as f:
    flag = f.read().strip()
e=65537
p=getPrime(128)
q=getPrime(128)
n=p*q
m=bytes_to_long(flag)

phi = (p-1)*(q-1)
d = inverse(e,phi)

ct=pow(m,d,n)


print (p)
print (q)
print (e)
print (ct)

print (hex(ct)[2:-1].decode('hex'))
