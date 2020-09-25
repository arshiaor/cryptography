import cryptography, sys, subprocess, time
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'termcolor'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyfiglet'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'animation'])


import pyfiglet
from colorama import init
import termcolor,animation

init()


@animation.wait('bar')
def wait():
    time.sleep(2.5)


def line():
    for i in range(30):
        print(termcolor.colored("-", "blue"), end="")
    print("\n")


print(termcolor.colored(pyfiglet.figlet_format("Arshiaor"), color="cyan"))

end = "start"
while end != "exit":
    print(termcolor.colored("1. Encrypt", "yellow"))
    print(termcolor.colored("2. Decrypt", "yellow"))
    print(termcolor.colored("for quitting type exit", "yellow"))
    choice = input()
    if choice == "exit":
        break
    else:
        choice = int(choice)
        if choice == 1:
            message = input("type your message: ").encode()
            file = open('key.key', 'rb')
            key = file.read()
            file.close()
            f = Fernet(key)
            try:
                encrypted = f.encrypt(message)
                print("Proccessing", end="")
                wait()
                print(termcolor.colored("Encryption Successfull!", "green"))
                print(termcolor.colored("Your Encrypted code ", "yellow"), termcolor.colored("{", "cyan"),
                      encrypted.decode(), termcolor.colored("}", "cyan"))
                line()
            except InvalidToken as e:
                print(termcolor.colored("invalid key- Encryption Unsuccessfull", "red"))
                line()
        elif choice == 2:
            file = open('key.key', 'rb')
            key = file.read()
            file.close()
            message1 = input("your code: ").encode()
            message2 = bytes(message1)
            f = Fernet(key)
            try:
                decrypted = f.decrypt(message2)
                print("Proccessing", end="")
                wait()
                print(termcolor.colored("Decryption Successfull!", "green"))
                print(termcolor.colored("Your Decrypted code ", "yellow"), termcolor.colored("{", "cyan"),
                      decrypted.decode(), termcolor.colored("}", "cyan"))
                line()
            except InvalidToken as e:
                print(termcolor.colored("invalid key- Decryption Unsuccessfull!", "red"))
                line()
    continue
.