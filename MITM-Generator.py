from random import randrange
from Crypto.Hash import SHA256

from math import log

h = SHA256.new()

base = 1
print(f"Advesary has changed base to {base}")

mod = 0xB10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371

a = randrange(0,50,1)
print (f"A has chosen {a}")

b = randrange(0,50,1)

print(f"B has chosen {b}")
akey = pow(base, a, mod)
bkey = pow(base, b, mod)

print(f"A sends {akey}")
print(f"B sends {bkey}")


asec = pow(bkey, a, mod)
bsec = pow(akey, b, mod)

print(f"A has the key {asec}")
print(f"B has the key {bsec}")

mitm = 1

h.update(bytearray(str(asec), "UTF-8"))


key = h.hexdigest()[0:16]

print(f"Hashed key is {key}")

h = SHA256.new()

h.update(bytearray(str(mitm), "UTF-8"))


print(f"MITM has {h.hexdigest()[0:16]}")
