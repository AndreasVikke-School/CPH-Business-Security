import hashlib, binascii, argparse

def md5_encrypt(password):
    return hashlib.md5(password.encode())

def sha_encryption(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), b'salt', 100000)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that encrypts a password')
    parser.add_argument('password', help='password to encrypt')
    parser.add_argument('-encryption', "-e", default='md5', help='encryption type md5 or sha')
    args = parser.parse_args()

    if args.encryption == 'md5':
        print(md5_encrypt(args.password).hexdigest())
    else:
        print(binascii.hexlify(sha_encryption(args.password)))