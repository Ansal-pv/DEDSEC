import subprocess
import pyfiglet
text = pyfiglet.figlet_format("DEDSEC")
print(text)
print("Enter an ip or website")
i = input()
subprocess.call("ping "+ i ,shell=True)