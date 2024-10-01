def bmi_calculator():
    while True:
        weight_mg = int(input("Masukkan berat badan Anda (mg): "))
        height_km = float(input("Masukkan tinggi badan Anda (km): "))

        # Konversi berat dan tinggi
        weight_kg = weight_mg / 1_000_000
        height_m = height_km * 1_000

        # Menghitung BMI
        bmi = weight_kg / (height_m ** 2)

        # Menentukan kategori BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesitas"

        print(f"BMI Anda: {bmi:.2f}, Kategori: {category}")

        # Opsi keluar
        exit_choice = input("Apakah Anda ingin keluar? (y/n): ")
        if exit_choice.lower() == 'y':
            break

def login():
    username = "Henry"  # Nama Praktikan
    password = "70"     # Tiga digit terakhir NIM kamu

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        user_input = input("Masukkan Username: ")
        pass_input = input("Masukkan 3 digit terakhir NIM: ")

        if user_input == username and pass_input == password:
            print("Login berhasil!")
            bmi_calculator()
            break
        else:
            attempts += 1
            print(f"Login gagal! Percobaan ke-{attempts}")
            if attempts == max_attempts:
                print("Anda telah gagal login 3 kali. Program berhenti.")
                break

# Memulai program
login()
