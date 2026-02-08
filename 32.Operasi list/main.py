# count() menghitung list berdasarkan value 
# sort() mengurutkan list 
# reverse() membalikan list



data_angka = [2,2,2,2,2,3,4,5,1,2,34,5,7,8,9,9,3,1,]


# pada materi string manipulasi part1 count menghitung berapa banyak suatu value dari per number atau string 
print(f"Data angka awal \n= {data_angka}")



# dalam konteks ini kita coba menghitung berapa banyak angka yang sama dalam list 
# menggunakan var_baru  = count.data_angka(value number/string) 
# dalam kode dibawah ini kita mengecek seberapa banyak value 9 didalam list maka jawaban nya akan itu
hasil_9 = data_angka.count(9)
print(f"cek angka 9 ada berapa di listt menggunakan count \n= {hasil_9}") 

# cek hasil 2 menggunakan count
hasil_2 = data_angka.count(2)
print(f"hasil 2 ada berapa di list menggunakan count \n= {hasil_2}")

print('\n')




# syntax index() untuk value str atau number dalam mengambil data 
# data nya berupa index angka
data_str = ['ucup','radit','halo']
print(f"data str awal \n= {data_str}")

# index() 
# index ke 0 
hasil_ucup = data_str.index('ucup') # adalah data ke index 0 
print(f"data ucup didalam list menggunakan index() \n= {hasil_ucup}")

# index ke 3 
hasil_radit = data_str.index('radit')
print(f"data radit didalam list menggunakan index() \n= {hasil_radit}")


# mengurutkan list number dari list diatas menggunakan sort()
sebelum = data_angka
print(f"Sbelum menggunakan sort() \n= {sebelum}")

# setelah menggunakan sort() data angka akan di urutkan 
data_angka.sort()
print(f"setelah menggunakan sorted() \n= {data_angka}")




# sort() didalam str 
# maka dia akan berjalan sesuai urutan abc 
data_sebelum_disort_str = data_str
print(f"sebelum menggunakan sort \n= {data_sebelum_disort_str}")

# sort()
data_sebelum_disort_str.sort()
print(f"setelah menggunakan sort() {data_sebelum_disort_str}")


# reverese() membalikan list 
data_sebelum_reverse_str = data_str 
print(f"sebelum menggunakan reverse \n= {data_sebelum_reverse_str}")

# menggunakan reverse()
data_sebelum_disort_str.reverse()
print(f"setelah menggunakan reverse() \n= {data_sebelum_reverse_str}")
