# Part 1
# latihan membuat dictionary dalam input 
# dan menggunakan dict.fromkeys(variabel dictionary.keys()) untuk mendapatkan result dari key dalam variabel dictionary dan menggunakan kurung () didalam nya menggunakan .keys()
# dan membuat dictionary kosong untuk mengisi sama seperti konsep list kosong 
# dan menggunakan import datetime 
# dan menggunakan [] dan memanggil keys didalam data data_mahasiswa untuk input yang sudah menggunakan dict.fromkeys(data_mahasiswa.key()) 
# dan membungkus datatime dalam tuples() untuk membungkus hasil input sesuai isi data dictionary
# menggunakan import os agar tidak ada history terminal 



import datetime
import os 



# os.system untuk mendapatkan hasil terminal yang bersih tanpa adanya history dari terminal 
os.system('cls')

data_mahasiswa = {
        "nama":'nama',
        'nim':'00000',
        "sks_lulus":0,
        "tanggal_lahir":datetime.datetime(1111,11,1)
}

dta_kosong = {}

# mendapatkan key dari data_mahasiswa dengan menggunakan 
# dict.fromkeys(variabel.keys())
# maka akan bersifat none maka kita akan isi data ini
isimahasiswa = dict.fromkeys(data_mahasiswa.keys())
print(isimahasiswa)

# mngisi data dalam input
# makan key yang tadinya kosonng menjadi nama itu sendiri 
print('-'*40)
print(f'{'SELAMAT DATANG'}')
print('-'*40)

# memanggil variabel isimahasiswa karena sudah menggunakan dict.fromkeys dan .keys()
# dalam variabel data_mahasiswa untuk diisi dan memanggil salah satu key didalam data itu
isimahasiswa['nama'] = input('masukan nama:')
isimahasiswa['nim'] = input('masukan nim:')
isimahasiswa['sks_lulus'] = int(input('masukan nilai sks:'))
tahunlahir = int(input('masukan tahun lahir(1999-2025/dll):'))
bulanlahir = int(input('masukan bulan lahir (1,12):'))
tanggallahir = int(input('masukan tanggal lahir (1,31):'))

# membungkus isi dari import datetime dengan () isi dari int input karena isi data dictionary adalah 3 
# dan diantara nya tahun , bulan, tanggal 
# dan membungkus data diatas yang diantara nya tahunlahir , bulanlahir, tanggallahir
isimahasiswa['tanggal_lahir'] = datetime.datetime(tahunlahir,bulanlahir,tanggallahir)
print(isimahasiswa)
