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

print(gen_pair(2048))
