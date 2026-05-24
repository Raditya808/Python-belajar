''' Function dan Argumen didalam function '''

''' didalam python untuk mendefinisikan sebuah fungsi yaitu menggunakan def / definition 
dan function bisa menerima suatu parameter dan print paremeter didalam () / input artinya
parameter biasanya digunakan untuk mendefinisikan sebuah value dan bisa dipanggil berkali kali 
tergantung isi parameter 
kalau isi nya ada dua dan ada koma maka di objek pemanggilan kita memanggil dua kali di dalam ()
dan function bisa memasukan value object apapun string bisa number bisa array juga bisa
'''


'''
contoh menerima satu parameter 
def namafungsi(parameter):
    print(parameter) 
namafungsi('pemanggilan harus satu parameter bebas number,string,float semua bisa')   
'''



'''
contoh2
ketika menerima dua parameter 
def namafungsi(parameter1,parameter2):
    print(f'{"parameter1","parameter2} ') 
namafungsi('pemanggilan harus 2 parameter dan menggunakan , bebas number,string,float semua bisa')   
'''






# contoh didalam kode menerima satu parameter
def helloperson(nama):
    print(f"Halo {nama}")
# maka output browser akan menjadi halo dari objek dibawah yaitu berisi string radit
helloperson('radit')
helloperson('lol')



# contoh selanjutnya kode menerima dua parameter
# membuat program tambah sederhana dua parameter 
def tambahop(angka1,angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
# memanggil parameter yang menggunakan , kalau dia lebih dari satu
# maka output nya dibawah ini adalah 1 + 6 = 7
# dan objek bisa di panggil berkali kali dan angka nya bisa berbeda beda 
tambahop(1,6)
tambahop(5,200)



# contoh selanjutnya kode function didalam array 
# mengisi object dengan data yang tidak didalam indentasi bisa asalkan selama 
# object nya juga di panggil maka dia akan mengeksekusi kode didalam indentasi function
# menggunakan for loop 
def testnama(peserta):
    hasilpserta = peserta
    for i in hasilpserta:
        # maka output list dibawah akan di panggil semuanya didalam list 
        print(f"Halo peserta {i}")

datalst = ['radit','lmao','rmahdan']
testnama(datalst)