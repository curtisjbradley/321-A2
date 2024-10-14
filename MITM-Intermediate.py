from random import randrange
from Crypto.Hash import SHA256

from math import log

h = SHA256.new()

base = 0xA4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5

mod = 0xB10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371

a = randrange(0,50,1)
print (f"A has chosen {a}")

b = randrange(0,50,1)

print(f"B has chosen {b}")
akey = pow(base, a, mod)
bkey = pow(base, b, mod)

print(f"A sends {akey}")
print(f"B sends {bkey}")

print(f"MITM intercepts and sends {mod} to A")
print(f"MITM intercepts and sends {mod} to B")

asec = pow(mod, a, mod)
bsec = pow(mod, b, mod)

print(f"A has the key {asec}")
print(f"B has the key {bsec}")

mitm = 0

h.update(bytearray(str(asec), "UTF-8"))


key = h.hexdigest()[0:16]

print(f"Hashed key is {key}")

h = SHA256.new()

h.update(bytearray(str(mitm), "UTF-8"))


print(f"MITM has {h.hexdigest()[0:16]}")
