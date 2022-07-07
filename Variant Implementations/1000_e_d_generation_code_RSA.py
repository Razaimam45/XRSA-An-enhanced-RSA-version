#Standard RSA code for Burp Test
import time
# file=open("e_stdRSA_file.txt","w")
file=open("d_stdRSA_file.txt","w")

for i in range(1000):
    #key gen start----------------------------------------
    start_key_gen_time = time.time()
    # print("Key Generation:\n");
    p = generate_prime_number(1024); # p & q generation
    q = generate_prime_number(1024);

    n = p*q; # evaluating n
    # print("\nn=",n);

    phi = (p-1)*(q-1); # evaluating phi
    # print("phi=", phi)

    e = ZZ.random_element(phi)
    while (gcd(e, phi) != 1):
        e = ZZ.random_element(phi) #choosing e
#     print("e=",e)
#     file.write(str(e)+"\n")

    d = inverse_mod(e, phi) #finding corresponding d, s.t. e*d = 1*mod(phi)
#     print("d=",d)
    file.write(str(d)+"\n")

    final_key_gen_time = time.time() 
    #key gen finish------------------------------------------------

    total_key_gen_time = final_key_gen_time - start_key_gen_time
#     print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )


    #Encryption start--------------------------------------------
    start_encrypt_time = time.time()
    m = 59; #original message m
    c = power_mod(m,e,n); #encrypted message c
    finish_encrypt_time = time.time()
    #Encryption finish---------------------------------------------

    total_encrypt_time = finish_encrypt_time - start_encrypt_time
#     print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

    #Decryption start----------------------------------------------
    start_decrypt_time = time.time() 
    decrypt_msg = power_mod(c,d,n) # decrypting 
    finish_decrypt_time = time.time()
    #Decryption finish----------------------------------------------

    total_decrypt_time = finish_decrypt_time - start_decrypt_time
#     print("\nTotal decrypt time taken in seco256nds: ", total_decrypt_time )


    total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
    print(i,"\n\nTotal algorithm time taken in seconds: ", total_time_taken)
#     print("\nIs decrypted msg & original msg512 same?", (decrypt_msg==m))
file.close()