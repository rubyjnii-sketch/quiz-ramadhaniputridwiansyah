print("===========================")
print("PROGRAM KELULUSAN MAHASISWA")
print("===========================")

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama == "andi":
    target = 70
elif nama == "budi":
    target = 75
elif nama == "citra":
    target = 80
else:
    target = 0
    print("Nama mahasiswa tidak terdaftar!")

# Proses ujian
if target != 0:
    print("\nNama mahasiswa :", nama)
    print("Target nilai    :", target)

    percobaan = 1
    lulus = False

    while percobaan <= 3:
        print("\nPercobaan ke-", percobaan)

        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            print("Selamat!", nama, "berhasil mencapai target.")
            lulus = True
            break
        else:
            print("Nilai belum mencapai target.")
            print("Silakan mengikuti remedial.")

        percobaan += 1

    # Menampilkan hasil akhir
    print("\n========== HASIL AKHIR ==========")

    if lulus:
        print(nama, "dinyatakan lulus!")
        print("Berhasil pada percobaan ke-", percobaan)
    else:
        print(nama, "dinyatakan tidak lulus!")
        print("Sudah mengikuti 3 kali percobaan.")

print("===============")
print("PROGRAM SELESAI")
print("===============")
