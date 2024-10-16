from Crypto.Util import number
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

pu, pr = gen_pair(2048)


m1= 500

e1 = pow(m1, pr[1], pr[0])

print(f"Encrypted {m1} - {e1}")

m2 = 100

e2 = pow(m2, pr[1], pr[0])

print(f"Encrypted {m2} - {e2}")

e3 = (e2 * e1) % pu[0]

print(f"Calculated signature for {m2 * m1} - {e3}")

d = pow(e3, pu[1], pu[0])

print(f"Decrypted {d}")


