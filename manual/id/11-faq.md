<!-- translated from zh-TW at commit 968641f -->

# 11. FAQ dan Pemecahan Masalah

## Umum
**Bisakah saya mentransfer foto dari kamera ke ponsel tanpa meningkatkan ke Pro?**
Ya. Pada tingkat Gratis, Anda dapat menerima otomatis JPEG ukuran kecil ~2 MP melalui Bluetooth, atau menelusuri kartu SD kamera melalui kabel USB dan secara manual memilih serta mengunduh file asli beresolusi penuh.

**Apakah Beta atau kunci uji berbayar?**
Tidak. Keduanya diterbitkan secara gratis hanya di GitHub di AeroCam-Releases. Jika seseorang meminta Anda membayar, itu bukan saluran resmi.

**Aplikasi menunjukkan «Ini bukan versi resmi» saat diluncurkan**
APK telah dikemas ulang oleh pihak ketiga. Ini tidak akan menerima kunci uji dan mungkin berisi kode yang tidak diinginkan. Copot pemasangannya dan unduh ulang dari AeroCam-Releases.

**Setelah memperbarui, kamera dan kunci uji saya yang dipasangkan hilang**
Mulai dari 92.03.09, build yang lebih baru dipasang sebagai aplikasi terpisah dan tidak memigrasikan data dari build lama. Pasangkan kembali kamera Anda dan masukkan kunci uji lagi.

**Di mana foto disimpan?**
Foto masuk ke `Pictures/AeroCam`, video ke `Movies/AeroCam`, dan file lain ke `Download/AeroCam`. Google Photos dan aplikasi galeri lainnya dapat melihatnya. File yang disimpan oleh build yang lebih lama dari 92.03.09 tetap berada di folder asli mereka.

**Saya menghapus foto di ponsel saya dan ingin mentransfernya lagi**
Cukup kirimkan lagi dari kamera — AeroCam mendeteksi bahwa file tersebut tidak lagi ada di ponsel Anda dan menyimpannya.

**Foto tidak muncul setelah dipulihkan dari Sampah atau menginstal ulang aplikasi**
Jalankan **Pengaturan → Penyimpanan & baterai → «Pindai ulang foto ponsel»**.

---

## Koneksi
**Tidak dapat terhubung ke kamera melalui Wi‑Fi**
1. Pastikan kamera berada di layar «Hubungkan ke komputer» dengan ikon Wi‑Fi terlihat; setengah tekan rana jika layar tertidur.
2. Periksa Tipe koneksi: gunakan **Transfer gambar** (Image transfer) untuk penerimaan otomatis dan galeri; gunakan **Kontrol kamera** (Camera control) untuk pemotretan jarak jauh dan pemotretan tanpa kartu.
3. Mode hotspot ponsel: konfirmasikan hotspot Anda aktif dan kamera terhubung dengannya.
4. Mode Wi‑Fi yang sama: konfirmasikan bahwa ponsel dan kamera berada di SSID yang persis sama (ponsel terkadang beralih secara otomatis ke Wi‑Fi lain atau data seluler).
5. Coba **Koneksi satu ketukan** — tidak perlu hotspot atau router.
6. Ketuk **ⓘ** dan telusuri panduan koneksi visual langkah demi langkah.

**Kamera tidak pernah ditemukan di Wi‑Fi hotel atau konvensi**
Jaringan Wi‑Fi publik biasanya memblokir lalu lintas perangkat-ke-perangkat. Beralihlah ke hotspot ponsel Anda atau Koneksi satu ketukan.

**Kamera mengatakan «Sudah dipasangkan dengan perangkat lain»**
Profil jaringan kamera tersebut dipasangkan dengan aplikasi yang berbeda. Buat profil jaringan baru di kamera dan pasangkan lagi.

**Koneksi satu ketukan tidak dapat menemukan Wi‑Fi kamera**
Setelah menerima perintah Bluetooth, kamera membutuhkan waktu 10–30 detik untuk memunculkan Wi‑Fi-nya, dan AeroCam mencoba lagi secara otomatis. Jika masih gagal, periksa kembali kata sandi Wi‑Fi kamera Anda.

