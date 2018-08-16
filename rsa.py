def gcd(a,h):
    temp = 0;
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp

#Two Random Prime Number
p = 3
q = 7

#e stands for encrypt
e = 2

#First part of public key
n = p * q

#Finding other part of public key.
phi = (p-1) * (q-1)

# e must be co-prime to phi and
#smaller than phi.

while e < phi:
    if gcd(e,phi) == 1:
        break
    else:
        e += 1

#Public Key ( n and e)
#Private key (d stands for decrypt)
#choosing d such that it satisfies
#d*e = 1 + k * totient

k = 2
d = (1 + (k*phi))/e
msg = 20

print("Message:",msg)

c = msg ** e

c = c % n

print("C: ",c)

m = c ** d

m = m % n

print("M : ",m)
