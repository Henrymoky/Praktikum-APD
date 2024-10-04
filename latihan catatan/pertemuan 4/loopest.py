# for i in range(10, -1, -1):
#     print(f"anak ayam turun {i}")
    
# ulang = 'ya'
# hitung = 0
# while ulang == 'ya':
#     print(f"Perulangan ke {hitung+1}")
#     ulang = input("Apakah anda masih ingin mengulang?")
#     hitung += 1
# print("Perulangan selesai")

# x = 0
# while x < 5:
#     print(x)
#     x += 1
 
# hitung = 1   
# while True:
#     print(f"Perulangan ke {hitung}")
#     ulang = input("Apakah anda masih ingin mengulang?")
#     if ulang == "tidak":
#         break
#     hitung += 1
    
# print(f" Total Perulangan: {hitung}")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i == 5:
#         break
#     print(i)
    
# for i in range(10):
#     if i % 2 == 0:
#         break
#     if i == 5:
#         continue
#     print(i)

usn = "admin"
pw = "admin123"
salah = 0

while salah < 3:
    username =  input("masukkan username: ")
    password = input("masukkan password: ")
    if usn == username and pw == password:
        print("login berhasil")
        break
    else:
        print("login gagal")
        salah +=1