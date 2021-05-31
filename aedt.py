import pyAesCrypt
import os 
import argparse
import pyfiglet


banner = pyfiglet.figlet_format("AEDT", font = "slant")
print(banner)
parser = argparse.ArgumentParser(description="AES Encryption and Decryption Tool")
group = parser.add_mutually_exclusive_group()

group.add_argument('-e','--encrypt', action='store_true',help='Choose Encryption')
group.add_argument('-d','--decrypt', action='store_true',help='Choose Decryption')

parser.add_argument('-k','--key', type=str, metavar='', required=True, help='Enter AES Key')
parser.add_argument('-f','--file', type=str, metavar='', required=True, help='Choose File Name')
parser.add_argument('-o','--output', type=str, metavar='', required=True, help='Choose Ouput File')


args = parser.parse_args()

if args.encrypt:
    key = args.key
    filename = args.file
    
    if os.path.exists(filename):
        output_file = args.output
        pyAesCrypt.encryptFile(filename, output_file, key)
        print('\033[32m' + "Saved: " +os.getcwd() + f"/{output_file}" + "\033[0m ")
    else:
        print('\033[31m' + "Please enter valid filename..." + "\033[0m ")
   
if args.decrypt:
    filename = args.file
    key = args.key
    if os.path.exists(filename):
        output_file = args.output
        try:
            pyAesCrypt.decryptFile(filename, output_file, key)
            print('\033[32m' + "Saved: " +os.getcwd() + f"/{output_file}" + "\033[0m ")
        except:
            print('\033[31m' +"Please enter the correct key..." + "\033[0m ")
    else:
        print('\033[31m' + "Please enter valid filename..." + "\033[0m ")
        

