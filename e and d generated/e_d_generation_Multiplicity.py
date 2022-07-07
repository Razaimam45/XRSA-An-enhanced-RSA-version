# ************* Multiplicity Burp Table Code ***************

# In[20]:
import time
file1=open("e_Multiplicity_file.txt","w")
file2=open("d_Multiplicity_file.txt","w")

for i in range(334):
    #key gen start----------------------------------------
    start_key_gen_time = time.time()
    p = generate_prime_number(1024); # p & q generation
    q = generate_prime_number(1024);

    n = p*q; # evaluating n

    phi = (p-1)*(q-1); # evaluating phi
    # print("phi=", phi)

    e_list=[]
    for i in range(3):
        ei = ZZ.random_element(phi)
        while (gcd(ei, phi) != 1):
            ei = ZZ.random_element(phi) #choosing e
            file1.write(str(ei)+"\n")
        e_list.append(ei)

    d_list=[]
    for i in range(3):
        temp=xgcd(phi,e_list[i])[2]
        di = temp%phi #finding corresponding d, s.t. e*d = 1*mod(phi)
        file2.write(str(di)+"\n")
        d_list.append(di)


    final_key_gen_time = time.time() 
    #key gen finish------------------------------------------------

    total_key_gen_time = final_key_gen_time - start_key_gen_time


    # Encryption start--------------------------------------------
    start_encrypt_time = time.time()
    M = 59; #print("original msg=",m)
    for i in range(3):
        c = power_mod(M,e_list[i],n); #print("encrypted msg=",c)
        M = c

    finish_encrypt_time = time.time()
    #Encryption finish---------------------------------------------

    total_encrypt_time = finish_encrypt_time - start_encrypt_time

    #Decryption start----------------------------------------------
    start_decrypt_time = time.time() 
    for i in range(3):
        d = d_list[-1-i] #to fetch the last element of d_list
        M = power_mod(c, d, n)
        c=M

    # print("decrypted msg=",decrypt_msg)#
    finish_decrypt_time = time.time()
    #Decryption finish----------------------------------------------

    total_decrypt_time = finish_decrypt_time - start_decrypt_time


    total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
    print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
    print("\nIs decrypted msg & original msg512 same?", (M==59))
    
file1.close()
file2.close()