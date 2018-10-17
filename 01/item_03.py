import os


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str


def create_binary_file():
    with open('some_binary_file.bin', 'wb') as binary_file:
        binary_file.write(os.urandom(10))

def create_text_file():
    with open('some_text_file.txt', 'wt' ) as text_file:
        text_file.write('Now is the time for us to have fun with text files.')
