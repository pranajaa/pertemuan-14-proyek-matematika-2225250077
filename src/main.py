
from pathlib import Path

from data_io import baca_data_nilai
from analisis import (
    hitung_rata_rata,
    nilai_tertinggi,
    nilai_terendah,
    hitung_status_kkm
)
from utilitas import tampilkan_judul, tampilkan_pesan, simpan_laporan


def main():
    tampilkan_judul()

    lokasi_proyek = Path(__file__).resolve().parent.parent
    file_data = lokasi_proyek / "data" / "nilai_contoh.txt"

    data_siswa = baca_data_nilai(file_data)

    if not data_siswa:
        tampilkan_pesan("Belum ada data nilai yang valid.")
        return

    print("\nDAFTAR NILAI SISWA")
    for siswa in data_siswa:
        print(f"{siswa['nama']}: {siswa['nilai']}")

    mencapai, belum_mencapai = hitung_status_kkm(data_siswa)

    print("\nHASIL ANALISIS")
    print(f"Rata-rata nilai : {hitung_rata_rata(data_siswa):.2f}")
    print(f"Nilai tertinggi : {nilai_tertinggi(data_siswa)}")
    print(f"Nilai terendah  : {nilai_terendah(data_siswa)}")
    print(f"Mencapai KKM    : {mencapai} siswa")
    print(f"Belum mencapai  : {belum_mencapai} siswa")

    laporan = (
        "REKAP DAN ANALISIS NILAI MATEMATIKA KELAS\n"
        "=========================================\n"
        f"Rata-rata nilai: {hitung_rata_rata(data_siswa):.2f}\n"
        f"Nilai tertinggi: {nilai_tertinggi(data_siswa)}\n"
        f"Nilai terendah: {nilai_terendah(data_siswa)}\n"
        f"Mencapai KKM: {mencapai} siswa\n"
        f"Belum mencapai KKM: {belum_mencapai} siswa\n"
    )

    file_output = lokasi_proyek / "output" / "laporan_nilai.txt"
    simpan_laporan(file_output, laporan)

    print(f"\nLaporan berhasil disimpan di: {file_output}")


if __name__ == "__main__":
    main()
