<!-- translated from zh-TW at commit 968641f -->

# 8. Penerimaan FTP (Pro)

Kamera Anda **mendorong foto langsung ke ponsel Anda melalui FTP** tepat setelah Anda mengambil setiap foto — tidak perlu memilih foto di kamera atau membuka galeri. Diuji pada Nikon Zf, setiap file RAW ~18 MB tiba di ponsel dalam waktu sekitar 1 detik.

AeroCam memiliki server FTP bawaan, jadi **Anda tidak perlu menyiapkan server eksternal apa pun**.

## Terbaik Untuk
- Acara, pernikahan, dan olahraga: foto mengalir ke ponsel Anda saat Anda memotret.
- Peninjauan instan dan berbagi sosial tepat setelah mengambil foto.

## Persyaratan
- Kamera dengan pengunggahan FTP bawaan (Nikon Z f, Z 8, Z 9, Z 6III, dll.).
- **Hotspot seluler** ponsel Anda dihidupkan dengan kamera yang terhubung dengannya (atau keduanya terhubung ke router yang sama).
- Kartu memori dimasukkan ke dalam kamera (FTP mentransfer file dari kartu).

## Pengaturan Pertama Kali
1. Nyalakan hotspot ponsel Anda.
2. Di AeroCam, buka kartu **FTP** di Beranda → ketuk **Mulai menerima** di bagian atas. Kartu menampilkan detail server — ketuk bidang apa saja untuk menyalinnya:
   - Alamat server (misalnya, `10.14.29.30`)
   - Port: `2121`
   - Nama pengguna: `aerocam`
   - Kata sandi: Kata sandi 8 karakter yang dihasilkan oleh aplikasi (ketuk «Buat ulang» kapan saja)
   - Mode pasif (PASV): **Aktif**
3. Pada kamera Anda: **MENU → Menu jaringan (Network menu) → Hubungkan ke server FTP (Connect to FTP server) → Pengaturan jaringan (Network settings) → Buat profil (Create profile)**:
   - Pilih hotspot ponsel Anda untuk Wi‑Fi.
   - Pilih `FTP` sebagai tipe server, masukkan alamat, port, nama pengguna, dan kata sandi di atas, dan aktifkan mode pasif.
4. Aktifkan koneksi FTP ini pada kamera. Pengaturan selesai setelah ubin FTP AeroCam menunjukkan «Terhubung».
5. Di menu FTP kamera, nyalakan **Kirim otomatis** (Auto send / kirim setelah pemotretan) sehingga setiap foto baru ditransfer secara otomatis.

Tidak yakin tentang langkah apa pun? Ketuk **ⓘ** di sebelah ubin FTP untuk panduan visual.

📷 Tangkapan layar: Kartu pengaturan FTP yang diperluas

## Selama Penggunaan
- Indikator status: Mati, Berjalan · Menunggu kamera, Terhubung, Menerima, atau Galat.
- Pemberitahuan menunjukkan «Menerima FTP · N diterima» beserta nama file dan kecepatan transfer saat ini.
- Foto disimpan menggunakan aturan **Pengaturan → Penerimaan & pemberitahuan** Anda (folder, nama file, JPEG saja, Simpan JPEG saja dari RAW, dll.) dan dicatat dengan sumber `FTP`.
- Jika transfer turun atau kamera mati di tengah file, file parsial akan dihapus secara otomatis sehingga file yang rusak tidak pernah muncul di galeri Anda.
- Setelah mematikan kamera, status diperbarui menjadi terputus dalam waktu ~1 menit; menyalakan kembali kamera akan menghubungkan kembali secara otomatis.
- **Penghentian otomatis menganggur**: **Pengaturan → Penerimaan & pemberitahuan → «Penghentian otomatis menganggur FTP»** (Tidak pernah, 5, 10, atau 30 menit). Menghitung dari foto terakhir yang diterima, tidak pernah berhenti di tengah transfer, dan memberi tahu Anda saat berhenti.

## Hal yang Perlu Diingat
- **Tetap nyalakan hotspot Anda.** Beberapa ponsel mematikan hotspot secara otomatis ketika tidak ada perangkat yang menggunakan data internet — nonaktifkan «Matikan hotspot secara otomatis» di pengaturan hotspot ponsel Anda.
- Menyalakan dan mematikan hotspot Anda dapat mengubah alamat IP ponsel Anda; perbarui di kamera jika perlu.
- Penerimaan FTP dan **penerimaan otomatis Wi‑Fi tidak dapat berjalan secara bersamaan** — memulai salah satu akan otomatis menghentikan yang lain.
- Saat FTP aktif, kamera berada dalam mode FTP, jadi **Rol kamera dan Jarak jauh tidak dapat terhubung melalui Wi‑Fi**. Gunakan kabel USB sebagai gantinya, atau hentikan penerimaan FTP dan alihkan kamera kembali ke «Hubungkan ke komputer» (Connect to PC).
- Server FTP hanya mengikat ke hotspot atau jaringan Wi‑Fi lokal Anda dan tidak pernah terekspos ke internet publik.
- Koneksi satu ketukan tidak dapat digunakan dengan FTP (Koneksi satu ketukan memulai Wi‑Fi kamera itu sendiri, sedangkan FTP mengharuskan kamera bergabung ke jaringan ponsel Anda).

## Mengirim Langsung ke NAS
Anda juga dapat mengarahkan pengaturan FTP kamera Anda langsung ke NAS rumah tanpa melalui ponsel. Itu adalah fitur kamera bawaan dan tidak memerlukan AeroCam.
