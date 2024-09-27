#ulang = 10
#for i in range (ulang):
#    print("perulangan ke-"+str(i)+"kali")
#    print(f"perulangan ke--{i} kali")

#simpan = [12, "udin petot", 14.5, True, 'A']
#for i in simpan:
#    print(i)

#print(simpan[2])

#for i in range(1, 4):
#    for j in range(1, 4):
#        print(f"{i} x {j} = {i * j}")
#    print()

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total perulangan: {hitung}")