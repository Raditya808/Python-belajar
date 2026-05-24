# dalam python parameter didalam fungsi bisa di assignment kan menggunakan = dan diisi dengan nilai default 
# entah itu string atau int 
# nilai default mau diisi atau tidak nilai default tidak akan menghasilkan error ketika kita isi yang lain nilai nya pada saat pemanggilan fungsi nya 

# contoh singkat 
# def namafungsi(parameter1,parameter2='nilai default'):



# contoh 1 
def haloperson(nama,pesan="selamat datang"):
    ''' memiliki dua parameter yang satu kosong dan yang satu memailiki default value '''
    print(f'Halo {nama} {pesan}')

# ketika ini dipanggil maka parameter pesan tidak perlu di panggil karena dia memiliki nilai default berisi string
haloperson('radit')



# contoh 2 
def sapa(user='kamu',sapa='apa kabar'):
    
    """ kedua parameter memiliki nilai default """
    print(f'halo {user} {sapa}')

# meskipun didalam parameter memiliki nilai default kita tetap bisa memanggil dengan parameeter lain
# maka output nya adalah halo radit apa kabar
sapa('radit')



# contoh 3 
def htung_pangkat(angka,pangkat=3):
    """ disini ada 2 parameter angka dan pangkat yang memiliki default parameter 3"""
    hasil = angka**pangkat
    """ dan di atas sini setiap kali angka dari parameter input nya maka akan di pangkatkan dengan variabel pangkat ** """
    return hasil

# maka hasil nya tetap akan 125 karena tidak peduli dia ada default value selagi ada isi di pemanggilan maka itu lah hasil tetap nya
hasil = htung_pangkat(pangkat=3,angka=5)
print(hasil)

# metode output bisa kek gini
print(htung_pangkat(5,3))


# contoh 4 
def htung_tambah(a1=1,a2=2,a3=3,a4=4):
    hasil = a1 + a2 + a3 + a4 
    return hasil

# metode mengambil satu parameter seperti ini bisa karena tidak akan menghasilkan error karena setiap parameter memiliki value
# namun hitungan nya jelas dari parameter a1 , a2 sampe a4 maka hasil nya 11
print(htung_tambah(a3=4))
