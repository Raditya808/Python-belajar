# elif statement lanjutan dari if else
# elif statement adalah salah satu konsep yang tergabung dengan if dan else 
# elif digunakan jika ingin menambahkan kondisi tambahan setelah if 
# elif bisa giunakan kapan pun sebanyak yang kita mau jika kita memiliki kondisi yang lebih di if dan else 
# penggunaan elif menggunakan == 


# contoh kode 
# if == kondisi:
#       aksi true 
# elif == tambhan kodnisi:
#       aksi true
#
# elif == tambhan kondis2:
#       aksi true
#   
#
# else:
#   aksi 


nama = input("Nama kamu sypaaaa")

# ini adalah kondisi pertama 
if nama == 'ucup':
    print("Kamu ganteng") # aksi true pertama

# ini adalah kondisi kedua 
elif nama == "otong":
    print("hai si kece bangetttt") # aksi true kedua

# ini adalah kondisi ketiga
elif nama == "mario":
    print("halo mario") # aksi true ke tiga



# ini adalah kondisi dimana input tidak valid dan tidak sesuai dengan kondisi pertama dan kedua
# ini adalah kondisi ketiga
else:
    print("Au ah ga kenal!") # aksi false keempat

# ini akan ikut ke print setelah input
print("ini adalah akhir dari program")
