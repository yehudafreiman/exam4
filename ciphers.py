def encode_ceaser(decode, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encode = ''
    decode = decode.lower()
    for i in decode:
        if i in alphabet:
            encode += alphabet[alphabet.index(i) + offset]
        else:
            encode += i
    return encode.upper()


def decode_ceaser(encode, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    decode = ''
    encode = encode.lower()
    for i in encode:
        if i in alphabet:
            decode += alphabet[alphabet.index(i) - offset]
        else:
            decode += i
    return decode.upper()


def encode_fence(decode):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encode = ''
    decode = decode.lower()
    decode = decode.replace(" ", "")
    for i,l in enumerate(decode):
        if l in alphabet:
            if i % 2 == 0:
                encode += l
            else:
                continue
    for i,l in enumerate(decode):
        if l in alphabet:
            if i % 2 != 0:
                encode += l
            else:
                continue
    return encode.upper()

def decode_fence(encode):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    decode = ''
    encode = encode.lower()
    for i in encode:
        if i in alphabet:
            decode += alphabet[alphabet.index(i)]
        else:
            decode += i
    return decode.upper()
