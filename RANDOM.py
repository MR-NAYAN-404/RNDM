import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from nsn import login

        login()
elif b == '32bit':
    print("NOT SUPPORTED BRO YOUR PHONE 32 BIT")
