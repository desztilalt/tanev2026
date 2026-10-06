import subprocess
from colorama import Fore, Back, Style

for i in range(15):
    print(f"{Fore.GREEN} blablablablablablabla")

input(f"{Fore.RESET}Üss egy billentyűt a folytatáshoz...")

subprocess.run(["cls"], shell=True)

print(f"{Back.RED}{Fore.WHITE}{"PIROS":^20}")
print(f"{Back.RESET}{Fore.BLACK}{"FEHÉR":^20}")
print(f"{Back.GREEN}{Fore.WHITE}{"ZÖLD":^20}")
print(Style.RESET_ALL, end="")

print("abc")