from Crypto.Util import number
from Crypto.Random import random

from Crypto.Hash import SHA256

def mod_inverse(a,m):
    def egcd(a,b):
        if a == 0:
            return b,0,1
        g,y,x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    g,x,_ = egcd(a,m)

    if (g != 1):
        raise Exception("Modular Inverse DNE")
    else:
        return x % m


def gen_prime(bits):
    return number.getPrime(bits)

def gen_pair(bits):
    p = gen_prime(bits // 2)
    q = gen_prime(bits // 2)
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    d = mod_inverse(e,phi)
    
    return ((n,e),(n,d))

pu,pr = gen_pair(2048) 

print(f"Alice sending n,e {pr}")

s = random.randint(1,pu[0])
c = pow(s, 65537, pu[0])
print(f"Bob sending {c}")



print(f"Mallory intercepts, and sends 1")

rec = 1

print(f"Alice receives {rec}")

s = pow(rec,pr[1],pu[0])

h = SHA256.new()

h.update(bytearray(str(s), "UTF-8"))

print(f"Alice computes the key: {h.hexdigest()[0:16]}")

h = SHA256.new()

h.update(bytearray(str(1), "UTF-8"))

print(f"Mallory computes the key: {h.hexdigest()[0:16]}")
