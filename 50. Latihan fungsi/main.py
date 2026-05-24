# LATIHAN FUNGSI 
import os 


# berfungsi membuat clean terminal
# untuk vs pake ('clear')
# os.system('cls')


# contoh menghitung luas dan keliling tanpa sebuah fungsi 
# loop while
# kondisi true akan membuat perulangan yang tidak ada henti 
# while True:

#     # ^ berfungsi menyenter dari teks f'' dan membat jarak sebesar 40
    
#     print('')

    # print(f'{'PROGRAM MENGHITUNG LUAS PERSEGI':^40}')
    # print(f'{'DAN KELILING PERSEGI':^40}')
    # print(f'{'-'*40:^40}')

#     print('')

#     # input user 
#     lebar = int(input('masukan nilai lebar:')) 
#     panjang = int(input('masukan nilai panjang:')) 


#     # program hitung luas  
#     luas = panjang*lebar
#     keliling = 2 * (panjang + lebar) 

#     print('')

#     # output
#     print(f'{'-'*40:^40}')
#     print(f'{'HASIL LUAS DAN KELILING':^40}')
#     print(f'Hasil Luas      = {luas}')
#     print(f'Hasil Keliling  = {keliling}')
#     print(f'{'-'*40:^40}')
    
#     # kondisi dimana perulangan itu berhenti atau lanjut
#     # continue = lanjut 
#     # dan break akan berhenti
#     lanjut = input('Lanjut y / n : ')
#     if lanjut == 'y':
#         continue
#     else:
#         break


# contoh menggunakan fungsi 
def header():
        ''' header '''        
        # os.system('clear')
        print(f'{'PROGRAM MENGHITUNG LUAS PERSEGI':^40}')
        print(f'{'DAN KELILING PERSEGI':^40}')
        print(f'{'-'*40:^40}')
        
    
def input_user():
    ''' input user '''
    lebar = int(input('Masukan angka lebar:'))
    panjang = int(input('Masukan angka panjang:'))
    
    return lebar,panjang


def hitung(lebar,panjang):
    ''' hasil luas'''
    return lebar*panjang


def keliling(lebar,panjang):
    ''' hasil keliling '''
    return 2*(lebar+panjang)    

# program hasil dan fungsi parameter untuk hasil dari perhitungan fungsi diatas 
while True:
    # Memanggil kondisi sekaligus fungsi utama 
    # memanggil fungsi header agar output header keluar terlebih dahulu
    header()
    
    # memanggil kondisi sekaligus fungsi kedua dan karena return ada 2 parameter 
    # memanggil lebar dan panjang dan fungsi dari input
    # agar dapat input 
    PANJANG,LEBAR = input_user()
    
    # memanggil kondisi atau sekaligus fungsi ke tiga dan mengisi parameter PANJANG,LEBAR menggunakan koma
    # serta memanggil fungsi dari keliling beserta memanggil parameter dari PANJANG,LEBAR
    print('') 
    print('-'*40)
    # hasil luas variabel dan isi fungsi hitung dan menerima parameter PANJANG DAN LEBAR MENGGUNAKAN KOMA 
    hasilluas = hitung(PANJANG,LEBAR)
    
    # hasil luas variabel dan isi fungsi keliling dan menerima parameter PANJANG DAN LEBAR MENGGUNAKAN KOMA
    hasilkeliling = keliling(PANJANG,LEBAR)
    
    print(f'Hasil luas = {hasilluas}')
    print(f'Hasil keliling = {hasilkeliling}')
    print('-'*40)
    print('')
    
    
    # kondisi ke empat 
    # kondisi dimana loop harus berhenti di kondisi string 
    lanjut = input('Ingin lanjut? y/n : ')
    if lanjut == 'y':
        continue
    else:
        break