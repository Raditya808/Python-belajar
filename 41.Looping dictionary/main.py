# mengambil data key string menggunakan for loop 
# mengambil data key string juga bisa menggunakan .keys()
# mengambil isi data key menggunakan key(i) dan menggunakan get untuk isi dari data key nya
# mengambil isi data key menggunakan variabel baru dan memanggil variabel data_dict dan menggunakan values dan mengeluarkan output isi dari key dalam bentuk ([]) dan dalam bentuk for loop
# mengambil isi data key dan isi data key nya menggunakan items() dan menggunakan variabel baru dan memanggil variabel data_dict dan menggunakan values dan mengeluarkan output isi dari key dan value nya dalam bentuk tuples () dan dalam bentuk for loop
# mengamil values key menggunakan values()
# mengambil data menggunakan per index dalam for loop beserta key dan value nya dan menggunakan items


data_dict = {
        "nama1":'muhammad',
        "nama2":'azia',
        "nama3":"qiqo"
}

# mengambil data key dari string menggunakan for loop 
# maka dia akan mengeluarkan key dari nama1,nama2,nama3
for i in data_dict:
    print(i)

print('')

# cara selanjut nya menggunakan .key()
# dan mendapatkan output menggunakan get
for i in data_dict.keys():
    # memanggil data key dan menggunakan get untuk isi key tersebut dan memanggil parameter i dari loop
    # dan mengambil isi dari data key dalam data dict
    print(data_dict.get(i))

print('')

# cara selanjutnya menggunakan values untuk mengambil isi dari data dict
# maka akan mengeluarkan isi dari key dalam bentuk ([])
datavalues = data_dict.values()
print(datavalues)

print('')

# menggunakan for loop dalam values ([])
# dan mengeluarkan isi dari data dic data dari key nya
for i in data_dict.values():
    print(i)

print('')



# cara selanjut nya menggunakan items dalam mengambil isi key dan data nya  
# maka output nya akan keluar dalam bentuk tuples () beserta key dan isi dari key nya
dataitems = data_dict.items()
print(dataitems)


print('')


# for loop items 
# for loop items 
for i in data_dict.items():
    print(i)


print('')


# mengambil dua data sekaligus menggunakan for data1,data2 di dalam data_dict
# agar bisa mengambil dua data sekaligus dan memisahkan nya 
# dan menggunakan items
for data1,data2 in data_dict.items():
    print(f'data key = {data1} values = {data2}')
