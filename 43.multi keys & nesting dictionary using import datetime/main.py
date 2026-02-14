# multi keys & nesting dict 
# using import datetime
# dan menggabungkan data dictionary kedalam dictionary {
#   "key1":data1
#   "key2":data2
#   "key3":data3
#   }
# menggunakan print sebagai jarak dalam format str menggunakan :
# menjarak string sebagai <16 jarak
# print(f'{"key":<16}')
# menggunakan for loop variabel dan membuat variabel baru di indentasi bernama KEY dan SISWA
# dan membuat variabel bernama key yang ada di parameter for dan membuat variabel baru yang nantinya in parameter di panggil dan memanggil variabel parameter for itu didalam[] dan memanggil key didalam data dictionary 
# lalu membuat print sesuai dengan jarak dari print <:16 agar jarak nya sama
# dan menggunakan .strftime('%x') agar mendapatkan output sesuai dengan tanggal lahir isi dictionary


import datetime 

data1 = {
        "nama":"otong",
        "nim":"11130",
        "sks_lulus":120,
        "beasiswa":False,
        "lahir":datetime.datetime(2000,5,10),
}

data2 = {
        "nama":"ucup",
        "nim":"11131",
        "sks_lulus":140,
        "beasiswa":True,
        "lahir":datetime.datetime(2003,7,17),
}

data3 = {
        "nama":"odin",
        "nim":"11132",
        "sks_lulus":145,
        "beasiswa":True,
        "lahir":datetime.datetime(2002,4,11),
}

# menggabungkan dictionary didalam dictionary menggunakan {}
# metode nesting dictionary
datamahasiswa = {
    "maha1":data1,
    "maha2":data2,
    "maha3":data3
}
# output seluruh data dictionary 
# dalam string kunci1 dan kunci2 dan kunci3 
# dalam values
print(datamahasiswa)


print('')



# print jarak menggunakan format str 
# print(f'{'namakey':<angka jarak}')
print('-'*40)
print(f'{"NAMA SISWA":<16} {"NIM":<16} {"SKS":<16}')
print('-'*40)

# for loop 
for data in datamahasiswa:
    # key didalam data yang dibungkus didalam datamahasiswa yang membungkus isi dari data dictionary dari maha1,maha2,maha3
    key = data 
    # membuat variabel bernama namasiswa,nimmahasiswa dan memanggil parameter in dan memanggil parameter for bernama key dalam bentuk list dan memanggil data dictionary bernama = nama dan nim tergantung isi dari data dictionary nya dalam bentuk [] list
    namasiswa = datamahasiswa[key]['nama']
    nimmahasiswa = datamahasiswa[key]['nim']
    sksiswa = datamahasiswa[data]['sks_lulus']
    print(f'{namasiswa:<16} {nimmahasiswa:<16} {sksiswa:<16}')

    
