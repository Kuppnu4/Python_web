import hashlib

names = {'Nata': 16, 'Bogdan': 24, 'Nastia': 20}

print(hash('Nata'))
print(hash('Bogdan'))
print(hash('Nastia'))

hashed_nata = hashlib.sha256('Nata'.encode())
print(hashed_nata.digest())
print(hashed_nata.hexdigest())
