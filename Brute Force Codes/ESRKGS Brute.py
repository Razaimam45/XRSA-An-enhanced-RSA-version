# ************* ESRKGS Permormance Table Code ***************
import time
#key gen start-----------------------------------------------
p = generate_prime_number(80)
q = generate_prime_number(80)
r = generate_prime_number(80)
s = generate_prime_number(80)
n = p*q;
m = r*s;
N = n*m; # evaluating N
print("N=",N); #CORRECT
phi_n = (p-1)*(q-1); # evaluating Euler Totients: phi
phi_m = (p-1)*(s-1);
phi_N = phi_n*phi_m;
print("phi(N)=", phi_N); #CORRECT
#E1, E2 calculation
e1 = ZZ.random_element(phi_n);
while (gcd(e1, phi_n) != 1):
    e1 = ZZ.random_element(phi_n) #choosing e1
e2 = ZZ.random_element(phi_m)
while (gcd(e2, phi_m) != 1):
    e2 = ZZ.random_element(phi_m) #choosing e2
print('Is gcd(e1*e2, phi_N) == 1',gcd(e1*e2, phi_N) == 1)    
E1 = power_mod(e1,e2,N)
# print("\nE1=",E1); #CORRECT
E = ZZ.random_element(phi_N*E1)
while (gcd(E, phi_N*E1) != 1):
    E = ZZ.random_element(phi_N*E1) #choosing e2
# print("\nE=",E); #CORRECT
D = inverse_mod(E,phi_N*E1)
# print("\nD=",D); #CORRECT
# small n is the component here
print("\npublic key = (",n, ",",E,")"); #Generated Key pairs
print("private key = (",n, ",",D,")\n");
#key gen finish----------------------------------------------
#Encryption start--------------------------------------------
start_encrypt_time = time.time()
# print("Encryption & Decryption:\n"); 
M = 59; print("original msg=",M) #original message m
C = power_mod(M,E,n); print("encrypted msg=",C) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
decrypt_msg = power_mod(C,D,n) # decrypting 
print("decrypted msg=",decrypt_msg)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))


#Method 1 #Thanks to this paper "Comment on “An Enhanced and Secured RSA Key Generation Scheme (ESRKGS)”"

#Since N is a multiple of n
#Therefore, phi_N is a multiple of phi_n
#So, GCD(E, phi_N)=1, and hence, E has an inverse in mod(phi_n), let's say it as D1

print("\n\nBRUTE ATTACK")#-----------------------------------------
time1 = time.time()

E = E
n = n
C = C

phi_n = euler_phi(n)
print("phi_n:",phi_n)

D1 = inverse_mod(E, phi_n)
print("D1:",D1)

decrypt_msg = power_mod(C,D1,n)
print(decrypt_msg)
time2 = time.time()

bruteTimetaken = (time2-time1)*1000
print("Cracking via [e*d=1.mod(phi_N)] (in ms):", bruteTimetaken)
