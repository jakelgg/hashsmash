import sys, os, hashlib, pyfiglet, getopt
from datetime import datetime


toDecrypt = ''
toEncrypt = ''
passwordFile = ''
algorithm=''

algorithmList = False
helpPage = False

banner = pyfiglet.figlet_format('HASHSMASH')
crackedBanner = pyfiglet.figlet_format('HASHSMASHED!!!')


def clearScreen():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def usage():

    global banner

    clearScreen()
        
    print(banner)
    print()
    print('  Password encryption and decryption tool.\n')
    print('  -h --help             - Help menu')
    print('  -l --list             - List of algorithms')
    print('  --algorithm=md5       - Define algorithm')
    print('  --decrypt=hash        - Decrypt a hash')
    print('  --encrypt=string      - Encrypt a string')
    print('  --passfile=path       - Defines path to password file\n')
    print('  Examples:\n')
    print('  hashsmash.py -s')
    print("  hashsmash.py --algorithm=md5 --encrypt=string")
    print("  hashsmash.py --algorithm=sha256 --decrypt=hash --passfile=passfiles/rockyou.txt\n")


def listAlgorithms():

    global banner

    clearScreen()

    print(banner)
    print()
    print('   - md5\n   - sha1\n    - sha256\n   - sha384\n   - sha512\n')
    print('   Examples:  --algorithm=sha256  --algorithm=md5\n')


def md5decrypt():

    startTime = datetime.now()
    global algorithm, toDecrypt, passwordFile, banner, crackedBanner
    line = 0
    passwordFile = open(passwordFile, 'r', errors='ignore')
    
    for word in passwordFile:
        word = word.rstrip("\n")
        hashedGuess = hashlib.md5(word.encode()).hexdigest()
        line += 1

        if hashedGuess == toDecrypt:

            clearScreen()

            print(crackedBanner)
            print("  The password is", str(word), '  ', toDecrypt)
            endTime = datetime.now()
            print('  Time elapsed: ', endTime-startTime)
            quit()

        elif hashedGuess != toDecrypt:
            print('  ', line, "   ", str(word), ' '*7, hashedGuess, '\n')

        else:
            clearScreen()
            print(banner)
            print("  Didn\'t find a match to the hash.")


def sha1decrypt():

    startTime = datetime.now()
    global algorithm, toDecrypt, passwordFile, banner, crackedBanner
    line = 0
    passwordFile = open(str(passwordFile), 'r', errors='ignore')
    
    for word in passwordFile:
        word = word.rstrip("\n")
        hashedGuess = hashlib.sha1(word.encode()).hexdigest()
        line += 1

        if hashedGuess == toDecrypt:

            clearScreen()
            print(crackedBanner)
            print("  The password is", str(word), '  ', toDecrypt)
            endTime = datetime.now()
            print('  Time elapsed: ', endTime-startTime)
            quit()

        elif hashedGuess != toDecrypt:
            print('  ', line, "   ", str(word), ' '*7, hashedGuess, '\n')

        else:
            clearScreen()
            print(banner)
            print("  Didn\'t find a match to the hash.")


def sha256decrypt():

    startTime = datetime.now()
    global algorithm, toDecrypt, passwordFile, banner, crackedBanner
    line = 0
    passwordFile = open(str(passwordFile), 'r', errors='ignore')
    
    for word in passwordFile:
        word = word.rstrip("\n")
        hashedGuess = hashlib.sha256(word.encode()).hexdigest()
        line += 1

        if hashedGuess == toDecrypt:

            clearScreen()
            print(crackedBanner)
            print("  The password is", str(word), '  ', toDecrypt)
            endTime = datetime.now()
            print('  Time elapsed: ', endTime-startTime)
            quit()
            
        elif hashedGuess != toDecrypt:
            print('  ', line, "   ", str(word), ' '*7, hashedGuess, '\n')

        else:
            clearScreen()
            print(banner)
            print("  Didn\'t find a match to the hash.")


def sha384decrypt():

    startTime = datetime.now()
    global algorithm, toDecrypt, passwordFile, banner, crackedBanner
    line = 0
    passwordFile = open(str(passwordFile), 'r', errors='ignore')
    
    for word in passwordFile:
        word = word.rstrip("\n")
        hashedGuess = hashlib.sha384(word.encode()).hexdigest()
        line += 1

        if hashedGuess == toDecrypt:
            clearScreen()
            print(crackedBanner)
            print("  The password is", str(word), '  ', toDecrypt)
            endTime = datetime.now()
            print('  Time elapsed: ', endTime-startTime)
            quit()

        elif hashedGuess != toDecrypt:

            print('  ', line, "   ", str(word), ' '*7, hashedGuess, '\n')

        else:
            clearScreen()
            print(banner)
            print("  Didn\'t find a match to the hash.")


