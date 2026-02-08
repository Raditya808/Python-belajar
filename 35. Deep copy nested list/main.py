# di beberapa materi sebelum nya kita sudah mengenal list dan manipulasi , copy dan nested list 
# seperti extend,insert,remove, pop,index[],append,sort,reverse
# dan copy()
# dan [variabellist1,variabellist2]
# dan hex(id) untuk mengecek memory atau address dari variabel list sama atau tidak 
# mengimport library deepcopy / from copy import deepcopy





# mengambil index jika didalam nya index gabungan 
data1 = [1,2,3,4] # data pada index ke 0 
data2 = [5,6,7,8] # data pada index ke 1 jika di gabungkan ke dalam list


# gabung 
# maka ketika kita menggabungkan maka data diatas akan di gabungkan namun bagaimana kita bisa 
# mengakses isi data nya / diambil satu persatu lewat index ?
datgabungan1dan2 = [data1,data2,10]
print(f"data 1 dan 2  adalah {datgabungan1dan2}")



# data copy
datgabungan1dan2copy = datgabungan1dan2.copy()
print(f"data 1 dan 2 copy {datgabungan1dan2copy}")


print(" ")


# mengambil posisi di data1 dan di index0 di ambil menggunakan index[] namun di akses dua kali karena data nya atau posisi nya lebih jelas
dataambil0di1 = datgabungan1dan2[0][0] # jika ini hanya satu 0 maka akan memanggil isi seluruh data1
# maka output nya bener adalah =1 di karenakan 0 adalah posisi index ke data1 dan tambah 0 adalah posisi ke 1 
print(f'data gabungan di data1 index ke 0 adalah = {dataambil0di1}')


# cek address atau memory
# menggunakan hex id 
print('')

print(f'data asli = {hex(id(datgabungan1dan2[0]))}')
print(f'data copy = {hex(id(datgabungan1dan2copy[0]))}')


datgabungan1dan2[0][1] = 50 
datgabungan1dan2copy[0][1] = 40
print(f"data asli di posisi ke data 1 dan index 1 {datgabungan1dan2}")
print(f"data copy di posisi ke data 1 dan index 1 {datgabungan1dan2copy}")


print("")

# menggunakan import deepcopy 
from copy import deepcopy
datgabungan1dan2 = [data1,data2,10]
datagabungandeepcopy = deepcopy(datgabungan1dan2copy)
datgabungan1dan2aslideep = deepcopy(datgabungan1dan2)

print('tanpa deep copy')
print(f'data asli = {hex(id(datgabungan1dan2[0]))}')
print(f'data copy = {hex(id(datgabungan1dan2copy[0]))}')

print('menggunakan deepcopy')
print(f'data asli = {hex(id(datgabungan1dan2aslideep[0]))}')
print(f'data copy deep = {hex(id(datagabungandeepcopy[0]))}')

