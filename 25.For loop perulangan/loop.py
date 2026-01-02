# for loop perulangan

# contoh jika di pikirkan 
# for kondisi:
#   aksi

# [] ini adalah list list adalah sebuah kotak yang fungsi nya menyimpan sebuah nilai 
angka2 = [0,1,2,3,4]
print(angka2) # output nya akan mengikuti kotak yang berisi nilai


# Contoh Pertama (for i in variabel) 
##########################################################################################################
# untuk menggunakan syntax for i adalah ini 
for i in angka2:    # ini artinya variabel angka2 atau value dari angka2 maka akan dijadikan sebuah i 
                    # artinya setiap perulangan i adalah value dari variabel2 = 0 1 2 3 4
    print(f"i sekarang adalah --> {i}") # output angka2 yang di panggil secara berulang = 0 1 2 3 4
print("Program Selesai1\n")    # ini adalah output ketika program diatas telah selesai berjalan

# maka kode akan berjalan sebanyak dari isi [] dan dikeluarkan dalam bentuk output i 
##########################################################################################################




# Contoh Kedua (range  = (5) )
##########################################################################################################
angka_range = range(5) # Set urutan angka menggunakan range = 5 artinya saat menggunakan loop dia akan mengeluarkan output  5 kali dari 0 
for i in angka_range:
     print(f"i sekarang adalah --> {i}")    # output nya maka akan mengeluarkan apa yang ada di angka_range yaitu range(5)
print("Program Selesai2\n")   # output nya dari 0 sampai 5 ngingat range hanya berisi (5) jika lebih output loop nya akan lebih
##########################################################################################################





# Contoh ketiga (range = (0,0))
##########################################################################################################
angka_range = range(1,5) #  Set angka 1,5 ini berarti saat di jalankan perulangan maka output nya berjalan dari 1 sampai 4  
for i in angka_range:
    print(f"i sekarang adalah --> {i}")
print("Program  Selesai3\n")    # maka output nya hanya mengeluarkan dari 1 sampai 4 , 5 nya tidak dikarenakan aturan loop pada python 
##########################################################################################################





# Contoh for i dalam string 
##########################################################################################################
data_str = 'saya ganteng habis'
for huruf in data_str:  # bagian i ini bisa kita ganti menggunakan huruf lain
    print(huruf)    # Maka yang akan terjadi di kode ini dia akan mengeluarkan output secara bagian per bagian dari variabel data_str dari atas sampai bawah
print('Program Selesai4')
##########################################################################################################
