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

def MEDUSA_SERVER():

    os.system("clear")
    
    print(MEDUSA_LOGO_BANNER)
    
    LPORT = input(" [LPORT] > ")
    
    print("[...] Starting the ncat listener in progress...")
    time.sleep(2)
    os.system(f"ncat -lnvp {LPORT}")
    
MEDUSA_SERVER()
