import time
#key gen start-----------------------------------------------
w = generate_prime_number(80)
x = generate_prime_number(80)
y = generate_prime_number(80)
z = generate_prime_number(80)
N = w*x*y*z; # evaluating N
phi_N = (w-1)*(x-1)*(y-1)*(z-1)
print("phi(N)=", phi_N); #CORRECT
e = ZZ.random_element(phi_N);
while (gcd(e, phi_N) != 1):
    e = ZZ.random_element(phi_N) #choosing e
f = ZZ.random_element(phi_N);
while (gcd(f, phi_N) != 1):
    f = ZZ.random_element(phi_N) #choosing e
while True:
    try:
        d = inverse_mod(e, phi_N)
        g = inverse_mod(f, phi_N)
        break
    except:
        continue

print("\npublic key = (",e, ",",f,",",N,")"); #Generated Key pairs
print("private key = (",d, ",",g,",",N,")\n");
#Encryption start------------------------------------------
start_encrypt_time = time.time()
# print("\nENCRYPTION:-------");
M = 59; print("original msg=",M) #original message M
C = power_mod(power_mod(M,e,N),f,N); print("encrypted msg=",C) #encrypted message C #CORRECT
finish_encrypt_time = time.time()
#Encryption finish------------------------------------------
#Decryption start---------------------------------------------
# print("\nDECRYPTION:-------");
decrypt_msg = power_mod(power_mod(C,g,N),d,N) # decrypting  #CORRECT
print("decrypted msg=",decrypt_msg)
finish_decrypt_time = time.time()
#Decryption finish-------------------------------------------------
print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))


print("\n\nBrute Attack")
time1 = time.time()
#Method1
e = e
f = f
N = N
C = C

phi_N = euler_phi(N)
print(phi_N)

d = inverse_mod(e, phi_N)
print("Cracked D: ",d)

g = inverse_mod(f, phi_N)
print("Cracked G: ",g)

print(power_mod(power_mod(C,g,N),d,N))
time2 = time.time()

bruteTimetaken = (time2-time1)*1000
print("Cracking via [e*d=1.mod(phi_N)] (in ms)", bruteTimetaken)
