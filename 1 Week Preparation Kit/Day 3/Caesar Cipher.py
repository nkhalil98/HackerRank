def caesarCipher(s, k):
    encrypted = []
    for char in s:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            encrypted.append(chr((ord(char)-97+k) % 26 + 97))
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            encrypted.append(chr((ord(char)-65+k) % 26 + 65))
        else:
            encrypted.append(char)
    return ''.join(encrypted)