# kita sudah sering membuat sebuah fungsi yang kek gini 
# dan kita terkadang ingin membuat sebuah fungsi yang bisa menerima value yang banyak tanpa harus membuat parameter yang banyak 
# dibawah ini ada 2 macam fungsi value parameter yang banyak




# 1
# menggunakan parameter 
# metode parameter yang banyak di fungsi  
def data(nama,tinggi,berat):
    print(f'nama = {nama} tinggi = {tinggi} berat = {berat}')
data('tio',170,21)



# 2 
# menggunakan index[] dan copy() dari parameter fungsi  dan menggunakan satu parameter
# lalu membuat variabel dan variabel copy tadi bisa di jadikan sebagai wadah dan di isi sebagai paremeter dari variabel tanpa harus mengisi di tuples 
# dan juga mengisi di pemanggilan fungsi nya dengan list yang sewaktu waktu bingung dan error
def data(dt):
    copydata = dt.copy() 
    nama = copydata[0] 
    tinggi = copydata[1] 
    berat = copydata[2]

    # metode copy() namun ribet karena harus menggunakan syntax variabel yang dijadikan copy() dari si parameter 
    print(f'nama = {nama} tinggi = {tinggi} berat = {berat}')
data(['tio',170,21])


# kedua cara diatas tidak efektif karena yang satu membuat banyak parameter 
# yang kedua sedikit efektif namun tidak efisien karena pemanggilan fungsi yang harus di isi sebagai list

# ada cara yang bagus tanpa menggunakan list index itu yaitu *args dalam parameter 
# *args berfungsi sama seperti metode kedua diatas cuman yang membedakan tidak harus mengisi list di pemanggilan fungsi
# dan tidak harus membuat copy() dari si parameter
# dan penamaan *args tidak harus bernama args tetapi bisa dengan nama lain misal *angka *data *dll


# 3 
# (*args)
def datanama(*args):
    nama = args[0] 
    tinggi = args[1]
    berat = args[2] 
    print(f'nama = {nama} tinggi = {tinggi} berat = {berat}')

# output akan sama seperti metode ke 2 diatas
datanama('tio',170,21)



# args juga bisa di ganti dengan sebuah nama 
 # misal 

def angkapilih(*angka):
    result = 0 
    for i in angka:
        result += i 
    return result

tes = angkapilih(10,10,20)
print(tes)
