#Standard RSA code for Performance Check
import time

#key gen start----------------------------------------
start_key_gen_time = time.time()
# print("Key Generation:\n");
p = generate_prime_number(1024); # p & q generation
q = generate_prime_number(1024);
# print("Bit size p: ",p.nbits())
# print("Bit size q: ",q.nbits())
# print("Is p=",p, "prime ? ", is_prime(p));
# print("Is q=",q,"prime ?",is_prime(q));

n = p*q; # evaluating n
# print("\nn=",n);

phi = (p-1)*(q-1); # evaluating phi
# print("phi=", phi)

e = ZZ.random_element(phi)
while (gcd(e, phi) != 1):
    e = ZZ.random_element(phi) #choosing e
# print("\ne=",e);
# print("*e < phi=",e < phi) #checking conditions for e
# print("*gcd(e,phi)=",gcd(e,phi))
# print("*Is e prime ?", is_prime(e))

d = inverse_mod(e, phi) #finding corresponding d, s.t. e*d = 1*mod(phi)
# print("\nd=",d);
# print("*Is d prime ?", is_prime(d))

# print("\npublic key = (",n,", ",e,")"); #Generated Key pairs
# print("private key = (",n,", ",d,")\n");
final_key_gen_time = time.time() 
#key gen finish------------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )


#Encryption start--------------------------------------------
start_encrypt_time = time.time()
# print("Encryption & Decryption:\n"); 
m = 59; #print("original msg=",m) #original message m
c = power_mod(m,e,n); #print("encrypted msg=",c) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
decrypt_msg = power_mod(c,d,n) # decrypting 
# print("decrypted msg=",decrypt_msg)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seco256nds: ", total_decrypt_time )


total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
print("\nIs decrypted msg & original msg512 same?", (decrypt_msg==m))