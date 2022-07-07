#Standard RSA code for Performance Check
import time

p = generate_prime_number(50)
q = generate_prime_number(50)
n = p*q; # evaluating n
phi = (p-1)*(q-1); # evaluating phi
e = ZZ.random_element(phi)
while (gcd(e, phi) != 1):
    e = ZZ.random_element(phi) #choosing e
d = inverse_mod(e, phi) #finding corresponding d, s.t. e*d = 1*mod(phi)
print("\npublic key = (",n,", ",e,")"); #Generated Key pairs
print("private key = (",n,", ",d,")\n");
#Encryption start--------------------------------------------
start_encrypt_time = time.time()
m = 59; print("original msg=",m) #original message m
c = power_mod(m,e,n); print("encrypted msg=",c) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------
#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
decrypt_msg = power_mod(c,d,n) # decrypting 
print("decrypted msg=",decrypt_msg)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

time1 = time.time()
#Method1
e = e
n = n
c = c

phi_N = euler_phi(n)
print(phi_N)

d = inverse_mod(e, phi_N)
print("Cracked d: ",d)

print(power_mod(c,d,n))
time2 = time.time()

bruteTimetaken = (time2-time1)*1000
print("Cracking via [e*d=1.mod(phi_N)] (in ms)", bruteTimetaken)