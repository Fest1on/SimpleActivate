import os
import subprocess
from colorama import Fore, Style

# IT'S A BANNER
banner = '''
█▀ █ █▀▄▀█ █▀█ █░░ █▀▀ ▄▀█ █▀▀ ▀█▀ █ █░█ ▄▀█ ▀█▀ █▀▀
▄█ █ █░▀░█ █▀▀ █▄▄ ██▄ █▀█ █▄▄ ░█░ █ ▀▄▀ █▀█ ░█░ ██▄
'''

# LIST COMMANDS
commands = [
    "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "slmgr /skms kms.digiboy.ir",
    "slmgr /ato"
]

print(Fore.GREEN + banner + Style.RESET_ALL)
print("")
print(Fore.GREEN + "Welcome, my dear friend! If you're here, it means you want to activate Windows for free. Hmm... Well, listen, I'll help you without any problems.")

choice = input("Activate windows? (Y/N): ").strip().upper()

if choice == 'Y':
    for command in commands:
        try:
            # Формируем PowerShell-команду
            cmd = f'powershell -Command "Start-Process cmd -ArgumentList \'/k {command}\' -Verb RunAs"'
            subprocess.run(cmd, shell=True)
        except Exception as e:
            print(Fore.RED + f"ERROR '{command}': {e}" + Style.RESET_ALL)
else:
    print(Fore.CYAN + "You refused to execute the command." + Style.RESET_ALL)