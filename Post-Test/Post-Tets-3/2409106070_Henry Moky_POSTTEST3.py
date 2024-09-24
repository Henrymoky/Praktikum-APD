# Input berat badan dalam mg (miligram)
berat_mg = float(input("Masukkan berat badan lo (mg): "))
# Input tinggi badan dalam km (kilometer)
tinggi_km = float(input("Masukkan tinggi badan lo (km): "))
# Mengubah satuan berat dari miligram ke kilogram (1 kg = 1,000,000 mg)
berat_kg = berat_mg / 1000000
# Mengubah satuan tinggi dari kilometer ke meter (1 km = 1000 meter)
tinggi_m = tinggi_km * 1000
# Hitung BMI
bmi = berat_kg / (tinggi_m ** 2)
# Tampilkan hasil BMI
print(f"Nilai BMI Anda adalah: {bmi:.2f}")
# Klasifikasi berdasarkan BMI
if bmi < 18.5:
    print("Berat badan lo kurang (Underweight).")
elif bmi < 24.9:
    print("Berat badan lo normal.")
elif bmi < 29.9:
    print("Berat badan lo berlebih (Overweight).")
else:
    print("You're fat bro, go to the gym (obesity).")
