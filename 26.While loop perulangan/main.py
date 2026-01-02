# while loop perulangan

# menggunakan syntax while
# while kondisi:
#   aksi:
#   aksi2:
#akhir dari program


# Contoh 1 
# ketika menggunakan syntax while dia akan membuat loop dari angka 10 berulang ulang  
#angka = 10 # kondisi ini dan 
#while angka > 5: # kondisi ini adalah true karena 10 masih lebih besar dari 5 dan karena kondisi true ini 
    #print("halo dari while loop") # sehingga membuat loop dari str halo dari while loop yang tidak akan berhenti

#print("Akhir dari program")


# Contoh 2 
angka = 0 # set angka = 0 
print(f"angka sekarang {angka}") # kode ini sebenarnya berjalan dari 0 angka 0 juga sebenarnya ikut di eksekusi
while angka < 5: # true dikarenakan 0 lebih dari 5 sehingga perulangan dimulai 
    angka += 1 # setiap loop karena kondisi 0 < 5 adalah true maka 
    print(f"angka sekarang {angka}")
    print("halo dari while loop") # akan mengeluarkan output sebanyak 5 kali 
print("akhir dari program") # print akhir ketika loop diatas sudah di jalankan

# kode diatas adalah contoh loop jika khasus ny a < maka hasil ketika loop akhir dia akan berhenti dan print di akhir di eksekusi
# kalau menggunakan <= maka dia aka true
