# membuat program sederhana menggunakan list [] dan index() serta while 
# dalam buku
# serta menggunakan index untuk dapat angka no urut +1 
# dan enumerate mengakses index isi list dan for parameter in variabel
# sertan karena kasus nya menggunakan while kita harus membuat kondisi percabangan yang membuat kode while berhenti menggunakan break atau continue untuk lanjut

list_buku = []

# membuat loop
while True:
    print('Masukan Buku')
    nama_buku = input('Masukan Nama Buku:\t')
    penulis = input('Masukan Penulis Buku:\t')
    
    buku_bru = [nama_buku,penulis]
    list_buku.append(buku_bru)

    for index,buku in enumerate(list_buku):
        print("-"*40)
        print(f"No {index+1} \nnama_buku = {buku[0]} \npenulis = {buku[1]}")
        print('-'*40)


    lanjut = input('Ingin lanjut ? (y/n)')

    if lanjut == 'n':
        break 
    else:
        continue
print('selesai')