**Hotspot ponsel terus mati**
Beberapa ponsel mematikan hotspot mereka saat perangkat yang terhubung tidak menggunakan data internet. Nonaktifkan «Matikan hotspot secara otomatis» di pengaturan hotspot ponsel Anda, atau gunakan Koneksi satu ketukan.

**Kamera tidak mau terhubung kembali setelah mengalihkan hotspot ponsel**
Alamat IP hotspot ponsel Anda mungkin telah berubah. Penerimaan otomatis Wi‑Fi menemukan kamera secara otomatis, sementara FTP memerlukan pembaruan IP server pada kamera.

**Tidak ada yang terjadi saat mencolokkan USB**
1. Konfirmasikan pengaturan USB kamera adalah **MTP/PTP**.
2. Pastikan kabel mendukung transfer data (beberapa kabel hanya untuk mengisi daya).
3. Ketuk Izinkan pada prompt akses USB Android.
4. Ketuk `⋮` di kanan atas ubin USB → **Uji USB** untuk melihat langkah mana yang gagal.

**Penerimaan latar belakang terus terganggu**
Nonaktifkan pengoptimalan baterai di bawah **Pengaturan → Penyimpanan & baterai**. Pada ponsel Xiaomi, OPPO, dan sejenisnya, atur juga AeroCam ke penggunaan baterai «Tidak dibatasi» di pengaturan sistem.

---

## Bluetooth
**Transfer foto Bluetooth macet**
- Saat memotret RAW, kamera harus mengonversi setiap gambar ke JPEG sebelum mengirim, dan mengoperasikan kamera membatalkan transfer. Cara kerjanya paling baik jika Anda mematikan kamera setelah memotret dan membiarkannya mentransfer di latar belakang.
- Ketuk **Putuskan dan sambungkan kembali** pada ubin Bluetooth, atau **⋮ → Mulai ulang layanan Bluetooth** (pasangan Anda dipertahankan).

**Menekan AF pada remote Bluetooth tidak fokus**
Kamera harus mengizinkan AF rana setengah tekan. Jika Anda menggunakan AF‑ON tombol belakang, periksa Pengaturan Kustom kamera Anda untuk memastikan **Aktivasi AF** (AF activation) diatur ke **Rana/AF-ON**.

**Apakah menerima foto yang sama melalui Bluetooth dan Wi‑Fi akan menyimpan dua salinan?**
Tidak secara default: ketika Wi‑Fi menerima file asli, ia secara otomatis menghapus salinan Bluetooth yang lebih kecil. Anda dapat mengubahnya di bawah **Pengaturan → Penerimaan & pemberitahuan → «Foto yang sudah diterima melalui Bluetooth»**.

---

## Pemotretan Jarak Jauh
**Tidak dapat menyesuaikan kecepatan rana atau ISO**
- Kecepatan rana memerlukan mode S atau M; bukaan memerlukan mode A atau M; matikan ISO Otomatis sebelum menyesuaikan ISO secara manual.
- Pada kamera dengan dial fisik seperti Zf: atur dial kecepatan rana ke **1/3 STEP** dan dial ISO ke **C**.

**Mengetuk pratinjau tidak memindahkan titik fokus**
Atur mode area AF kamera ke mode yang memungkinkan titik bergerak (seperti AF titik tunggal). Dalam AF Area Otomatis, kamera memilihnya secara otomatis.

**Beberapa item dasbor hilang (lensa, sisa jepretan, jumlah rana)**
Beberapa kamera melaporkan detail tertentu hanya dalam mode tertentu. Beralih ke «Kontrol kamera» dan memasukkan Jarak jauh biasanya membuatnya tersedia. Jumlah rana memerlukan setidaknya satu foto pada kartu memori.

**Di mana saya dapat melihat suhu warna yang tepat (Kelvin)?**
Nikon menyimpan nilai Kelvin yang diukur dalam tag MakerNote yang dienkripsi, sehingga «Detail» menampilkan nama prasetel White Balance saja.

---

## Tujuan Penyimpanan dan Pemotretan Tanpa Kartu
**Menekan tombol tidak melakukan apa pun saat tidak ada kartu yang dimasukkan**
Konfirmasikan **Kunci pelepas slot kosong** diatur ke **Aktifkan pelepas** pada kamera, dan AeroCam terhubung (bilah status menunjukkan «ponsel saja»).

