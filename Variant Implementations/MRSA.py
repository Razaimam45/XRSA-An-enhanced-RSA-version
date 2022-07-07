import time

# MRSA Latest code

#key gen start-----------------------------------------------
start_key_gen_time = time.time()
# print("Key Generation:\n");
w = generate_prime_number(512)
x = generate_prime_number(512)
y = generate_prime_number(512)
z = generate_prime_number(512)

N = w*x*y*z; # evaluating N

phi_N = (w-1)*(x-1)*(y-1)*(z-1)
# print("phi(x)=", phi_x);
# print("phi(y)=", phi_y);
# print("phi(N)=", phi_N); #CORRECT


e = ZZ.random_element(phi_N);
while (gcd(e, phi_N) != 1):
    e = ZZ.random_element(phi_N) #choosing e
# print("\ne =",e);
# print("*e < phi_N=",e < phi_N); #checking conditions for e
# print("*gcd(e,phi_N)=",gcd(e,phi_N)); #CORRECT

f = ZZ.random_element(phi_N);
while (gcd(f, phi_N) != 1):
    f = ZZ.random_element(phi_N) #choosing e
# print("\nf =",f);
# print("*f < phi_N=",f < phi_N); #checking conditions for e
# print("*gcd(f,phi_x)=",gcd(f,phi_N)); #CORRECT

while True:
    try:
        d = inverse_mod(e, phi_N)
        g = inverse_mod(f, phi_N)
        break
    except:
        continue

# print("\npublic key = (",e, ",",f,",",N,")"); #Generated Key pairs
# print("private key = (",d, ",",g,",",N,")\n");

final_key_gen_time = time.time()
#key gen finish----------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )

#Encryption start------------------------------------------
start_encrypt_time = time.time()
# print("\nENCRYPTION:-------");
M = 59; #print("original msg=",M) #original message M

C = power_mod(power_mod(M,e,N),f,N); #print("encrypted msg=",C) #encrypted message C #CORRECT
finish_encrypt_time = time.time()
#Encryption finish------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start---------------------------------------------
start_decrypt_time = time.time() 
# print("\nDECRYPTION:-------");

decrypt_msg = power_mod(power_mod(C,g,N),d,N) # decrypting  #CORRECT
# print("decrypted msg=",decrypt_msg)
finish_decrypt_time = time.time()
#Decryption finish-------------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seconds: ", total_decrypt_time )

# Total Exe256cution Time
total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)

print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))