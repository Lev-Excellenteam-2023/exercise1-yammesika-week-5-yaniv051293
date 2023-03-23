

def find_secret_messages(filename):
    """
    Finds all secret messages in the resources/logo.jpg file.
    The messages are strings of at least 5 letters, written in lowercase English letters
    only and ending with an exclamation mark.
    :return:
    """
    with open(filename, 'rb') as f:
        data = f.read()

    message = ""
    for byte in data:
        if ord('a') <= byte <= ord('z'):
            message += chr(byte)
        elif byte == ord('!') and len(message) >= 5:
            message += '!'
            yield message
            message = ""
        else:
            message = ""


def main():
    for word in find_secret_messages("logo.jpg"):
        print(word)


if __name__ == '__main__':
    main()
