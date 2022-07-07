# ************* ESRKGS Permormance Table Code ***************

# In[20]:
import time

#X RSA Latest code

#key gen start-----------------------------------------------
start_key_gen_time = time.time()
# print("Key Generation:\n");
p = generate_prime_number(1024); # 4 prime generation
q = generate_prime_number(1024);
r = generate_prime_number(1024);
s = generate_prime_number(1024);

# print("Is p1=",p1, "prime ? ", is_prime(p1));
# print("Is p2=",p2,"prime ?",is_prime(p2));
# print("Is p3=",p3, "prime ? ", is_prime(p3));
# print("Is p4=",p4,"prime ?",is_prime(p4)); #CORRECT


n = p*q;
m = r*s;
N = n*m; # evaluating N
# print("\nx=",x);
# print("y=",y);
# print("N=",N); #CORRECT


phi_n = (p-1)*(q-1); # evaluating Euler Totients: phi
phi_m = (p-1)*(s-1);
phi_N = phi_n*phi_m;
# print("phi(n)=", phi_n);
# print("phi(m)=", phi_m);
# print("phi(N)=", phi_N); #CORRECT


#E1, E2 calculation
e1 = ZZ.random_element(phi_n);
while (gcd(e1, phi_n) != 1):
    e1 = ZZ.random_element(phi_n) #choosing e1
# print("\ne1 =",e1);
# print("*E1 < phi_n=",e1 < phi_n); #checking conditions for e1
# print("*gcd(E1,phi_m)=",gcd(e1,phi_m)); #CORRECT

e2 = ZZ.random_element(phi_m)
while (gcd(e2, phi_m) != 1):
    e2 = ZZ.random_element(phi_m) #choosing e2
# print("\ne2 =",e2);
# print("*e2 < phi_m=",e2 < phi_m) #checking conditions for e2
# print("*gcd(e2,phi_m)=",gcd(e2,phi_m)) #CORRECT

E1 = power_mod(e1,e2,N)
# print("\nE1=",E1); #CORRECT

E = ZZ.random_element(phi_N*E1)
while (gcd(E, phi_N*E1) != 1):
    E = ZZ.random_element(phi_N*E1) #choosing e2
# print("\nE=",E); #CORRECT
# print("\nE bits",E.nbits())

D = inverse_mod(E,phi_N*E1)
# print("\nD=",D); #CORRECT
# print("\nD bits",D.nbits())

# small n is the component here
# print("\npublic key = (",n, ",",E,")"); #Generated Key pairs
# print("private key = (",n, ",",D,")\n");

final_key_gen_time = time.time()
#key gen finish----------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )

#Encryption start--------------------------------------------
start_encrypt_time = time.time()
# print("Encryption & Decryption:\n"); 
M = 59; #print("original msg=",M) #original message m
C = power_mod(M,E,n); #print("encrypted msg=",C) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
decrypt_msg = power_mod(C,D,n) # decrypting 
# print("decrypted msg=",decrypt_msg)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seco256nds: ", total_decrypt_time )


total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))