
def getMessage():

    print('Enter your message:')
    return input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (26))
        key = int(input())
        if (key >= 1 and key <= 26):
            return key

def translateMessage(message):
    translated = ""
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


message = getMessage()

key = getKey()

cipherm = translateMessage(message)

print(cipherm)