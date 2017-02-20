#!/usr/bin/env python3

"""problem_059.py

Problem 59: XOR decryption

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using INPUT_FILE, a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

INPUT_FILE = '../input/059.txt' # default: '../input/059.txt'

# SOLUTION ####################################################################

def decrypt_message(message, key):
    """Returns the result of XOR decrypting message with the given key."""
    decrypted = []
    key_len = len(key)
    for i, byte in enumerate(message):
        decrypted_char = chr(ord(byte) ^ ord(key[i % key_len]))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)


def solve():
    # sequence that should occur if the message is properly decrypted
    target_seq = ' the '

    # create the encrypted message from the file
    byte_vals = next(com.ints_from_file(INPUT_FILE, sep=','))
    encrypted = ''.join(chr(byte) for byte in byte_vals)

    # try each possible key and look for target sequence in message
    for i in range(1, 27):
        for j in range(1, 27):
            for k in range(1, 27):
                key = ''.join([
                    com.alpha_char_lower(i),
                    com.alpha_char_lower(j),
                    com.alpha_char_lower(k),
                ])

                # decrypt message with key and check for target sequence
                decrypted = decrypt_message(encrypted, key)
                if target_seq in decrypted:
                    return sum([ord(char) for char in decrypted])


if __name__ == '__main__':
    print(solve())
