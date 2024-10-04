#list barang
barang = [ [“Sapatu”, “Kaus Kakhi”, “Sarung”], [“Pulpen”, “Pensil”, “Laptop”] ]
#memanggil list secara keseluruhan untuk melihat bagaimana outputnya print(barang, “\n”)
#memanggil indeks pertama print(barang[0], “\n”)
#kali ini kita ingin menampilkan elemen “Pulpen”, kita perlu mengakses indeks dua kali, yang pertama untuk memilih list dengan elemen yang kita inginkan dan yang kedua indeks elemen itu sendiri
print(barang[1][0])