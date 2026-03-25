# rekap tanpa menggunakan for i  
# tanpa while
# dan menggunakan print biasa 

import datetime
import os 


# set terminal bersih
os.system('cls')

datasetmaha = {
        "nama":'',
        "umur":0,
        "tanggallhir":datetime.datetime(1111,11,11)
}


# set key default dari dict fromkeys 
newkey = dict.fromkeys(datasetmaha)


# key input 
newkey['nama'] = input('Masukan Nama:')
newkey['umur'] = int(input('Masukan Umur:'))

# set newkey untuk tanggal lahir dari variabel
tahun = int(input('Masukan Tahun Lahir:'))
bulan = int(input('Masukan Bulan Lahir:'))
tanggal = int(input('Masukan Tanggal Lahir:'))

# set newkey menggunakan datetime import 
newkey['tanggallhir'] = datetime.datetime(tahun,bulan,tanggal)

# output
print('-'*50)
print(f'{'NAMA':<16} {'Umur':<16}')
print(f'{newkey['nama']}')
print('-'*50)
