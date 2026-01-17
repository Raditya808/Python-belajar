# break 
# break berfungsi untuk menghentikan perulangan (loop) secara paksa sebelum kondisi perulangan terpenuhi.
# ketika ada kondisi percabangan lalu didalam if ada print dan di indentasi if juga memiliki print 
# maka print di bagian indentasi if akan di eksekusi di luar indentasi if 
# dan if di indentasi akan di buat secara loop 


# contoh 1
print("="*30)
print("Contoh Pertama dalam konsidisi if")
angka = 0 

while angka <5:

     # di sini setiap perulangan akan menghasilkan sampai 5
    angka += 1  
    print(angka)
    

    # dan di sini dikarenakan ada break dalam percabangan maka di jalankan sampai loop baris 3 aja
    if angka == 3:
        print('loop baris 3')
        break # ketika break ini dijalankan maka dia tidak akan mengeluarkan output sampai 5 dia hanya menjalankan sampai 3 aja jika break ini tidak ada maka loop akan terus berjalan sampao ribuan output

    print('loop indentasi if')
print('prpgram selesai')
print("="*30)


# contoh kedua dalam input
# loop ini akan mengabaikan loop ke setiap angka jika di kondisi akhir sesuai input maka dia akan di eksekusi 
print("Contoh kedua dalam kondisi if dan input")
angka = int(input('Masukan angka:'))
angka2 = 0 

while True: # membuat jika kondisi true 
    angka2 +=1  # maka setiap perulangan akan ditambah 1 
    print(angka2)

    # kondisi if menggabungkan kedua variabel atas yang angka buat input dan angka2 untuk kondisi loop
    if angka == angka2:
        print(f"loop ke {angka}")
        break

    print('loop indentasi if')
print("Program selesai")





