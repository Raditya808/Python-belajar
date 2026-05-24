
# didalam python selain membuat print didalam indentasi fungsi 
# kita bisa menambahkan return 
# return berfungsi mengembalikan nilai yang konsep nya sama seperti print cuman lebih simpel
# untuk membuat return misal nya seperti ini 

'''def hitung(a,b):
    return parameter a dan b 
hitung(nilaiparametera,nilaiparameterb)'''



# misal dalam khasus hitng kuadrat 
def kuadrat(input_kuadrat):
    ''' fungsi kuadrat '''
    return input_kuadrat**2 


print('\nFungsi kuadrat dan metode print nya\n')
# output metode 1 
y = kuadrat(5)
print(y) # hasil nya bener 25 

# output metode 2 
# menggunakan tambah setelah input
y = kuadrat(5) + 10 
print(y)

# output metode 3 
# membuat print langung secara sederhana 
print(kuadrat(5)) # ini juga hasil nya 25



# contoh selanjutnya dalam khasus hitung tambah dan multi input 
print('\nfungsi tambah multiinput\n')
def hitungtambah(angka1,angka2):
    ''' fungsi tambah dan multi input'''
    return angka1 + angka2 

# output 
print(hitungtambah(10,10)) # 20


# contoh selanjut nya multireturn dan membuat variabel,variabel supaya dapat hasil nya satu persatu didalam return
print('\nfungsi multireturn\n')
def operasimtk(a,b):
    ''' fungsi multi return '''
    tambah = a + b 
    kurang = a - b 
    kali = a * b  
    bagi = a / b 
    return tambah,kurang,kali,bagi


# metode output yang memanggil variabel lalu koma sesuai isi parameter agar bisa di panggil satu persatu output nya didalam badan fungsi 
# membuat banyak variabel dan koma ',' di sesuai kan isi dalam return karena return memiliki 4 metode maka dibawah harus ada 4 variabel dan koma
a,b,c,d = operasimtk(5,5)
print(a) # posisi a yang berjalan adalah tambah 
print(b) # posisi b yang berjalan adalah kurang
print(c) # posisi c yang berjalan adalah kali 
print(d) # posisi d yang berjalan adalah bagi


