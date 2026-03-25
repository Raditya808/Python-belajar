# Part 2 
# lanjutan dari part 1 dengan mennggunakan dictionary kosong {}
# dan menggunakan while dan for loop 
# dan dengan menggunakan syntax update dari operasi dictionary dan membungkus dict dari variabel data_kosongmaha kosonng nya dan membuat key baru dan membungkus isimahasiswa yang di set menggunakan dict.fromkeys
# dan membuat kondisi percabangan if dan else agar perulangan while berhenti atau lanjut

# update menggunakan import random dan import string 
# untuk mendapatkan key yang sesuai 
  # dan mendambah kan variabel baru dan menambahkan ''.join(random for i in range(6)) dan menambahkan batas 
  # untuk maksimal key mennggunakan random syntax for i in range(6) batas 6 
   # dan menambahkan syntax (random.choice(string.ascii,uppercase,lowercase))  
    # agar saat menggunakan syntax update {} tidak menimpa dengan key yang sama di perulangan for i tergantung batas nya    


import datetime
import os 
import random
import string


# lanjutan menggunakan data dictionary kosongh {}
data_kosongmaha = {}

# os.system untuk mendapatkan hasil terminal yang bersih tanpa adanya history dari terminal 
os.system('cls')

data_mahasiswa = {
        "nama":'nama',
        'nim':'00000',
        "sks_lulus":0,
        "tanggal_lahir":datetime.datetime(1111,11,1)
}

# membuat dictionary kosong untuk syntax update dan membungkus dengan variabel data_kosongmaha
dta_kosong = {}

# mngisi data dalam input
# makan key yang tadinya kosonng menjadi nama itu sendiri 
print('-'*40)
print(f'{'SELAMAT DATANG'}')
print('-'*40)

# update menggunakan while perulangan
while True:
    # mendapatkan key dari data_mahasiswa dengan menggunakan 
    # dict.fromkeys(variabel.keys())
    # maka akan bersifat none maka kita akan isi data ini
    isimahasiswa = dict.fromkeys(data_mahasiswa.keys())
    print(isimahasiswa)


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
    isimahasiswa['tanggal_lahir'] = datetime.datetime(tahunlahir,bulanlahir,tanggallahir).strftime('%x')
    
    # memanggil data kosong dictionary dann membungkus dalam update dan membuat key bernama string key dan di isi : dari isimahasiswa yang di set menggunakan dict.fromkeys
    # dan mendambah kan variabel baru dan menambahkan ''.join(random for i in range(6)) dan menambahkan batas 
    # untuk maksimal key mennggunakan random syntax for i in range(6) batas 6 
    # dan menambahkan syntax (random.choice(string.ascii,uppercase,lowercase))

    key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_kosongmaha.update({key:isimahasiswa})

    # membuat print tabel database menggunakan <16 format str
    print('-'*90)
    print(f'{'KEY':<16} {'NAMA':<16} {'NIM':<16} {'SKS LULUS':<16} {'TANGGAL LAHIR':<16}')
    print('-'*90)
    
    # update menggunakan for loop
    for i in data_kosongmaha:
        print(f'{i:<16} {data_kosongmaha[i]['nama']:<16} {data_kosongmaha[i]['nim']:<16} {data_kosongmaha[i]['sks_lulus']:<16} {data_kosongmaha[i]['tanggal_lahir']}')

    tambahdata = input('ingin tambah data (y/n):')
    if tambahdata =='y':
        continue
    else:
        break



