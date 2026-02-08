# list 
# list adalah kumpulan data yang disimpan dalam satuu kurung 

# list menggunakan []

# lalu ada syntax list untuk membuat variabel menjadi list di khasus range(0,9)

# lalu ada list comprehension variabel = [i for i in range(0,9)] dan bisa di kali i nya

# lalu ada list comprehension variabel = [i for i in range(0,9) if i !=5] dan bisa menggunakan if didalam nya untuk menghilangkan salah satu angka 

# lalu ada list comprehension variabel = [i for i in range(0,9) if i %2] dan bisa menampilkan ganjil menggunakan operator modulus / % 

#  lalu ada list comprehension variabel = [i for i in range(0,9) if ] dan bisa menampilkan genap 

# list dalam angka 
angka = [1,2,3] # output [1,2,3]
print(angka)


# list dala string 
string = ['radit','lutpi','windah']
print(string)

# bollean 
bollean = [True,False,False]
print(bollean)


# campuran bisa mencampur semua tipe data 
# number, str, bolean
campuran  = ['radit',12,True]
print(campuran)



# cara alternatif membuat list khasus range(angka)
# menggunakan synatx list 
angka_list = range(0,9,2)
print(angka_list) # tidak akan bisa dikarenakan tidak memiliki syntax list 
ubah_angka_list = list(angka_list)
print(ubah_angka_list)


# list comprehension [i for i in range(angka)]
# range adalah batas
list_comprehension = [i**2 for i in range(0,9)]
print(list_comprehension)


# list comprehension menghilangkan salah satu angak menggunakan != 
# range adalah batas 
list_comprehension = [i for  i in range(0,9) if i != 5] # menghilangkan 5 
print(list_comprehension)


# list_comprehension menggunakan if dan menampilkan angka ganjil 
# range adalah batas
list_ganjil = [i for  i in range(0,10) if i %2 != 0]
print(list_ganjil)


# list comprehension menggunakan if dan menampilkan angka genap 
# range adalah batas 
angka_genap = [i for i in range(0,10)if i %2 == 0]
print(angka_genap)
