# Input 
barang = input("Masukkan nama barang: ")
harga = float(input("Masukkan harga barang (Rp): "))
jumlah = int(input("Masukkan jumlah barang: "))
diskon = float(input("Masukkan persentase diskon (%): "))
# Proses 
hargasebelumdiskon = harga * jumlah
totaldiskon = (diskon / 100) * hargasebelumdiskon
total_bayar = hargasebelumdiskon - totaldiskon
sisabagi = totaldiskon % 3
# Output 
print(f"\nAnda membeli {jumlah} {barang} dengan harga satuan Rp{harga:.2f},")
print(f"Total sebelum diskon adalah Rp{hargasebelumdiskon:.2f}, total diskon adalah Rp{totaldiskon:.2f},")
print(f"dan total yang harus dibayar adalah Rp{total_bayar:.2f}.")
print(f"\nDiskon {totaldiskon:.2f} dibagi dengan 3 sisanya {sisabagi:.2f}")