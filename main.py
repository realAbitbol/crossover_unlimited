"""
This script should give you enough crossover trial time for you and your kids :)
"""
import subprocess
import time
from os import environ,getcwd
getUser = lambda: environ["USERNAME"] if "C:" in getcwd() else environ["USER"]
user = getUser()

plist = f"/Users/{user}/Library/Preferences/com.codeweavers.CrossOver.plist"
subprocess.Popen([f"plutil -convert xml1 {plist}"], shell=True, stdout=subprocess.PIPE, encoding="utf", errors="ignore")
time.sleep(0.1)

with open(f'{plist}', 'r') as fp:
    textfile = fp.readlines()
    counter = 0
    for line in textfile:
        word = '<date>'
        counter += 1
        if word in line:
            textfile[counter-1] = "        <date>2150-01-01</date>\n"
            with open(f'{plist}', 'w') as file:
                file.writelines(textfile)