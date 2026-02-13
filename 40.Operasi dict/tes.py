# operasi dict 
# menggunakan get() agar tidak menghasilkan error mengakses data dic
# get ganti message dengan koma , setelah mengakses data dic
# mengganti data atau menambah data menggunakan list[] atau update menggunakan ({})
# hapus data dic menggunakan del datadic['nama']



# data menggunakan kurawal (dictionary)
data_dic = {
"cup":"ucup",
"tong":"otong",
"dang":"dadamg"
}

# output
print(data_dic)


# cek panjang menggunakan len()
panjangdict = len(data_dic)
print(f"Panjang dari data dic adalah = {panjangdict}")

# cek true false jika value ada di dalam data itu dan menghasilkan nilai boolean
# dengann menggunakan operator in
# jika value nya diganti maka akan bernilai False
cekdatadict = "cup"
hasil = cekdatadict in data_dic
print(f"apakah data {cekdatadict} ada di = {data_dic}? = {hasil}")


# mengakses dic dengan get 
# seperti yang kita tau kita bisa mengakses isi dic dengan [] list lewat print
# namun untuk menngetahui jika data itu beneran dictionary kita bagus nya menggunakan get 

# contoh 1 (tanpa get)
print(data_dic['cup'])

# contoh 2 (menggunakan get)
print(data_dic.get('cup'))

# contoh 3 ketika mengakses yang tidak ada di data dictionary maka yang akan terjadi akan error 
#print(data_dic['kis'])

# namun berbeda dengan get dia tidak error namun menghasilkan None bahwa data itu tidak ada
# dan kalau kita bisa mengakses setelah koma untuk mengganti isi dari message nya yang None dengan kemauan kita sendiri
print(data_dic.get('kis','tidak ada'))




# mengganti data atau menambah data menggunakan list[] atau update
# mengganti data atau update menggunakan list []

# memanggil isi data dan mengganti isi data dic nya 
# maka value ucup di ganti menjadi ucup surucup keren
data_dic['cup'] = 'ucup surucup keren'
print(data_dic)

# menambah data 
# maka akan bertambah radit didalam nya 
data_dic['radit'] = 'ramadhan'
print(data_dic)

# diatas adalah contoh pemanggilan dari isi data dic dan mengganti value nya ke yang lain 
# dan membuat data baru dengan menggunakan metode yang sama nah cara lain ada dengan menggunakan update



# menggunakan update dengan kurawal yang langsung mengubah data dan menambah 
# data yang awal nya ucup surucup keren berubah menjadi ucup surucup tidak keren
data_dic.update({"cup":"ucup surucup tidak keren"})
print(data_dic)


# atau bisa untuk menambahkan data 
# maka data baru akan tertulis ketika kita mengakses tulisan / ketikan yang lain sama seperti metode menggunakan list diatas 
# dan cara ini lebih bagus karena syntax update yang untuk mengupdate data / menambah data
data_dic.update({"databaru":"kitasan"})
print(data_dic)


# menghapus salahs satu data didaalam data dic
# maka data baru akan dihapus
del data_dic['databaru']
print(data_dic)
