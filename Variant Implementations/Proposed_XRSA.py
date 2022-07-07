# ************* XRSA Permormance Table Code ***************

# In[20]:
import time

#X RSA Latest code

#key gen start-----------------------------------------------
start_key_gen_time = time.time()
# print("Key Generation:\n");
p1 = generate_prime_number(100)
p2 = generate_prime_number(100)
p3 = generate_prime_number(100)
p4 = generate_prime_number(100)

# print("Bit size p1: ",p1.nbits())
# print("Bit size p2: ",p2.nbits())
# print("Bit size p3: ",p3.nbits())
# print("Bit size p4: ",p4.nbits())
# print("Is p1=",p1, "prime ? ", is_prime(p1));
# print("Is p2=",p2,"prime ?",is_prime(p2));
# print("Is p3=",p3, "prime ? ", is_prime(p3));
# print("Is p4=",p4,"prime ?",is_prime(p4)); #CORRECT


x = p1*p2;
y = p3*p4;
N = x*y; # evaluating N
# print("\nx=",x);
# print("y=",y);
# print("N=",N); #CORRECT

phi_x = (p1-1)*(p2-1); # evaluating Euler Totients: phi
phi_y = (p3-1)*(p4-1);
phi_N = phi_x*phi_y;
# print("phi(x)=", phi_x);
# print("phi(y)=", phi_y);
# print("phi(N)=", phi_N); #CORRECT

    
#=============================================================================#
#CHECK: modified on 06-Aug-2021
E1 = ZZ.random_element(phi_x)
E2 = ZZ.random_element(phi_y)

while(gcd(E1*E2, phi_N) != 1):
    E1 = ZZ.random_element(phi_x)
    E2 = ZZ.random_element(phi_y)
    
print('Is gcd(E1*E2, phi_N) == 1',gcd(E1*E2, phi_N) == 1)    

E_dash = (E1*E2)%N
# print("\nE' = ",E_dash)
#=============================================================================#

D_dash = inverse_mod(E_dash,phi_N)
# print("D' = ",D_dash)

E=(E_dash).__xor__(N); #print("\nE = ",E) #CORRECT
D=(D_dash).__xor__(N); #print("D = ",D) #CORRECT

# print("\npublic key = (",N, ",",E,")"); #Generated Key pairs
# print("private key = (",N, ",",D,")\n");

final_key_gen_time = time.time()
#key gen finish----------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )

#Encryption start------------------------------------------
start_encrypt_time = time.time()
# print("\nENCRYPTION:-------");
M = 59; #print("original msg=",M) #original message M

E_double_dash = (E).__xor__(N); #print("E'' = ",E_double_dash)
C = power_mod(M,E_double_dash,N); #print("encrypted msg=",C) #encrypted message C #CORRECT
finish_encrypt_time = time.time()
#Encryption finish------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start---------------------------------------------
start_decrypt_time = time.time() 
# print("\nDECRYPTION:-------");
D_double_dash = (D).__xor__(N); #print("D'' = ",D_double_dash)
decrypt_msg = power_mod(C,D_double_dash,N) # decrypting  #CORRECT
# print("decrypted msg=",decrypt_msg)
finish_decrypt_time = time.time()
#Decryption finish-------------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seconds: ", total_decrypt_time )

# Total Execution Time
total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)

print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))
