# Latihan Perulangan membuat Segitiga


# *
# **
# ***
# ****

print("menggunakan for")

# 1.MENGGUNAKAN FOR I IN RANGE(VARIABELRANGE):
loop_perbagian = 4          # setiap baris akan memiliki 4 loop 
loop_sisi = 1               # setiap baris akan di tambah 1 

for i in range(loop_perbagian):     # membuat loop 4 baris 
    print("*"*loop_sisi)
    loop_sisi +=1                   # setiap loop akan di tambah 1 

print(" ")



# 2.VARIABEL SIMPEL TANPA MENGGUNAKAN VARIABEL  
# MENGGUNAKAN FOR I IN RANGE(ANGKA):
loop_perbagian = 1 

for i in range(4):          # membuat 4 baris didalam loop 
    print("*"*loop_perbagian)
    loop_perbagian +=1      # setiap loop akan di tambah 1

print(" ")



# *
# **
# ***
# ****
# 3.MENGGUNAKAN WHILE
print("menggunakan while dan if tanpa kondisi dan break")
baris_loop = 5      # setiap baris akan memiliki 

loop = 1 

while True:         # jika kondisi  
    print("*"*loop)
    loop += 1 

    if loop > baris_loop:   # harus dalam kondisi false 
        break # dan harus ada kondisi setelah if 


print(" ")


# 4.MEMANGGIL GANJIL SAJA 
# WHILE LOOP GANJIL 
# *
        # genap = false +1 = 3 
# ***
        # genap = false +1 = 5 
# *****
        # genap = false + 1 = 7
# *******
        # genap = false + 1 = 9  
# *********
        # genap = false +1 = 11  
# ***********

print("hanya menampilkan ganjil saja")


baris_loop = 10 
loop = 1 

while True:

    # bagian ini menentukan logic untuk menentukan angka ganjil dengan menggunakan operattor modulo %
    if (loop%2):
        print('*'*loop)
        loop +=1 
    
    # memaksa program langsung ke kondisi awal loop
    else:
        loop +=1 
        continue

   # kondisi ini cek jika per loop sudah di tambah 1 / sudah melewati angka 12 maka akan berhenti  
    if loop > baris_loop:
        break

        

print(" ")



# 5.MEMBUAT SPASI DI KODE GANJIL
# DAN MEMBUAT KE TENGAH SUATU STR MENGGUNAKAN WHILE LOOP 
print("membuat spasi loop")
baris_loop = 10 
loop = 1
spasi = int(baris_loop/2) # membuat variabel baru dan di konversi ke integer

while True:
    if (loop%2):
        print(" "*spasi,"*"*loop) # string kosong yang dikali variabel spasi

        spasi -=1 # memanggil spasi lalu di tambah 1 ini akan membuat * ke tengah 
        loop +=1 

    else:
        loop+=1 
        continue


    if loop > baris_loop:
        break

