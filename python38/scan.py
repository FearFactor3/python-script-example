#!/bin/python3.6

import subprocess

p = subprocess.Popen(["nmap", "-sV", "--script", "nmap-vulners", "[IP_ADDRESS]", "-p22,80,3306"], stdout=subprocess.PIPE)
(output, err) = p.communicate()
msg = output.decode('utf-8').strip()

subprocess.check_output(['sendemail', '-f', '[FROM_EMAIL]', '-u', 'AUTH_NOTIFICATION', '-t', '[TO_EMAIL]', '-s', 'smtp.gmail.com:587', '-o', 'tls=yes', '-xu', '[USER_NAME]', '-xp', '[PASSWORD]', '-m', msg], stdin=None, stderr=None, shell=False, universal_newlines=False)