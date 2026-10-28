
def tampilkan_judul():
    print("=" * 45)
    print("REKAP DAN ANALISIS NILAI MATEMATIKA KELAS")
    print("=" * 45)


def tampilkan_pesan(pesan):
    print(pesan)

def simpan_laporan(nama_file, isi_laporan):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(isi_laporan)