

# index[0] data masing masing list bisa di = '' ganti value nya 
# index[0] print() print data index masing masing didalam list 
# insert(1,'sjds') untuk menggeser value str berdasarkan index 
# extend(list_lama) untuk menggabungkan list yang di var sebelum / sesudah 
# remove() menghapus value str atau index 
# var.append('sds') menambah list di urutan terakhir 
# pop() menghapus atau mengecek list paling akhir berdasarkan =


# contoh 
# 3 index dari 0 
data_index = ['radit','ucup','apalah']


# data_index0
data_index0 = data_index[0] # = radit 
print(f"data 0  = {data_index0}")


# data menggunakan -
data_min = data_index[-1] # = apalah 
print(f"data -1 = {data_min}")


# data menggunakan - 
data_min = data_index[-2] # = ucup 
print(f"data -2 = {data_min}")


# data menggunakan -
data_min = data_index[-3] # = radit
print(f"data -3 = {data_min}")


# pada materi sebelum nya kita belajar len untuk menghitung string 
# karena per koma adalah string di data index maka output nya 3
data_len = len(data_index)
print(f"Panjang karakter adalah = {data_len}")



# manipulasi list 
# nambah data index
# isi dari data index
# untuk menambah data kita perlu memanggil data index dan kita menggunakan syntax insert
# dataindex.insert(angka_index,value)
print(f"data sebelum di tambah = {data_index}")


# nambah data menggunakan insert di index 1 maka ucup akan bertukar posisi 
# (1 adalah index dan 'opet' adalah value string)
data_index.insert(1,'opet')
print(f"data setelah di tambah menggunakan insert = {data_index}")


# lalu selanjut nya kita bisa menambahkan isi list nya lagi 
# menggunakan syntax append
# maka riski akan di tambahkan di list namun di posisi di akhir
data_index.append('riski')
print(f"data setelah di tambah menggunakan append = {data_index}")


# lalu selanjut nya kita bisa menambahkan list dengan list baru dengan menggunakan syntax extend 
# maka data list lama dan baru di tambahkan
data_list_baru = ['kiki','riki']
data_index.extend(data_list_baru)
print(f"data list lama dan baru digabung menggunakan extend = {data_index}")


# lalu kita bisa merubah value dari list di ganti dengan value yang baru 
# maka radit akan menjadi rapit
data_index[0] = 'rapit'
print(f"Data setelah index 0 diganti = {data_index}")


# lalu kita bisa menghapus value list di ganti dengan value yang baru berupa str
# jika kita menggunakan syntax remove dan menghapus value str yang tidak sesuai list 
# maka akan terjadi error
data_index.remove('rapit')
print(f"data setelah menggunakan remove dan menghapus rapit = {data_index}")


# lalu kita bisa menghapus value list paling belakang/akhir 
# maka riki akan hilang
# kalau menggunakan pop di data yang ada list maka kita akan menghapus value str yang akhir 
# kalau kita menggunakan variabel baru maka kita melihat value str yang dihapus itu
data_pop = data_index.pop()
print(data_pop)
