# PROPOSAL PROYEK PROGRAM SEDERHANA

## Program Rekap dan Analisis Nilai Matematika Kelas

### 1. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang sering dilakukan dalam pembelajaran matematika. Guru perlu mengetahui nilai rata-rata, nilai tertinggi, nilai terendah, dan jumlah siswa yang mencapai Kriteria Ketuntasan Minimal (KKM). Jika dilakukan secara manual, proses tersebut membutuhkan waktu dan berisiko terjadi kesalahan perhitungan.

Oleh karena itu, saya merancang program sederhana menggunakan Python untuk membantu proses rekap dan analisis nilai matematika siswa secara lebih mudah dan teratur.

### 2. Pengguna dan Tujuan Program

Pengguna program ini adalah guru atau mahasiswa Pendidikan Matematika yang ingin mengolah data nilai siswa.

Tujuan program:
1. Membaca data nama dan nilai siswa.
2. Menghitung nilai rata-rata kelas.
3. Menentukan nilai tertinggi dan terendah.
4. Menghitung jumlah siswa yang lulus dan belum mencapai KKM.
5. Menampilkan hasil analisis nilai secara teratur.

### 3. Ruang Lingkup Program

Program ini memiliki ruang lingkup sebagai berikut:
1. Data terdiri dari nama siswa dan nilai matematika.
2. Nilai yang diterima berada pada rentang 0 sampai 100.
3. KKM yang digunakan adalah 75.
4. Program menghitung rata-rata, nilai tertinggi, dan nilai terendah.
5. Program menentukan status siswa berdasarkan KKM.
6. Program menangani data yang tidak valid dan file yang tidak ditemukan.
7. Program dijalankan melalui terminal menggunakan Python.

### 4. Kebutuhan Program

**Kebutuhan perangkat lunak:**
- Visual Studio Code.
- Python.
- Git.
- Akun GitHub.

**Kebutuhan fungsional:**
- Program dapat membaca data nilai dari file.
- Program dapat memeriksa validitas nilai.
- Program dapat menghitung statistik nilai.
- Program dapat menentukan status kelulusan berdasarkan KKM.
- Program dapat menampilkan dan menyimpan hasil rekap.

### 5. Input, Process, dan Output (IPO)

| Bagian | Keterangan |
|---|---|
| Input | Nama siswa dan nilai matematika dari file teks |
| Process | Memeriksa data, menghitung rata-rata, mencari nilai tertinggi dan terendah, serta menentukan status berdasarkan KKM |
| Output | Rekap nilai, rata-rata kelas, nilai tertinggi, nilai terendah, jumlah siswa tuntas, dan jumlah siswa belum tuntas |

### 6. Algoritma Program

Langkah-langkah algoritma:
1. Mulai.
2. Membaca file yang berisi nama dan nilai siswa.
3. Memeriksa apakah file tersedia.
4. Memeriksa format data dan rentang nilai.
5. Menyimpan data yang valid.
6. Menghitung rata-rata nilai kelas.
7. Menentukan nilai tertinggi dan terendah.
8. Menghitung jumlah siswa yang mencapai KKM dan yang belum mencapai KKM.
9. Menampilkan hasil rekap nilai.
10. Menyimpan laporan hasil analisis.
11. Selesai.

### 7. Pseudocode

```text
MULAI
    Baca file data nilai

    JIKA file tidak ditemukan
        Tampilkan pesan kesalahan
    JIKA TIDAK
        Periksa format setiap data
        Periksa nilai berada pada rentang 0 sampai 100
        Simpan data yang valid

        JIKA tidak ada data valid
            Tampilkan pesan bahwa data kosong
        JIKA TIDAK
            Hitung rata-rata nilai
            Cari nilai tertinggi
            Cari nilai terendah
            Hitung siswa dengan nilai >= 75
            Hitung siswa dengan nilai < 75
            Tampilkan hasil rekap
            Simpan laporan
        AKHIR JIKA
    AKHIR JIKA
SELESAI
```

### 8. Rancangan Struktur Program

Program direncanakan menggunakan beberapa file agar setiap bagian memiliki tugas yang jelas.

| File | Fungsi |
|---|---|
| `src/main.py` | Menjalankan program utama |
| `src/data_io.py` | Membaca data dan menyimpan laporan |
| `src/analisis.py` | Menghitung statistik nilai dan status siswa |
| `src/utilitas.py` | Membantu pemeriksaan dan pengolahan data |
| `data/nilai_contoh.txt` | Menyimpan contoh data nilai |
| `tests/test_case.md` | Menyimpan rancangan pengujian |
| `README.md` | Menjelaskan proyek dan cara penggunaan |
| `.gitignore` | Menentukan file yang tidak perlu diunggah ke GitHub |

### 9. Rancangan Pengujian

| Kode | Kondisi Pengujian | Data atau Tindakan | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Data normal | Nilai 80, 70, dan 90 | Rata-rata 80, tertinggi 90, terendah 70 |
| TC02 | Nilai batas bawah | Nilai 0 | Nilai diterima sebagai data valid |
| TC03 | Nilai batas atas | Nilai 100 | Nilai diterima sebagai data valid |
| TC04 | Nilai tidak valid | Nilai 105 | Data ditolak atau diberi pesan kesalahan |
| TC05 | File tidak ditemukan | Membuka file yang tidak tersedia | Program menampilkan pesan kesalahan |
| TC06 | Semua siswa tuntas | Nilai 80, 85, dan 90 | Semua siswa dinyatakan mencapai KKM |

### 10. Rancangan Data

Data siswa disimpan dalam file teks dengan format nama dan nilai yang dipisahkan tanda koma.

Contoh:

```text
Ayu,85
Budi,78
Citra,90
Doni,65
Eka,75
```

Program menggunakan daftar untuk menyimpan data siswa selama proses pengolahan.

### 11. Pelaksanaan Tugas Individu

Proyek ini dikerjakan secara individu. Saya bertanggung jawab atas seluruh proses pengerjaan, mulai dari menentukan masalah, menyusun proposal, merancang algoritma, menentukan struktur program, menyusun test case, hingga menyiapkan dokumentasi dan repository GitHub.

### 12. Jadwal Pengerjaan

| Tahap | Kegiatan |
|---|---|
| Pertemuan 14 | Menyusun rancangan proyek, algoritma, struktur program, test case, dan dokumentasi awal |
| Pertemuan 15 | Melakukan implementasi program, pengujian, debugging, dan melengkapi dokumentasi |
| Pertemuan 16 | Melakukan presentasi dan demonstrasi proyek sesuai arahan dosen |

### 13. Repository GitHub

Repository GitHub digunakan untuk menyimpan dokumentasi, rancangan program, dan perkembangan proyek melalui commit secara bertahap.

URL repository: https://github.com/maulianamutiara/pertemuan-14-proyek-matematika-2225250078