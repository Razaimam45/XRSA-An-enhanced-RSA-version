#Modified RSA code for Performance Check
import time

#key gen start----------------------------------------
start_key_gen_time = time.time()
# print("Key Generation:\n");
A = 5; # p & q generation
B = 7;

print("Is A=",A, "prime ? ", is_prime(A));
print("Is B=",B,"prime ?",is_prime(B));

N = A*B; # evaluating n
print("\nN=",N);

phi_N = (A-1)*(B-1); # evaluating phi
print("phi_N=", phi_N)

k1 = ZZ.random_element(phi_N)
while (gcd(k1, phi_N) != 1 or ((N**0.5) < k1 < phi_N)==False):
    k1 = ZZ.random_element(phi_N) #choosing k1
print("\nk1=",k1);
print("*√N < k1 < phi_N=",(N**0.5) < k1 < phi_N) #checking conditions for k1
print("*gcd(k1,phi_N)=",gcd(k1,phi_N))

X = ZZ.random_element(N)
if(A>B):
    while (gcd(X,N) != 1 or ((N-A) < X < N)==False):
        X = X = ZZ.random_element(N)
    print("\nX=",X)
    print("*gcd(X,N)=",gcd(X,N))
    print("*N-A < X < N",(N-A) < X < N)

elif(A<B):
    while (gcd(X,N) != 1 or ((N-B) < X < N)==False):
        X = X = ZZ.random_element(N)
    print("\nX=",X)
    print("*gcd(X,N)=",gcd(X,N))
    print("*N-B < X < N",(N-B) < X < N)


k2 = inverse_mod(k1, X) #finding corresponding d, s.t. e*d = 1*mod(phi)
print("\nk2=",k2);

# X=29
# k1=5
# k2=6
print("\npublic key = (",X,", ",k1,")"); #Generated Key pairs
print("private key = (",X,", ",k2,")\n");
final_key_gen_time = time.time() 
#key gen finish------------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )


#Encryption start--------------------------------------------
start_encrypt_time = time.time()
# print("Encryption & Decryption:\n"); 
PT = 3; print("original msg=",PT) #original message m
CT = power_mod(PT,k1,X); print("encrypted msg=",CT) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
PT = (power_mod(CT,k2,X))**0.5 # decrypting 
print("decrypted msg=",PT)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seconds: ", total_decrypt_time )


total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
print("\nIs decrypted msg & original msg same?", (PT==3*1.0))