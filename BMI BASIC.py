# Kalkulator BMI sederhana
# input dari user
berat = float(input("Masukkan berat badan (kg) :"))
tinggi = float(input("Masukkan tinggi badan (cm) :"))
# ubah tinggi ke meter
tinggi_m = tinggi/100
# Hitung BMI
bmi = berat / (tinggi_m **2)
print(f"\nBMI kamu adalah: {bmi :.2f}")
# Tentukan kategori
if bmi < 18.5:
    print("Kategori : Kurus")
elif bmi < 25:
    print("Kategori : Ideal atau Normal")
elif bmi < 30:
    print("Kategori : Gemuk")
else:
    print("Kategori : Overweight atau obesitas")
# Syarat tinggi badan
if tinggi < 160:
    print("Hasil : Tinggi badan anda tidak sesuai dengan persyaratan")
elif tinggi > 160:
    print("Hasil : Tinggi badan anda memenuhi persyaratan")
# Penilaian Stakes
if bmi < 17:
    print("Penilaian : Stakes 4 atau Sangat Kurus")
elif 17 <= bmi < 18.5:
    print("Penilaian : Stakes 3 atau Kurus")
elif 18.5 <= bmi < 20:
    print("Penilaian : Stakes 3 atau Normal Bawah")
elif 20 <= bmi < 23:
    print("Penilaian : Stakes 1 atau Normal Ideal")
elif 23 <= bmi < 25:
    print("Penilaian : Stakes 2 atau Overweight Ringan")
elif 25 <= bmi < 27:
    print("Penilaian : Stakes 3 atau Overweight Sedang")
else:
    print("Penilaian : Stakes 4 atau Obesitas")
          