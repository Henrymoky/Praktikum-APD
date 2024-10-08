# List pemain basket (nested list)
daftar_pemain = []

# Multiuser login credentials
users = [['admin', 'admin123', 'admin'], ['user', 'user123', 'user']]

# Flag untuk mengatur loop
program_berjalan = True

# Program CRUD
while program_berjalan:
    print("\n--- Menu Utama ---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # Proses login
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        user_found = False
        is_admin = False

        for user in users:
            if user[0] == username and user[1] == password:
                user_found = True
                if user[2] == 'admin':
                    is_admin = True
                break

        if user_found:
            print(f"\nSelamat datang, {username}!")
            
            if is_admin:
                # Menu admin
                admin_menu = True
                while admin_menu:
                    print("\n--- Menu Admin ---")
                    print("1. Tambah Pemain")
                    print("2. Lihat Pemain")
                    print("3. Update Pemain")
                    print("4. Hapus Pemain")
                    print("5. Logout")
                    
                    admin_choice = input("Pilih menu: ")

                    if admin_choice == "1":
                        # Tambah pemain
                        nama = input("Masukkan nama pemain: ")
                        umur = input("Masukkan umur pemain: ")
                        tinggi = input("Masukkan tinggi pemain: ")
                        daftar_pemain.append([nama, umur, tinggi])
                        print(f"Pemain {nama} berhasil ditambahkan.")
                    
                    elif admin_choice == "2":
                        # Lihat daftar pemain
                        print("\n--- Daftar Pemain ---")
                        if len(daftar_pemain) == 0:
                            print("Tidak ada pemain dalam daftar.")
                        else:
                            for i, pemain in enumerate(daftar_pemain):
                                print(f"{i + 1}. Nama: {pemain[0]}, Umur: {pemain[1]}, Tinggi: {pemain[2]}")
                    
                    elif admin_choice == "3":
                        # Update pemain
                        nomor = int(input("Masukkan nomor pemain yang ingin diupdate: ")) - 1
                        if 0 <= nomor < len(daftar_pemain):
                            nama_baru = input("Masukkan nama baru: ")
                            umur_baru = input("Masukkan umur baru: ")
                            tinggi_baru = input("Masukkan tinggi baru: ")
                            daftar_pemain[nomor] = [nama_baru, umur_baru, tinggi_baru]
                            print("Data pemain berhasil diupdate.")
                        else:
                            print("Nomor pemain tidak valid.")
                    
                    elif admin_choice == "4":
                        # Hapus pemain
                        nomor = int(input("Masukkan nomor pemain yang ingin dihapus: ")) - 1
                        if 0 <= nomor < len(daftar_pemain):
                            pemain_terhapus = daftar_pemain.pop(nomor)
                            print(f"Pemain {pemain_terhapus[0]} berhasil dihapus.")
                        else:
                            print("Nomor pemain tidak valid.")
                    
                    elif admin_choice == "5":
                        # Logout
                        admin_menu = False
                    else:
                        print("Pilihan tidak valid.")
            else:
                # Menu user biasa (lihat pemain saja)
                user_menu = True
                while user_menu:
                    print("\n--- Menu User ---")
                    print("1. Lihat Pemain")
                    print("2. Logout")
                    
                    user_choice = input("Pilih menu: ")

                    if user_choice == "1":
                        # Lihat daftar pemain
                        print("\n--- Daftar Pemain ---")
                        if len(daftar_pemain) == 0:
                            print("Tidak ada pemain dalam daftar.")
                        else:
                            for i, pemain in enumerate(daftar_pemain):
                                print(f"{i + 1}. Nama: {pemain[0]}, Umur: {pemain[1]}, Tinggi: {pemain[2]}")
                    elif user_choice == "2":
                        # Logout
                        user_menu = False
                    else:
                        print("Pilihan tidak valid.")
        else:
            print("Username atau password salah.")
    
    elif pilihan == "2":
        # Proses register
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")

        users.append([username_baru, password_baru, 'user'])
        print(f"User {username_baru} berhasil didaftarkan.")

    elif pilihan == "3":
        # Keluar dari program
        print("Terima kasih telah menggunakan program ini.")
        program_berjalan = False
    else:
        print("Pilihan tidak valid.")
