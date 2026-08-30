import string


'''
fungsi yang di ketahui sebelum nya 

def namafungsi(param):
    print(param)
namafungsi()
'''


# ketika membuat fungsi dan mengisi fungsi tersebut sebagai sebuah value 
# maka ketika value nya berupa int,float,bool,string 
# maka akan mengakibatkan error khusus nya di bool dan string ketika membuat tipe data yang data nya adalah int 
# itu lah fungsi type int dengan menggunakan tipe data berupa int didalam parameter 
# penggunaan 
# tipe data didalam fungsi tidak hanya int namun ada juga yang berfungsi untuk string 
# namun string harus menggunakan import terlebih dahulu
'''
def namafungsi(param:int):
'''
# pembuatan nama fungsi dan parameter yang didalam nya diisi : setelah parameter lalu ketik tipe data integer 
# atau menggunakan (opsional) -> setelah penutupan fungsi dan di akhiri titik dua : untuk hoover dia sebagai tipe data int sepenuh nya seperti ini 
'''
def namafungsi(param:int) -> int:
'''


# contoh type data int pada fungsi  
# fungsi type hints pada integer
def pangkat(a:int) -> int:
    hasil = 10 ** a 
    return hasil 
# maka output akan menjadi 100 
output = pangkat(2)
print(output)


# contoh selanjutnya string pada fungsi 
def nama(a:string):
    print(a)
nama('rdyt')


