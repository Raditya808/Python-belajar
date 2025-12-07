a = 9
b = 5

# macam macam operator 
# not ~ 
# xor ^ 
# and &
# or | 
# setiap angka yang output binary mau itu 1 atau 2 akan di gabungkan 
# kalau 0 angka nya tetap


# Bitwise menggunakan | or 
print("bitwise menggunakan | or ")
print(format(a,'08b')) # menentukan angka binary dalam variabel a lalu di format menjadi angka 8 baris
print(format(b,'08b')) # menentukan angka binary dalam variabel b lalu di format menjadi angka 8 baris
c = a | b # menentukan hasil dari dua variabel tersebut menggunakan operator bitwise dari or atau |
print(format(c,'08b')) # menentukan hasil dari dua variabel tersebut
print("=========================")


# Bitwise menggunakan ^ xor 
# xor adalah operator dimana angka 1 di baris yang sama maka akan menghasilkan nilai 0 
# namun jika angka 1 nya di baris yang berbeda maka angka 1 tersebut akan digabungkan sebagai output
print("bitwise menggunakan ^ xor ")
print(format(a,'08b'))
print(format(b,'08b'))
c = a ^ b # menentukan hasil dari dua variabel tersebut menggunakan operator bitwise dari xor atau ^ 
print(format(c,'08b'))
print("=========================")



# bitwise menggunakan & and 
# jika salah satu angka nya ada satu dan di line yang sama maka akan 
# di hasilkan yang sama 
print('bitwise menggunakan & and')
print(format(a,'08b'))
print(format(b,'08b'))
c = a & b 
print(format(c,'08b'))
print("=========================")



# bitwise menggunakan not ~
print("bitwise menggunakan ~ not")