**Foto menunjukkan «DEMO» di kamera**
Jika tidak ada kartu yang dimasukkan dan AeroCam tidak terhubung dalam mode «ponsel saja», kamera menandai jepretan sebagai **DEMO** dan tidak menyimpannya. Masukkan kartu atau memotret saat terhubung ke AeroCam.

**Foto tidak sampai ke ponsel saya, dan spanduk merah muncul di bagian atas Beranda**
- «Kamera berada dalam mode "Image transfer"»: Memotret tanpa kartu memerlukan **Kontrol kamera**. Beralih mode pada kamera; ia akan terhubung kembali dan mentransfer jepretan yang di-buffer secara otomatis.
- «Wi‑Fi satu ketukan: tidak ada kartu memori»: Koneksi satu ketukan tidak mendukung pengambilan gambar tanpa kartu. Masukkan kartu atau beralih ke hotspot / Wi‑Fi yang sama.

**«Koneksi terputus» muncul**
Saat menyimpan ke ponsel saja, menjatuhkan koneksi selama lebih dari 10 detik memicu peringatan karena foto yang diambil saat terputus tidak disimpan ke kartu. AeroCam pulih secara otomatis setelah terhubung kembali.

---

## Pengeditan dan Gaya
**NEF tidak mau terbuka atau tidak dapat diedit**
File NEF Efisiensi tinggi / Efisiensi tinggi★ diedit menggunakan JPEG ukuran penuh tersematnya; file yang hanya berisi pratinjau kecil tidak dapat diedit. Untuk mengembangkan file RAW lengkap di ponsel Anda, alihkan kamera ke **Kompresi lossless** — lihat [Bab 6](06-edit.md#raw-yang-dapat-diedit-di-ponsel-alihkan-kompresi-raw-kamera).

**Tampilan .np3 berbeda dari kamera**
Editor ponsel mensimulasikan kurva dan saturasi; Color Blender dan Color Grading belum disimulasikan, jadi hasilnya adalah perkiraan. Jika JPEG sudah memiliki Picture Control yang diterapkan di kamera, efeknya bertumpuk.

**Warna terlihat berbeda setelah menulis .np3 ke kamera**
Slot kamera kustom hanya menerima **Dasar + Kurva + Penajaman**; Saturasi, Color Blender, dan Color Grading tidak dapat ditulis melalui koneksi. Untuk hasil penuh, salin file `.np3` ke kartu memori dan impor melalui menu kamera.

**Penyambungan panorama gagal atau melewatkan foto**
Setiap bingkai membutuhkan sekitar 30% tumpang tindih dengan bingkai yang berdampingan. File yang tidak cocok dicantumkan berdasarkan nama, dan panorama kisi memerlukan semua ubin untuk hadir sebelum menyambung.

---

## FTP
**Kamera menampilkan Err.31 atau Err.32**
Perbarui ke Beta terbaru, dan periksa kembali bahwa alamat IP, port `2121`, nama pengguna `aerocam`, dan kata sandi pada kamera cocok dengan ubin FTP AeroCam, dengan mode pasif diaktifkan.

**Kamera menampilkan kegagalan masuk**
Kata sandi harus cocok persis dengan yang ditampilkan di FTP AeroCam (peka huruf besar-kecil). Jika Anda mengetuk «Buat ulang» kata sandi, perbarui juga di kamera.

**Saat FTP berjalan, Rol kamera atau Jarak Jauh tidak dapat terhubung**
Saat dalam mode FTP, kamera tidak menerima koneksi Wi‑Fi untuk galeri atau pemotretan jarak jauh. Gunakan kabel USB, atau hentikan penerimaan FTP dan alihkan kamera kembali ke «Hubungkan ke komputer».

---

## Lainnya
**Aplikasi mogok (crash)**
Buka kembali AeroCam, buka **Pengaturan → Support → «Salin info diagnostik»**, dan tempelkan saat [melaporkan masalah](12-report.md) — ini mencakup jejak tumpukan kerusakan terakhir.

**Bagaimana cara mematikan statistik penggunaan anonim?**
Nonaktifkan **Pengaturan → Support → «Kirim statistik penggunaan anonim»** — lihat [Privasi dan Statistik Anonim](10-privacy.md).
