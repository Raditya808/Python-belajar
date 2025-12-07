# class yang tanpa menggunakan syntax super ataupun __init__
# hanya menggunakan pewarisan dari class yang paling awal 

class kendaraan1:
    def __init__(self,nama_kendaraan="",tipe=""):
        self.nama_kendaraan = nama_kendaraan
        self.tipe = tipe
    
    def output(self):
        print("=====================")
        print(self.nama_kendaraan)
        print(self.tipe)
        print("=====================")
    
class kendaraan2(kendaraan1):
    def __init__(self,nama_kendaraan,tipe,berat):
        self.nama_kendaraan = nama_kendaraan
        self.tipe = tipe
        self.berat = berat
        
    def output(self):
        print("=====================")
        print(self.nama_kendaraan)
        print(self.tipe)
        print(self.berat)
        print("=====================")

tes1 = kendaraan1(nama_kendaraan="motor",tipe="revo 2011")
tes1.output()

tes2 = kendaraan2(nama_kendaraan="mobil",tipe="kijang",berat="200kg")
tes2.output()
    
    
    
