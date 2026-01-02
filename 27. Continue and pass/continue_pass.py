# continue dan pass dalam python dan dalam while menggunakan if statement 


# pass dalam python berfungsi sebaga dummy syntax yang artinya dia tidak akan di eksekusi di dalam kode sifat nya hampir mirip else namun tidak menggunakan str

# pass 
print("Ini contoh pertama")
angka = 0

while angka <5:

    angka += 1 
    if angka == 3:
        pass # ini tidak akan di eksekusi
    print(angka)

print(" ")

# continue
print("Ini contoh kedua")
angka = 0 
while angka < 5:
    angka +=1 
    print(f"Angka sekarang --> {angka}")
    if angka == 3: # baris loop ke tiga 
        print("loop baris ketiga") # loop baris 3 
        
        continue # akan meloncat ke step loop selanjutnya
    print("loop selesai di inden if") # eksekusi line di inden if dan bagian ini akan di eksekusi di output mengikuti loop baris ketiga  
print("Program selesai")



