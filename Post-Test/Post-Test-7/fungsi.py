# Dictionary pemain basket
pemain_basket = {}

# Multiuser login credentials (variabel global)
users = {'admin': {'password': 'admin123', 'role': 'admin'}, 'user': {'password': 'user123', 'role': 'user'}}

# Flag untuk mengatur loop (variabel global)
program_berjalan = True

# Fungsi untuk menambahkan pemain baru (menggunakan parameter)
def tambah_pemain(id_pemain, nama, umur, tinggi):
    pemain_basket[id_pemain] = {'nama': nama, 'umur': umur, 'tinggi': tinggi}
    print(f"Pemain {nama} berhasil ditambahkan.")

# Fungsi untuk melihat daftar pemain (tanpa parameter)
def lihat_pemain():
    if not pemain_basket:
        print("Tidak ada pemain dalam daftar.")
    else:
        for id_pemain, info in pemain_basket.items():
            print(f"ID: {id_pemain}, Nama: {info['nama']}, Umur: {info['umur']}, Tinggi: {info['tinggi']}")

# Fungsi untuk mengubah data pemain (menggunakan parameter opsional)
def ubah_pemain(id_pemain, nama_baru=None, umur_baru=None, tinggi_baru=None):
    if id_pemain in pemain_basket:
        if nama_baru:
            pemain_basket[id_pemain]['nama'] = nama_baru
        if umur_baru:
            pemain_basket[id_pemain]['umur'] = umur_baru
        if tinggi_baru:
            pemain_basket[id_pemain]['tinggi'] = tinggi_baru
        print(f"Data pemain ID {id_pemain} berhasil diupdate.")
    else:
        print("ID pemain tidak ditemukan.")

# Fungsi untuk menghapus pemain
def hapus_pemain(id_pemain):
    if id_pemain in pemain_basket:
        pemain_terhapus = pemain_basket.pop(id_pemain)
        print(f"Pemain {pemain_terhapus['nama']} berhasil dihapus.")
    else:
        print("ID pemain tidak ditemukan.")

# Fungsi login multiuser (menggunakan parameter)
def login(username, password):
    if username in users and users[username]['password'] == password:
        return users[username]['role']
    return None

# Prosedur untuk mencetak jumlah pemain saat ini (tanpa parameter)
def hitung_pemain():
    jumlah = len(pemain_basket)
    print(f"Total pemain saat ini: {jumlah}")

# Fungsi rekursif untuk input angka (umur)
def input_umur():
    try:
        umur = int(input("Masukkan umur pemain: "))
        return umur
    except ValueError:
        print("Umur harus berupa angka. Silakan coba lagi.")
        return input_umur()

# Fungsi rekursif untuk validasi input tinggi
def input_tinggi():
    try:
        tinggi = float(input("Masukkan tinggi pemain: "))
        return tinggi
    except ValueError:
        print("Tinggi harus berupa angka. Silakan coba lagi.")
        return input_tinggi()

# Error handling saat memilih menu
def pilih_menu():
    try:
        return int(input("Pilih menu: "))
    except ValueError:
        print("Pilihan tidak valid. Harus berupa angka.")
        return pilih_menu()

# Prosedur untuk menampilkan menu user
def tampilkan_menu_user():
    print("\n--- Menu User ---")
    print("1. Lihat Pemain")
    print("2. Logout")

# Program CRUD
while program_berjalan:
    print("\n--- Menu Utama ---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = pilih_menu()

    if pilihan == 1:
        # Proses login
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        role = login(username, password)

        if role == 'admin':
            print(f"\nSelamat datang, {username} (Admin)!")
            # Menu admin
            admin_menu = True
            while admin_menu:
                print("\n--- Menu Admin ---")
                print("1. Tambah Pemain")
                print("2. Lihat Pemain")
                print("3. Update Pemain")
                print("4. Hapus Pemain")
                print("5. Lihat Total Pemain")
                print("6. Logout")

                admin_choice = pilih_menu()

                if admin_choice == 1:
                    # Tambah pemain
                    nama = input("Masukkan nama pemain: ")
                    umur = input_umur()  # Fungsi rekursif untuk validasi umur
                    tinggi = input_tinggi()  # Fungsi rekursif untuk validasi tinggi
                    id_pemain = len(pemain_basket) + 1  # ID unik otomatis
                    tambah_pemain(id_pemain, nama, umur, tinggi)

                elif admin_choice == 2:
                    # Lihat daftar pemain
                    lihat_pemain()

                elif admin_choice == 3:
                    # Update pemain
                    id_pemain = int(input("Masukkan ID pemain yang ingin diupdate: "))
                    nama_baru = input("Masukkan nama baru (biarkan kosong jika tidak ingin mengubah): ")
                    umur_baru = input("Masukkan umur baru (biarkan kosong jika tidak ingin mengubah): ")
                    tinggi_baru = input("Masukkan tinggi baru (biarkan kosong jika tidak ingin mengubah): ")
                    ubah_pemain(id_pemain, nama_baru or None, umur_baru or None, tinggi_baru or None)

                elif admin_choice == 4:
                    # Hapus pemain
                    id_pemain = int(input("Masukkan ID pemain yang ingin dihapus: "))
                    hapus_pemain(id_pemain)

                elif admin_choice == 5:
                    # Hitung jumlah pemain
                    hitung_pemain()

                elif admin_choice == 6:
                    # Logout
                    admin_menu = False
                else:
                    print("Pilihan tidak valid.")
        
        elif role == 'user':
            print(f"\nSelamat datang, {username} (User)!")
            # Menu user biasa
            user_menu = True
            while user_menu:
                tampilkan_menu_user()  # Prosedur untuk menampilkan menu

                user_choice = pilih_menu()

                if user_choice == 1:
                    # Lihat daftar pemain
                    lihat_pemain()

                elif user_choice == 2:
                    # Logout
                    user_menu = False
                else:
                    print("Pilihan tidak valid.")
        
        else:
            print("Username atau password salah.")
    
    elif pilihan == 2:
        # Proses register
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")

        users[username_baru] = {'password': password_baru, 'role': 'user'}
        print(f"User {username_baru} berhasil didaftarkan.")

    elif pilihan == 3:
        # Keluar dari program
        print("Terima kasih telah menggunakan program ini.")
        program_berjalan = False
    else:
        print("Pilihan tidak valid.")
