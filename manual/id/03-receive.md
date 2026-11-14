<!-- translated from zh-TW at commit 968641f -->

# 3. Penerimaan Otomatis dan Penyimpanan

## Dasbor Kamera
Setelah terhubung, kartu atas di Beranda menunjukkan status langsung kamera Anda:

| Item | Detail |
|---|---|
| Model, lensa | Misalnya, «Nikon Z f» dan «NIKKOR Z 24–120 mm f/4» |
| Baterai | Persentase (menjadi merah pada 20% atau kurang) |
| Koneksi | Hotspot ponsel, Wi‑Fi yang sama, Wi‑Fi kamera, atau USB |
| Kartu memori | Ruang terpakai/total dan sisa jepretan untuk setiap kartu; slot ganda dicantumkan secara terpisah |
| Kualitas | Misalnya, `RAW` atau `JPEG fine★ L`; memperbarui secara otomatis saat Anda mengubah kualitas atau memasukkan/melepaskan kartu |
| Tujuan penyimpanan | Misalnya, «Menyimpan ke: kartu ✓» — lihat [Tujuan Penyimpanan dan Pemotretan Tanpa Kartu](#tujuan-penyimpanan-dan-pemotretan-tanpa-kartu) di bawah |
| Transfer | Status saat ini, dengan «Riwayat ›» di kanan atas |
| Gaya kamera | Slot C1–C9 terakhir dibaca — lihat [Bab 6](06-edit.md#gaya-kamera-c1c9-pro) |

Item yang tidak dilaporkan oleh kamera dalam mode saat ini akan disembunyikan. Beralih ke «Kontrol kamera» dan memasukkan Jarak Jauh biasanya membuka lebih banyak item status.

### Kelola Kamera
Perluas **Kelola kamera (n)** di bawah dasbor untuk mengedit, menghapus, atau menambahkan kamera. Halaman detail setiap kamera menunjukkan:
- Model, nomor seri (digit tengah disembunyikan; ketuk untuk mengungkapkan), versi firmware, **jumlah rana (shutter count)**, dan tanggal pembacaan.
- **Jumlah rana bulanan**: diagram batang selama 6 bulan terakhir (dilacak sejak Anda mulai menggunakan AeroCam).
- Waktu koneksi terakhir, metode, lensa, tingkat baterai, dan ruang kosong pada kartu memori.
- Jumlah file yang ditransfer ke ponsel Anda, tanggal koneksi pertama, dan profil jaringan yang disimpan.

Jumlah rana dibaca dari foto terbaru pada kartu memori, jadi harus ada setidaknya satu foto di kartu tersebut.

### Peringatan Baterai Lemah
Mengirim pemberitahuan saat baterai kamera turun ke ambang batas Anda (default 15%). Ini tidak akan memperingatkan lagi sampai baterai naik setidaknya 5% di atas ambang batas. Sesuaikan atau matikan di bawah **Pengaturan → Penerimaan & pemberitahuan**.

📷 Tangkapan layar: Dasbor kamera

---

## Penerimaan Otomatis (Pro)
1. Di Beranda, ketuk Wi‑Fi → **Mulai menerima**. Aplikasi menjaga koneksi latar belakang ke kamera (terlihat di laci pemberitahuan Anda).
2. Selama pemutaran di kamera, tekan **i → Kirim ke PC / Pilih untuk dikirim** (Send to PC / Select to send — kata-kata menu bervariasi menurut model), dan foto langsung ditransfer ke ponsel Anda.

Jika Anda ingin foto didorong secara otomatis begitu Anda menekan tombol rana, gunakan [Penerimaan FTP](08-ftp.md). Saat kabel USB dicolokkan, penerimaan beralih ke USB secara otomatis.

### Jeda Penerimaan
Saat penerimaan otomatis Wi‑Fi aktif, ketuk **⏸ Jeda** di kanan atas kartu «Transfer» (atau «Jeda» dalam pemberitahuan) untuk menjeda sementara:
- Wi‑Fi tetap terhubung, jadi Rol kamera dan Jarak jauh terus berfungsi secara normal.
- Foto yang antre di kamera menunggu hingga ketuk **Lanjutkan penerimaan**, lalu mentransfer secara berurutan. Foto apa pun yang sedang ditransfer selesai terlebih dahulu.
- Penerimaan dilanjutkan secara otomatis jika Anda mengetuk Lanjutkan, menghentikan penerimaan, menggesek aplikasi dari aplikasi terkini, kehilangan Wi‑Fi, mematikan kamera, atau mencolokkan kabel USB.

### Saat Terputus
- Jika koneksi turun, AeroCam terhubung kembali secara otomatis. Setelah beberapa kali percobaan ulang yang gagal, aplikasi mencari lagi berdasarkan ID kamera sehingga ia tetap menemukan kamera bahkan jika alamat IP-nya berubah.
- **Kamera beralih ke transfer Bluetooth**: Karena kamera hanya memiliki satu chip nirkabel, ia mematikan Wi‑Fi saat mengirim melalui Bluetooth. Beranda menampilkan «Kamera sedang mengirim foto melalui Bluetooth… Wi‑Fi akan terhubung kembali secara otomatis saat selesai» dan tidak memperlakukannya sebagai galat.
- **Rol kamera atau Jarak Jauh meminjam koneksi**: Kamera hanya menerima satu koneksi dalam satu waktu. Saat Anda membuka Rol kamera atau Jarak jauh, penerimaan otomatis melepaskan tautan dan melanjutkan secara otomatis saat Anda pergi.
- **Saat kamera tidak dapat ditemukan di Wi‑Fi**: Setelah waktu habis (default 3 menit), penerimaan berhenti secara otomatis dan memberi tahu Anda sehingga tidak menguras baterai Anda. Ubah waktu habis di bawah **Pengaturan → Penerimaan & pemberitahuan**.

---

## Aturan Penerimaan
Konfigurasikan ini di bawah **Pengaturan → Penerimaan & pemberitahuan**. Wi‑Fi, USB, dan FTP semuanya mengikuti aturan yang sama.

### Tipe File yang Diterima
Pilih apa yang akan disimpan: Semua file, Hanya JPG, JPG + RAW, Foto + video, atau Kustom (JPEG, RAW, HEIF, TIFF, Video, Lainnya).

Plus tiga sakelar tambahan (Pro):

| Sakelar | Apa yang dilakukannya |
|---|---|
| **Simpan JPEG saja dari RAW** | Hanya mengekstrak JPEG ukuran penuh yang disematkan di dalam file RAW (biasanya 2–5 MB alih-alih RAW 20–50 MB) pada resolusi penuh dengan metadata EXIF lengkap, disimpan sebagai `DSC_1234_S.JPG`. Bagus untuk berbagi sosial dan melihat sehari-hari |
| **Simpan JPEG terkompresi** | Mengompres ulang JPEG kamera yang masuk di ponsel Anda (`_S.JPG`, resolusi piksel yang sama, kualitas diatur dalam pengaturan Galeri) |
| **Ganti salinan terkompresi saat file asli tiba** | Menghapus salinan `_S.JPG` di ponsel Anda setelah JPEG asli disimpan |

> Untuk menerima file RAW, atur kualitas gambar kamera Anda ke RAW atau RAW+JPEG, dan atur opsi unggah «Hubungkan ke komputer» kamera ke RAW+JPEG (bukan «Hanya JPEG»). Kata-kata menu bervariasi menurut model.

### Aturan Lainnya
| Aturan | Detail |
|---|---|
| Mode penerimaan | Berkelanjutan, atau berhenti setelah menerima satu file |
| Video berukuran besar | Video yang lebih besar dari ambang batas (default 1024 MB) dilewati selama penerimaan otomatis, dicatat sebagai «Disaring», dan dapat diunduh secara manual |
| Folder penyimpanan | Berdasarkan kamera, Berdasarkan tanggal, Berdasarkan kamera dan tanggal, atau Berdasarkan tipe file |
| Penamaan file | Nama kamera asli (`DSC_1234.NEF`), Awalan tanggal (`20261011_DSC_1234.NEF`), atau Awalan tanggal & waktu (`20261011_153012_DSC_1234.NEF` — menjaga foto dari beberapa kamera diurutkan secara kronologis). Hanya berlaku untuk file yang baru disimpan |

### Tempat File Disimpan
- Foto: `Pictures/AeroCam/…`
- Video: `Movies/AeroCam/…`
- File lainnya: `Download/AeroCam/…`

Aplikasi lain seperti Google Photos dapat melihatnya segera. Jika Anda menghapus dan menginstal ulang AeroCam, gunakan **Pengaturan → Penyimpanan & baterai → «Pindai ulang foto ponsel»** untuk mengembalikan foto yang disimpan sebelumnya kembali ke galeri.

### Deteksi Duplikat
- Diperiksa menggunakan nomor seri kamera, nama file, ukuran, waktu pengambilan, dan hash file. Duplikat dilewati dan dicatat sebagai «Duplikat».
- Jika Anda menghapus foto di ponsel Anda (termasuk memindahkannya ke Sampah) dan mengirimkannya lagi, AeroCam menyimpannya lagi.
- Anda tidak perlu menghentikan dan memulai ulang penerimaan untuk mengirim ulang foto yang sama.

### Saat Foto yang Sama Tiba melalui Bluetooth dan Wi‑Fi
Wi‑Fi mentransfer file resolusi penuh, jadi Wi‑Fi diutamakan:
- Jika Wi‑Fi tiba terlebih dahulu dan Bluetooth mengirimkannya nanti: salinan Bluetooth diabaikan.
- Jika Bluetooth tiba terlebih dahulu dan Wi‑Fi menerima foto yang sama nanti, perilakunya mengikuti **Pengaturan → Penerimaan & pemberitahuan → «Foto yang sudah diterima melalui Bluetooth»**:
  - **Ganti dengan aslinya saat diterima melalui Wi‑Fi** (direkomendasikan): menyimpan file ukuran penuh dan menghapus salinan Bluetooth yang lebih kecil.
  - **Jangan unduh lagi melalui Wi‑Fi**.
  - **Simpan kedua salinan**.
- File RAW asli selalu disimpan.

---

## Tujuan Penyimpanan dan Pemotretan Tanpa Kartu
Mengontrol ke mana foto pergi saat Anda menekan tombol rana. AeroCam memeriksa apakah kartu memori dimasukkan dan memilih secara otomatis:
- **Kartu dimasukkan**: Menggunakan **Pengaturan → Pemotretan → Tujuan penyimpanan**:
  - **Kartu memori**: menyimpan ke kartu kamera.
  - **Kartu + ponsel** (Pro): menyimpan ke kartu dan menyalin ke ponsel Anda secara bersamaan.
- **Tidak ada kartu yang dimasukkan** (Pro): Secara otomatis beralih ke **Ponsel saja (penangkapan tanpa kartu)**. Anda dapat menekan tombol rana seperti biasa dan foto ditransfer langsung ke ponsel Anda, dinamai menurut waktu pengambilan (misalnya, `AC_20261025_193805.JPG`). Memasukkan kartu beralih kembali secara otomatis.

Berfungsi dari Beranda, Rol kamera, dan Jarak jauh, melalui Wi‑Fi dan USB.

**Pengaturan pertama kali:**
1. Di menu Pengaturan Kustom (Custom Settings) kamera, atur **Kunci pelepas slot kosong** (Slot empty release lock) ke **Aktifkan pelepas** (Enable release) (jika tidak, kamera akan memblokir rana saat tidak ada kartu yang dimasukkan).
2. Melalui Wi‑Fi, atur Tipe koneksi kamera ke **Kontrol kamera** (Camera control). Jika itu pada «Transfer gambar» (Image transfer), AeroCam mengingatkan Anda untuk beralih sekitar 3 detik setelah pemotretan pertama; foto tetap di-buffer di kamera dan ditransfer secara otomatis setelah Anda beralih. USB tidak memiliki batasan ini.
3. Koneksi satu ketukan tidak mendukung pemotretan tanpa kartu — gunakan hotspot ponsel atau Wi‑Fi yang sama sebagai gantinya.

**Pesan bilah status** (atas Beranda dan Rol kamera):

| Pesan | Arti |
|---|---|
| Menyimpan ke: kartu ✓ | Menyimpan ke kartu memori kamera |
| Menyimpan ke: kartu + ponsel ✓ | Menyimpan ke kartu dan ponsel Anda |
| Menyimpan ke: ponsel saja (tidak ada kartu di kamera) | Foto mentransfer langsung ke ponsel Anda |
| Kamera berada dalam mode «Image transfer»… (merah) | Alihkan Tipe koneksi ke «Kontrol kamera» (Camera control) |
| Wi‑Fi satu ketukan: tidak ada kartu memori, tidak dapat memotret (merah) | Masukkan kartu, atau beralih ke hotspot / Wi‑Fi yang sama |
| Kartu memori penuh (merah) | Tukar kartu atau kosongkan ruang (tidak beralih otomatis ke ponsel saja) |
| Tidak ada kartu memori di kamera, tidak dapat memotret (merah) | Tingkat gratis, atau ponsel memiliki ruang kosong kurang dari 1 GB |

> Perekaman video tidak tersedia tanpa kartu memori, dan pemotretan berkelanjutan lebih lambat karena setiap foto harus ditransfer ke ponsel.

---

## Lokasi Foto (GPS)
Di bawah **Pengaturan → Penerimaan & pemberitahuan → Lokasi foto**, ada dua sakelar:
- **Kirim lokasi ke kamera (Bluetooth)** (aktif secara default): Saat kamera menyala atau mengirim melalui Bluetooth, ponsel Anda mengirim lokasi GPS-nya ke kamera sehingga kamera menyematkannya di foto baru.
- **Tambahkan lokasi ke JPEG yang diterima (ponsel)**: Menambahkan lokasi ponsel Anda berdasarkan waktu pengambilan ke JPEG yang diterima melalui Wi‑Fi, USB, FTP, unduhan galeri, atau pemotretan jarak jauh. Bertanya sekali saat pertama kali Anda mulai menerima.
  - File RAW tidak pernah dimodifikasi, dan foto yang sudah memiliki data GPS mempertahankan koordinat aslinya.
  - Riwayat lokasi yang dicatat selama sesi hanya tinggal di ponsel Anda dan dihapus setelah 24 jam.
  - Jika waktu pengambilan tidak cocok dengan titik yang tercatat, tidak ada yang ditulis (lebih baik tidak ada lokasi daripada lokasi yang salah).
  - AeroCam harus dibuka saat Anda mulai menerima untuk merekam lokasi.

> Koordinat GPS yang disematkan berjalan bersama file asli saat Anda membagikannya. Berbagi kode QR menghapus GPS secara default — lihat [Bab 4](04-gallery.md#berbagi-kode-qr).

---

## Riwayat
Ketuk **Riwayat ›** di kanan atas kartu «Transfer» di Beranda. Mencantumkan setiap hasil penerimaan, unduhan galeri, dan pengambilan jarak jauh (Berhasil, Duplikat, Dilewati, Gagal) dengan gambar mini.
- Ketuk entri apa saja untuk pratinjau layar penuh di dalam aplikasi.
- Cari, filter berdasarkan kamera, atau bersihkan riwayat. Menghapus riwayat tidak menghapus file di ponsel Anda.
