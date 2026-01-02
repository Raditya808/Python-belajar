# Latihan percabangan 
# Kalkulator sederhana 


print("="*50)
print("Kalkulator sederhana")
print("="*50 + "\n")


angka_1  = float(input('masukan angka_1 = '))
operator = input("Operator(+,-,*,/,)    =")
angka_2  = float(input('masukan angka_2 = '))


# percabangan nya (untuk hasil hitung dari operator matematika diatas)
# menggunakan if , elif , else

# kondisi awal (if)
if operator == "+":
    hasil = angka_1 + angka_2 
    print(f"Hasil dari operator (+) adalah = {hasil}")

# kondisi kedua (elif) / menambahkan kondisi memang harus elif 
elif operator == "-":
    hasil = angka_1 - angka_2 
    print(f"Hasil dari operator (-) adalah = {hasil}")

# kondisi ketiga (elif)
    # kali dalam python bukanlah x melainkan (*) bintang
# kondisi di bawah ini yang menggunakan or yaitu menambahkan kondisi dimana x bisa di input sebagai kali
elif operator == "x" or operator =="*":  
    hasil = angka_1 * angka_2
    print(f"Hasil dari operator (*) adalah = {hasil}")


# kondisi keempat (elif) 
    # oeperator pembagian adalah (/) garis miring
elif operator == "/":
    hasil = angka_1 / angka_2 
    print(f"Hasil dari operator (/) adalah = {hasil}")

# kondisi dimana yang di input bukanlah angka atau angka yang tidak sesuai maka tidak akan valid
else:
    print("TIDAK VALID")

# output ketika program telah selesai di input
print("Akhir dari program")
