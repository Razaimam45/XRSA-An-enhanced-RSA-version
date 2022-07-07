#Multiplicity RSA code performance
import time

#key gen start----------------------------------------
start_key_gen_time = time.time()
p = generate_prime_number(1024); # p & q generation
q = generate_prime_number(1024);

n = p*q; # evaluating n
# print("\nn=",n);

phi = (p-1)*(q-1); # evaluating phi
# print("phi=", phi)

e_list=[]
for i in range(3):
    ei = ZZ.random_element(phi)
    while (gcd(ei, phi) != 1):
        ei = ZZ.random_element(phi) #choosing e
    e_list.append(ei)
#     print("\ne_",i+1,"=",ei);
#     print("*ei < phi=",ei < phi) #checking conditions for e
#     print("*gcd(e1,phi)=",gcd(ei,phi))

# print(e_list)

d_list=[]
for i in range(3):
    temp=xgcd(phi,e_list[i])[2]
    di = temp%phi #finding corresponding d, s.t. e*d = 1*mod(phi)
    d_list.append(di)
#     print("\nd_",i+1,"=",di);
# print(d_list)

# print("\npublic key list = (",n,", ",e_list,")"); #Generated Key pairs
# print("private key list = (",n,", ",d_list,")\n");
final_key_gen_time = time.time() 
#key gen finish------------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )


# Encryption start--------------------------------------------
start_encrypt_time = time.time()
M = 59; #print("original msg=",m)
for i in range(3):
    c = power_mod(M,e_list[i],n); #print("encrypted msg=",c)
    M = c
    
# print("c=",c)    
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt time taken in seconds: ", total_encrypt_time )

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
for i in range(3):
    d = d_list[-1-i] #to fetch the last element of d_list
    M = power_mod(c, d, n)
    c=M
    
# print("M=",M)
# print("decrypted msg=",decrypt_msg)#
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seco256nds: ", total_decrypt_time )


total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
print("\nIs decrypted msg & original msg same?", (M==59))