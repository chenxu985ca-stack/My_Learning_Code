import random
import string

# chars = "0123456789abcdefghijklmnopqrstuvwxyz"

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


def encrypt(encrypt_code):
    # encrypt_code = input("请输入要加密的文字: ")
    ciper_code = ""

    for letter in encrypt_code:
        index = chars.index(letter)
        ciper_code += key[index]

    print(f"需要加密的文字：{encrypt_code}")
    print(f"加密后的文字：{ciper_code}")


def decrypt(decryt_code):
    # decryt_code = input("请输入要解密的文字: ")
    reciper_code = ""
    for letter in decryt_code:
        index = key.index(letter)
        reciper_code += chars[index]

    print(f"需要解密的文字： {decryt_code}")
    print(f"解密后的文字：{reciper_code}")


def encrypt_decrype():
    encrypt_code = input("请输入要加密的文字: ")
    ciper_code = ""

    for letter in encrypt_code:
        index = chars.index(letter)
        ciper_code += key[index]

    print(f"需要加密的文字：{encrypt_code}")
    print(f"加密后的文字：{ciper_code}")

    decryt_code = input("请输入要解密的文字: ")
    reciper_code = ""
    for letter in decryt_code:
        index = key.index(letter)
        reciper_code += chars[index]

    print(f"需要解密的文字： {decryt_code}")
    print(f"解密后的文字：{reciper_code}")


encrypt_decrype()
