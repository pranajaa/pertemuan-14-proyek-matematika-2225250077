
def baca_data_nilai(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if baris == "":
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Format data tidak valid: {baris}")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Nilai tidak valid: {baris}")
                    continue

                if 0 <= nilai <= 100:
                    data_siswa.append({
                        "nama": nama,
                        "nilai": nilai
                    })
                else:
                    print(f"Nilai harus 0 sampai 100: {baris}")

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    return data_siswa