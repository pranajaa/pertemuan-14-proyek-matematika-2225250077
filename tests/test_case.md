# Rancangan Pengujian Program

Pengujian ini dirancang untuk memastikan program rekap dan analisis nilai matematika berjalan sesuai kebutuhan.

| Kode | Kondisi | Data atau Tindakan | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Data normal | Nilai 80, 70, 90 | Rata-rata 80, nilai tertinggi 90, nilai terendah 70 |
| TC02 | Batas bawah | Nilai 0 | Nilai diterima sebagai data valid |
| TC03 | Batas atas | Nilai 100 | Nilai diterima sebagai data valid |
| TC04 | Nilai tidak valid | Nilai 105 | Nilai ditolak atau muncul pesan kesalahan |
| TC05 | File tidak ditemukan | Membaca file yang tidak tersedia | Muncul pesan kesalahan |
| TC06 | Semua siswa mencapai KKM | Nilai 80, 85, 90 dengan KKM 75 | Semua siswa dinyatakan mencapai KKM |

## Kesimpulan

Rancangan pengujian mencakup kondisi normal, batas nilai, data tidak valid, file yang tidak ditemukan, dan kondisi seluruh siswa mencapai KKM. Pengujian sebenarnya dilakukan setelah program selesai dibuat.