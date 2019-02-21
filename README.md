# Hashsmash

A slow Python hash encryption and decyption tool. I am new to Python and programming in general so I am creating some tools to help develop my skills. I am also using this project to help me get a better understanding of how git works.

## Features

* Algorithms - MD5, SHA1, SHA224, SHA256, SHA384, and SHA512.
* Encrypt with any algorithm
* Decrypt by encrypting file of passwords and comparing hashes.

## Getting Started

Ensure you are using the correct python version. Tested in Python 3.7.2 but should work in any Python 3 verison.

```
python --version
```
You're now ready to clone the project.

### Prerequisites

This tool only uses one module that is not in the Python standard library called Pyfiglet. Install it with the following command.

```
pip install pyfiglet or pip3 install pyfiglet
```

## Using the tool

This tool uses arguments to identify the functions you want to run. Don't forget you can always use -h to get to the help page and -l to get a list of algorithms you can use.

```
python hashsmash.py -h or python hashsmash.py -l
```

### Encryption

To encrypt files using this tool, you need to use the --encrypt= argument and the --alorithm= argument.

```
python hashsmash.py --encrypt=text-to-encrypt --algorithm=md5
```

### Decryption

Decrypt files using three arguments, --decrypt= --algorithm= and --passfile=. The password file must be located in the same directory as the project.

```
python hashsmash.py --decrypt=text-to-decrypt --algorithm=sha256 --passfile=rockyou.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
