# coppy list mengganti value berdasarkan [0,1,2,3]
# berdasarkan index
#a[0] = ''
# b = a 
# hex dan id dalam mengecek address variabel
# menggunakan copy() duplikat list

a = ['ucup','ita','mike']
print(f"data a = {a}")

b = a 
print(f"data b = {b}")

print(" ")


# akan merubah isi list a dan b 
a[0] = 'pucu'
a.sort()
print(f"data a = {a}")
print(f"data b = {b}")


# cek address dari variabel menggunakan hex dan id
# pada syntax hex dan id kita bisa melihat bahwa 
# a dan b ada di list yang berbeda namun b tetep mengambil isi list dari si a 
# dan hasil dari hex dan id menunjukann bahwa mereak berada di memori yang sama 
# unntuk mengatasi hal ini kita menggunakan syntax var.copy()
# untuk menduplikat list ke data baru 
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

print(" ")

# copy() 
# maka yang akan terjadi saat di print c nya berada di memori yang berbeda
# sehingga tidak di memori yang sama
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(" ")

# saat di print() data nya bisa kita ubah sehingga kode lain tidak ikut terubah
print('data a dan b dan c c di copy')
print(a)
print(b)
print(c)

print('')

print('ubah data c di index 0')
c[0] = 'ati'
print(a)
print(b)
print(c)
