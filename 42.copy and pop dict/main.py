# copy dan pop dictionary menggunkan 
# copy() = mengcopy 
# pop() = menghapus isi dictionary paling akhir 


data_dict = {
        "nama":'muhammad',
        "nama2":'raditya',
        "nama3":'ramadhan',
        "nama4":'muhammad raditya ramadhan'
}

# perbedaan ketika menggunakan copy() 
# dalam assignment dan print langsung

# assignment dan copy 
dataassign = data_dict.copy()
print(f'data assignment = {dataassign}\n')

# print langsung dari data data_dict
print(f'data langsung = {data_dict}\n')


# ubah menggunakan data dictionary menggunakan list []
# mengubah key bernama 'nama' dan value bernama muhammad ke yang lain
# ketika menggunakan copy maka data di bagian assignment tidak ikut berubah di bagian key nama 
# karena sudah di copy
data_dict['nama'] = 'dammahum'
print(f'data diubah = {dataassign}\n')
print(f'data langsung = {data_dict}\n')


# menghapus key menggunnakan pop()
# dann menggunakan metode assignment
# menghapus key nama yang berisi value bernama dammahum
# maka ketika print assignment data bernama nama akan dihapus karena sudah di gunakan menggunakan pop()
datapop = data_dict.pop('nama')
print(f'data pop = {datapop}')

print(f'data diubah = {dataassign}')
print(f'data langsung = {data_dict}')
