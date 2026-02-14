# cara gampang menggunakan values
import datetime
from time import strftime

maha1 = {
        "nama":'ucup',
        "nim":'1122331',
        "nilai":90,
        'lahir':datetime.datetime(2001,10,9)
}


maha2 = {
        "nama":'iko',
        "nim":'1122332',
        "nilai":80,
        'lahir':datetime.datetime(2004,5,10)
}

maha3 = {
        "nama":'ucup',
        "nim":'1122333',
        "nilai":90,
        'lahir':datetime.datetime(2002,6,8)
}

# membuat nesting di variabel full_datagabung
# dan membuat key maha1,maha2,maha3
full_datagabung = {
        "maha1":maha1,
        "maha2":maha2,
        "maha3":maha3
}
# output data nya
print('-'*90)
print(f"Data key beserta values nya = {full_datagabung}")
print('-'*90)

print('')


# membuat table print jarak menggunakan format strinng :<16
# dan menggunakan string didalam kurawal{}
print('-'*90)
print(f'{'Nama':<16} {'Nim':<16} {'Nilai':<16} {'Lahir':<16}')
print('-'*90)

# menggunakan values agar data dictionary didalam full_datagabung bisa di akses lewat i dalam masing masing keys
for i in full_datagabung.values():
    # keys nama , nim , nilai , lahir di dalam data dictionary di full_datagabung
    # dan menggunakan strftime('%x') output tanggal lahir
    print(f'{i["nama"]:<16} {i["nim"]:<16} {i["nilai"]:<16} {i["lahir"],strftime("%x")}')




