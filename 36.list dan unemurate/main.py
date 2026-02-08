# di materi sebelumnya kita mempelajari materi for loop 
# dan pemanggilan for i in range 
# i bisa kita ganti dengan nama lain selagi print nya ngikutin itu 
#
# contoh 



data_angka = [1,2,3,4]

# contoh 1 
# ketika membuat for loop seperti ini 
# maka kita akan mengambil isi dari list variabel data_angka 
# dan identitas nya kita mennggunnakan angka maka saat print 
# angka akan mengambil isi dari list nya 
for angka in data_angka:
    print(f'data angka dari list = {angka}')


print('')


# contoh 2 menggunakan len 
# seperti bahasa c dan javascript
# menggunakan for i in range karena ada len 
data_angka = [4,5,6,7]
datalist = len(data_angka)

for i in range(datalist):
    print(f'data angka dari list = {data_angka[i]}')



print(' ')



# contoh 3 dalam menggunakan len 
# len harus memiliki variabel yang di set ke 0 
# agar output nya keluar menggunakan unary operator var+=1
# dan menggunakan len untuk konversi integer tanpa len maka list akan error 
# dan saat print kita akan memanggil variabel list nya dan [] list berisi variabel yang di isi nya adalah 0 
data_angka = [1,2,3,4,5,6,7]
tes = 0 
gabungan = len(data_angka)

while tes < gabungan:
    print(f'data angka = {data_angka[tes]}')
    tes+=1




print('')





# contoh ke 4 
# metode list comperehension 
# dengn menggunakan [] dan membuat for loop didalam list ini
# dan menggunakan print didalamnya setelah nya adalah for loop
#
# atau menggunakan print dan [] mempangkatkan dua **2

data = [1,2,100,230] 
[print(f'data memiliki = {i}')for i in data]

# mengambil data diatas
tes = [i**2 for i in data]
print(f'data pangkat 2 {tes}')




print('')



# conntoh ke 5 
# menggunakan enumerate untuk mendapatkan index masing masing dari isi list
# dan menggunakan index di for loop dan setelah nya adalah koma dan parameter utuk output print 
# lalu selanjutnya menggunakan enumerate untuk mendapatkan index masing masing di list 

data_list = [1,2,'radit','lmao','amogus']

for index,data in enumerate(data_list):
    print(f'nomor = {index} data nya = {data}')

