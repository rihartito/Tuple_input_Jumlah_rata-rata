
'''
buatlah sebuah program agar bisa menambahkan atau tidak sesuai inputan user 
setelah itu rata-ratakan dan jumlahkan semua angka yang ada dituple,hitung ada
berapa angka didalam Tuple tersebut,tampilkan isinya dalam tuple


input :user = menambahkan atau tidak ; jumlah_user = angka yang dimasukkan

proses :
membuat def,mengubah menjadi list
melakukan perulangan while 
melakukan perulangan for 
melakukan append 

output :
melihat tuple yang baru,rata-rata,penjumlahan,dengan jumlah isi dalam tuple
'''

def paket_lengkap(hola):
    ubah = list(hola)
    jumlah = 0 
    print((ubah))
    user = str(input("apakah anda ingin menambahkan ya/tidak :"))
    while user == "ya" :
        masuk = int(input("masukkan angka :"))
        ubah.append(masuk)
        user = str(input("apakah anda ingin menambahkan ya/tidak :"))
    for i in ubah :
        jumlah += i
    print("Tuple yang baru")
    print (tuple(ubah))
    print("rata-ratanya adalah :",jumlah // len(ubah))
    print("Jumlahnya adalah :",jumlah)
    print("jumlah isi dalam tuple :",len(ubah))

Tuple_baru = (2,3,4,1)
paket_lengkap(Tuple_baru)


