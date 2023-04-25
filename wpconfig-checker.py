import requests
import sys
import os
import colorama
from colorama import Fore

cases={
    "wp-config.php~",
    "*wp-config.php",
    "wp-config.php.tmp",
    ".wp-config.php.swp",
    "wp-config-sample.php",
    "wp-config.inc",
    "wp-config.old",
    "wp-config.txt",
    "wp-config.php.txt",
    "wp-config.php.bak",
    "wp-config.php.old",
    "wp-config.php.dist",
    "wp-config.php.inc",
    "wp-config.php.swp",
    "wp-config.php.html",
    "wp-config.php.zip",
    "wp-config-backup.txt",
    "wp-config.php.save",
    "wp-config.php-backup",
    "wp-config.php.backup",
    "wp-config.php.orig",
    "wp-config.php_orig",
    "wp-config.php.original",
    "_wpeprivate/config.json"
}


if(len(sys.argv)==1):
    print(Fore.YELLOW ,"\n [i] Usage : python {} https://doamin.com/".format(sys.argv[0]))
else:
    print(Fore.GREEN ,"\n [+] Starting Check Wordpress")
    print(Fore.GREEN ,"\n [+] Check Config file")
    counter=0
    for i in cases:
        URL = sys.argv[1]+i

        response = requests.get(URL)
        if("define" in response.text ) and ( response.status_code != 403) and ( response.status_code != 404):
            print(Fore.GREEN ,"\n [+] The Following URL works : " + URL)
            counter=+1

    if(counter == 0):
        print(Fore.RED ,"\n [-] No Result Found")

    print(Fore.GREEN ,"\n [+] Starting Scan Wordpress")
    os.system("sudo wpscan --url {} -e --random-user-agent --no-update ".format(sys.argv[1]))

    print(Fore.GREEN ,"\n [+] Starting check registeration enabled")
    res = requests.get(sys.argv[1]+"wp-register.php" , allow_redirects=False)
    if ("User registration is currently not allowed" in res.text) and (res.status_code == 302) and (res.status_code == 404) and (res.status_code == 301) and (res.status_code != 200):
        print(Fore.RED,"\n [-] Registration Not enable")
    else:
        print(Fore.GREEN,"\n [+] Registration Enabled")
