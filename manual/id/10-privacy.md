<!-- translated from zh-TW at commit 968641f -->

# 10. Privasi dan Statistik Anonim

AeroCam tidak memiliki akun pengguna. Foto Anda mentransfer secara langsung antara kamera dan ponsel Anda dan **tidak pernah diunggah ke server mana pun**. Hanya item kecil yang tercantum di bawah ini yang pernah meninggalkan ponsel Anda.

## Saat Aplikasi Terhubung ke Internet
| Fitur | Apa yang dikirim | Bisakah dimatikan? |
|---|---|---|
| Periksa pembaruan (Beta) | Hanya meminta GitHub untuk info versi terbaru | Berjalan secara otomatis sekali sehari |
| Statistik penggunaan anonim | Lihat di bawah | Ya, di bawah Pengaturan → Dukungan |
| Berbagi kode QR | Berjalan hanya di jaringan lokal Anda (Wi‑Fi atau hotspot ponsel yang sama) sehingga orang yang memindai dapat melihat foto pilihan Anda | Berhenti saat Anda mengetuk Berhenti atau saat pengatur waktu berakhir |

## Statistik Penggunaan Anonim
Digunakan untuk memahami secara kasar berapa banyak orang yang menggunakan AeroCam, kamera dan fitur mana yang mereka gunakan, dan di mana masalah terjadi sehingga kami tahu apa yang harus dibangun selanjutnya. **Tidak pernah dijual kepada siapa pun dan tidak pernah digunakan untuk iklan.**

- **Sakelar**: **Pengaturan → Support → «Kirim statistik penggunaan anonim»**, aktif secara default.
- Dijelaskan sekali saat pertama kali Anda terhubung ke kamera, di mana Anda dapat memilih «OK» atau «Matikan». **Tidak ada yang dikirim sebelum Anda menjawab.**
- **Saat dimatikan**: Pengiriman berhenti segera, dan kedua ID acak di bawah ini dan data apa pun yang belum dikirim akan dihapus. Menyalakannya kembali menghasilkan ID baru.
- Saat offline (misalnya, saat terhubung ke Wi‑Fi kamera itu sendiri), peristiwa disimpan di ponsel Anda dan dikirim nanti saat akses internet tersedia.
- Build Dev tidak pernah merekam atau mengirim statistik.

### Data yang Dikirim
- **ID acak yang dihasilkan aplikasi**: Tidak berasal dari ponsel atau kamera Anda; disetel ulang jika Anda menginstal ulang aplikasi atau mematikan statistik.
- Model kamera (misalnya, Nikon Z f) — hanya nama model.
- Metode koneksi (Bluetooth, Wi‑Fi, USB, FTP) dan jenis Wi‑Fi (Wi‑Fi kamera itu sendiri, hotspot ponsel, router).
- Fitur mana yang digunakan setiap hari (nama fitur saja, sekali sehari), termasuk fitur terkunci yang diketuk.
- Jumlah koneksi yang berhasil atau gagal; pada kegagalan, hanya kode kategori (seperti «waktu habis») yang dikirim, tidak pernah pesan galat.
- Langkah tambah kamera: dimulai, berhasil, kamera tidak ditemukan, dan alasan kegagalan.
- Jumlah foto yang diterima setiap hari (hitungan untuk JPEG, RAW, dan video — hitungan saja).
- Apakah izin diberikan atau ditolak.
- Tingkat saat ini (Gratis, kunci Beta…), versi aplikasi, bahasa aplikasi, dan versi utama Android.
- Negara: ditentukan dari koneksi; hanya kode negara yang disimpan.

### Tidak Pernah Dikirim
Nomor seri kamera, nama pemilik atau hak cipta yang disetel di kamera, lokasi (GPS), foto dan video, nama file, metadata pemotretan (EXIF), nama dan kata sandi Wi‑Fi, ID ponsel (IMEI, Android ID, ID iklan), nama, email, akun, atau teks pesan galat.

### Retensi
- Detail harian per perangkat disimpan selama 90 hari, setelah itu hanya total agregat harian yang tersisa.
- ID acak yang tidak aktif selama sekitar 13 bulan akan dihapus.
- Server secara niscaya melihat alamat IP Anda saat menangani permintaan; itu hanya digunakan untuk menentukan negara dan mencegah penyalahgunaan, dan **tidak pernah disimpan dalam data statistik**.

## Informasi Lokasi
- **Kirim lokasi ke kamera (Bluetooth)**: Ponsel Anda mengirim lokasinya ke kamera sehingga kamera menulisnya ke dalam foto.
- **Tambahkan lokasi ke JPEG yang diterima (ponsel)**: Nonaktif secara default. Saat diaktifkan, titik lokasi yang dicatat selama sesi penerimaan hanya tinggal di ponsel ini dan dihapus setelah 24 jam.
- Kedua sakelar berada di bawah **Pengaturan → Penerimaan & pemberitahuan → Lokasi foto** — lihat [Bab 3](03-receive.md#lokasi-foto-gps).
- Lokasi yang disematkan dalam foto berjalan bersama file saat Anda membagikan file asli. **Berbagi kode QR menghilangkan lokasi secara default.**

## Penggunaan Izin
| Izin | Tujuan |
|---|---|
| Bluetooth, Perangkat sekitar | Memasangkan dengan kamera, transfer foto Bluetooth, remote Bluetooth, menemukan kamera Wi‑Fi |
| Lokasi | Mengirim lokasi ke kamera atau menambahkannya ke foto; juga diperlukan oleh Android untuk membaca nama Wi‑Fi |
| Pemberitahuan | Kemajuan penerimaan, foto masuk, masalah transfer, peringatan baterai kamera lemah |
| Foto dan video | Menampilkan dan mengatur foto di Foto ponsel |

## Info Diagnostik
**Pengaturan → Dukungan → «Salin info diagnostik»** hanya menyalin teks ke papan klip Anda — **Anda yang memutuskan** apakah akan mengirimkannya kepada kami atau tidak. Ini mencakup versi aplikasi, status ponsel & jaringan, kemampuan kamera, dan log koneksi terbaru, dengan hanya 4 digit terakhir nomor seri kamera Anda. Sebelum menempelkan ke Issue GitHub publik, tinjau untuk memastikan tidak ada hal yang Anda lebih suka rahasiakan yang disertakan.
