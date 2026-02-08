# di beberapa materi list sebelum nya kita telah belajar materi list,lalu list manpulasi ,serta operasi list 
# sekarang kita akan belajar tentang nested list atau list bersarang
#
#



# contoh 1
# menggabungka list 
print('list gabungan lewat []')
data1 = [1,2,3,4]
data2 = [5,6,7,8]

# kita bisa menggabungkan list dengan menggunakan [] didalam nya 
hsil_data = [data1,data2]
print(hsil_data)
# maka saat di print maka akan mengeluarkan output gabungan list



# contoh kedua 
# kita bisa menggabungan list menggunakan parameter dan \n 
print('list for i in variabel')
data1str = ['radit','nas','syad']
data2str = [21,20,21]

# membuat parameter untuk print 
for data in data1str:
    # maka output data akan mengeluarkan dari data1str
    print(f'data1 {data1str}\n')
    for data2 in data2str:
        # dan ini mengeluarkan output di data2str
        print(f'data umur {data2str}')

print(" ")


print("list for i in variabel")
data1str = ['radit',21,'laki-laki']
data2str = ['nas',20,'perempuan']
data3str = ['syd',21,'laki-laki']
# atau bisa seperti ini 
# menggunakan [] berbagai index
# menggabungan isi dari variabel list data1str dan data2str
# dan memanggil berdasarkan index
# dan memanggil output berdasarkan index
gabungan = [data1str,data2str,data3str]
for i in gabungan:
    print(f"data nama = {i[0]}") # index 0 = data1str
    print(f'data umur = {i[1]}') # index 1 = data2str
    print(f'data kelamin = {i[2]}\n') # index 2 = data3str


print("")

print('data gabungan list')
print(gabungan)

print('')

# copy list di materi sebelumnya
datacopy = gabungan.copy()
print('list copy')
print(f'data copy = {datacopy}')

print('')

# mengubah list berdasarkan index karena sudah di copy() atau di duplikat
# maka tidak akan keganggu data sebelumnya

datacopy[0] = 'lmao',21,'laki-laki'
print(f'data copy ubah index = {datacopy}')
