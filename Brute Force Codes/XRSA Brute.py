#CORRECTED as of 6 Aug 2021
# ************* XRSA Permormance Table Code ***************
import time

#key gen start-----------------------------------------------
# print("Key Generation:\n");
p1 = generate_prime_number(80)
p2 = generate_prime_number(80)
p3 = generate_prime_number(80)
p4 = generate_prime_number(80)

x = p1*p2;
y = p3*p4;
N = x*y; # evaluating N

phi_x = (p1-1)*(p2-1); # evaluating Euler Totients: phi
phi_y = (p3-1)*(p4-1);
phi_N = phi_x*phi_y; print("phi_N", phi_N)
#=============================================================================#
#CHECK: modified on 06-Aug-2021
E1 = ZZ.random_element(phi_x)
E2 = ZZ.random_element(phi_y)

while(gcd(E1*E2, phi_N) != 1):
    E1 = ZZ.random_element(phi_x)
    E2 = ZZ.random_element(phi_y)
    
print('Is gcd(E1*E2, phi_N) == 1',gcd(E1*E2, phi_N) == 1)    

E_dash = (E1*E2)%N
#=============================================================================#
D_dash = inverse_mod(E_dash,phi_N)

print("E_dash",E_dash)
print("D_dash",D_dash)

E=(E_dash).__xor__(N); #print("\nE = ",E) #CORRECT
D=(D_dash).__xor__(N); #print("D = ",D) #CORRECT
#key gen finish----------------------------------------------
print("\npublic key = (",N,", ",E,")"); #Generated Key pairs
print("private key = (",N,", ",D,")\n");

#Encryption start------------------------------------------
M = 59; print("original msg=",M) #original message M
E_double_dash = (E).__xor__(N); #print("E'' = ",E_double_dash)
C = power_mod(M,E_double_dash,N); print("encrypted msg=",C) #encrypted message C #CORRECT
finish_encrypt_time = time.time()
#Encryption finish------------------------------------------

#Decryption start---------------------------------------------
start_decrypt_time = time.time() 
# print("\nDECRYPTION:-------");
D_double_dash = (D).__xor__(N); #print("D'' = ",D_double_dash)
decrypt_msg = power_mod(C,D_double_dash,N) # decrypting  #CORRECT
print("decrypted msg=",decrypt_msg)
finish_decrypt_time = time.time()
#Decryption finish-------------------------------------------------
print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))

print("\n\nBRUTE ATTACK")#-----------------------------------------
time1 = time.time()

E = E
N = N
C = C

E_dash=E.__xor__(N)
print("E_dash:",E_dash)

phi_N = euler_phi(N)
print("phi_N:",phi_N)

D_dash = inverse_mod(E_dash, phi_N)
print("D_dash:",D_dash)

D = D_dash.__xor__(N)

print("Cracked D: ",D)

D_double_dash = (D).__xor__(N); #print("D'' = ",D_double_dash)
decrypt_msg = power_mod(C,D_double_dash,N)
print(decrypt_msg)
time2 = time.time()

bruteTimetaken = (time2-time1)*1000
print("Cracking via [e*d=1.mod(phi_N)] (in ms):", bruteTimetaken)