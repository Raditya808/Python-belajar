# dictionary di python 
# kalau biasanya kita memiliki sebuah list [] dan kita bisa akses menggunakan index 
#
# nah kalau dictionary kita bisa mengakses di kurung {} dan mengisi key string lalu : isi value nya entah itu str int float atau boolean
# contoh 

data_list = ['tes1','tes2','tes3']

# untuk print akses nya kita bisa menggunakna []
print(data_list[0]) # maka akan di akses di tes1 


# dictionary dan cara akses nya 
# kita mengisi key nya menggunakan str lalu setelah nya kita menggunakan : lalu di isi dengan value 
# kalau mau menambahkan key lagi dibawah nya bisa menggunakan , koma setelah nya
# dic ini di isi bebas semua tipe data akan bisa muncul bahkan ketika kita panggil data list diatas aja bisa
# dan untuk memanggil key nya kita menggunakan list setelah print(variabel nya[]) didalam print
data_dict = {
"nama":'radit',
'umur':21,
'data':data_list,
}
# maka ketika di print output nya adalah {'nama':'radit'}
print(data_dict)
# dan kita bisa memanggil isi key nya 
# dari str 

# maka output nya adalah radit
print(data_dict['nama'])


# panggil output di data dict dengan isi data list
print(data_dict['data'])


# print data umur di key data_dict
print(data_dict['umur'])