def sha512decrypt():

    startTime = datetime.now()
    global algorithm, toDecrypt, passwordFile, banner, crackedBanner
    line = 0
    passwordFile = open(passwordFile, 'r', errors='ignore')
    
    for word in passwordFile:
        word = word.rstrip("\n")
        hashedGuess = hashlib.sha512(word.encode()).hexdigest()
        line += 1

        if hashedGuess == toDecrypt:

            clearScreen()
            print(crackedBanner)
            print("  The password is", str(word), '  ', toDecrypt)
            endTime = datetime.now()
            print('  Time elapsed: ', endTime-startTime)
            quit()

        elif hashedGuess != toDecrypt:
            print('  ', line, "   ", str(word), ' '*7, hashedGuess, '\n')

        else:
            clearScreen()
            print(banner)
            print("  Didn\'t find a match to the hash.")


def md5encrypt():

    global toEncrypt, algorithm, banner

    clearScreen()
    print(banner)
    word = toEncrypt.encode('utf8')
    print('  ', toEncrypt, '   ', hashlib.md5(word).hexdigest())


def sha1encrypt():

    global toEncrypt, algorithm, banner

    clearScreen()
    print(banner)
    word = toEncrypt.encode('utf8')
    print('  ', toEncrypt, '   ', hashlib.sha1(word).hexdigest())


def sha256encrypt():

    global toEncrypt, algorithm, banner

    clearScreen()
    print(banner)
    word = toEncrypt.encode('utf8')
    print('  ', toEncrypt, '   ', hashlib.sha256(word).hexdigest())


def sha384encrypt():

    global toEncrypt, algorithm, banner

    clearScreen()
    print(banner)
    word = toEncrypt.encode('utf8')
    print('  ', toEncrypt, '   ', hashlib.sha384(word).hexdigest())

def sha512encrypt():

    global toEncrypt, algorithm, banner

    clearScreen()
    print(banner)
    word = toEncrypt.encode('utf8')
    print('  ', toEncrypt, '   ', hashlib.sha512(word).hexdigest())


def main():

    global toDecrypt, toEncrypt, passwordFile, algorithm, banner, crackedBanner, opts, args, algorithmList, helpPage

    if not len(sys.argv[1:]):
        usage()

    try: 
        opts, args = getopt.getopt(sys.argv[1:], "hla:d:e:p:", 
        ["help","list","algorithm=","decrypt=","encrypt=","passfile="])

    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ('-h','--help'):
            helpPage = True

        elif o in ('-l','--list'):
            algorithmList = True
        elif o in ('-a','--algorithm'):
            algorithm = str(a)

        elif o in ('-d','--decrypt'):
            toDecrypt = str(a)

        elif o in ('-e','--encrypt'):
            toEncrypt = str(a)

        elif o in ('-p','--passfile'):
            passwordFile = str(a)

        else: 
            usage()
            print('Unhandled option.')
            sys.exit()

    if len(algorithm) > 8:
        print("Invalid algorithm.")

    elif len(toDecrypt) == 32:
        md5decrypt()

    elif len(toDecrypt) == 40:
        sha1decrypt()

    elif len(toDecrypt) == 64:
        sha256decrypt()

    elif len(toDecrypt) == 96:
        sha384decrypt()
    
    elif len(toDecrypt) == 128:
        sha512decrypt()
    
    elif algorithm.lower() == 'md5' and len(toEncrypt) != 0:
        md5encrypt()

    elif algorithm.lower() == 'sha1' and len(toEncrypt) != 0:
        sha1encrypt()
    
    elif algorithm.lower() == 'sha256' and len(toEncrypt) != 0:
        sha256encrypt()

    elif algorithm.lower() == 'sha384' and len(toEncrypt) != 0:
        sha384encrypt()

    elif algorithm.lower() == 'sha512' and len(toEncrypt) != 0:
        sha512encrypt()

    elif helpPage == True:
        usage()

    elif algorithmList == True:
        listAlgorithms()

    else:
        print()
        print(" "*4, "Invalid arguments.")

   
main()