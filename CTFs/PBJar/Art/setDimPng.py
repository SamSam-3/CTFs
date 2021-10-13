import subprocess


f = open("art.png",'rb')
newFile = f.readlines()

x = subprocess.run(['pngcheck','art.png'], stdout=True).stdout

print(x)