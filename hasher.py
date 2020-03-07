import hashlib


def get_hash(filepath):
    with open(filepath, 'rb') as f:
        while True:
            text = f.readline()
            if text:
                yield hashlib.md5(text).hexdigest()
            else:
                break
