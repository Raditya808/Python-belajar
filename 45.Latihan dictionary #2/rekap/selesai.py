import os 
import string 
import datetime 
import random

dataksng = {}

dataset = {
    "nama":'',
    "umur":0,
    "tanggal_lahir":datetime.datetime(1111,11,11)
}


# set datakey didalam data set 
# menggunakan while 
while True:
    # membuat key dict.fromkeys 
    keytes = dict.fromkeys(dataset.keys())
    
    # memanggil key dictionary dan dijadikan input
    keytes['nama'] = input('Masukan Nama:')
    keytes['umur'] = input('Masukan umur:')
    
    # bungkus tanggal lahir
    # karena komponen datetime memiliki 3 yaitu tahun,bulan,hari 
    # dijadikan sebagai variabel dulu dan dibungkus ke dalam key keytes[]
    tahun = int(input('Masukan Tahun Lahir(1000,2025):'))
    bulan = int(input('Masukan Bulan Lahir(1,12):'))
    tanggal = int(input('Masukan Tanggal Lahir(1,32):'))
    
    # bungkus 3 variabel diatas ke dalam key dan datetime
    keytes['tanggal_lahir'] = datetime.datetime(tahun,bulan,tanggal).strftime('%x')
    
    # output baris
    print('-'*80)
    print(f'{'KEY':<16} {'NAMA':<16} {'UMUR':<16} {'TANGGAL LAHIR':<16}')
    print('-'*80)
    
    # memanggil dataksng {} dan di masukan ke dalam syntax update dan 
    # menjadikan 'key' sebagai identitas baru dari keytes yang dijadikan dict.fromkeys
    # membuat identitas key baru menggunakan random dan str menggunakan ''.join()
    inikey = ''.join((random.choice(string.ascii_lowercase) for i in range(6)))
    dataksng.update({inikey:keytes})
    for i in dataksng:
        key = i 
        nama = dataksng[i]['nama']
        umur = dataksng[i]['umur']
        tanggallhir = dataksng[i]['tanggal_lahir']
        print(f'{i:<16} {nama:<16} {umur:<16} {tanggallhir:<16}')
    
    # kondisi berhenti menggunakan break continue dan percabangan if dan else
    tambahdata = input('Ingin Tambah Data G? (y/n):')
    if tambahdata == 'y':
        continue
    else:
        break 
    
    import os 
import string 
import datetime 
import random

dataksng = {}

dataset = {
    "nama":'',
    "umur":0,
    "tanggal_lahir":datetime.datetime(1111,11,11)
}


# set datakey didalam data set 
# menggunakan while 
while True:
    # membuat key dict.fromkeys 
    keytes = dict.fromkeys(dataset.keys())
    
    # memanggil key dictionary dan dijadikan input
    keytes['nama'] = input('Masukan Nama:')
    keytes['umur'] = input('Masukan umur:')
    
    # bungkus tanggal lahir
    # karena komponen datetime memiliki 3 yaitu tahun,bulan,hari 
    # dijadikan sebagai variabel dulu dan dibungkus ke dalam key keytes[]
    tahun = int(input('Masukan Tahun Lahir(1000,2025):'))
    bulan = int(input('Masukan Bulan Lahir(1,12):'))
    tanggal = int(input('Masukan Tanggal Lahir(1,32):'))
    
    # bungkus 3 variabel diatas ke dalam key dan datetime
    keytes['tanggal_lahir'] = datetime.datetime(tahun,bulan,tanggal).strftime('%x')
    
    # output baris
    print('-'*80)
    print(f'{'KEY':<16} {'NAMA':<16} {'UMUR':<16} {'TANGGAL LAHIR':<16}')
    print('-'*80)
    
    # memanggil dataksng {} dan di masukan ke dalam syntax update dan 
    # menjadikan 'key' sebagai identitas baru dari keytes yang dijadikan dict.fromkeys
    # membuat identitas key baru menggunakan random dan str menggunakan ''.join()
    inikey = ''.join((random.choice(string.ascii_lowercase) for i in range(6)))
    dataksng.update({inikey:keytes})
    for i in dataksng:
        key = i 
        nama = dataksng[i]['nama']
        umur = dataksng[i]['umur']
        tanggallhir = dataksng[i]['tanggal_lahir']
        print(f'{i:<16} {nama:<16} {umur:<16} {tanggallhir:<16}')
    
    # kondisi berhenti menggunakan break continue dan percabangan if dan else
    tambahdata = input('Ingin Tambah Data G? (y/n):')
    if tambahdata == 'y':
        continue
    else:
        break 
    
    
