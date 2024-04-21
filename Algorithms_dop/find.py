import hashlib
import os


hashes = {}


def get_hash(path):
    with open(path, 'rb') as file:
        bytes = file.read()
        readable_hash = hashlib.md5(bytes).hexdigest()
        return readable_hash


def find_duplicates(directory):

    duplicates = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = get_hash(path)
            if file_hash not in hashes:
                hashes[file_hash] = path
            else:
                duplicates.append((path, hashes[file_hash]))
    return duplicates


duplcates = find_duplicates('picture')
for duplcate in duplcates:
    print(f'Filecopies: {duplcate[0]} and {duplcate[1]}')
print(hashes)