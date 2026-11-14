<!-- translated from zh-TW at commit 968641f -->

# 2. Menghubungkan Kamera Anda

AeroCam memiliki empat metode koneksi. Anda dapat mengatur lebih dari satu, dan aplikasi secara otomatis menggunakan metode mana pun yang tersedia. Keempat ubin di Beranda (Wi‑Fi, USB, Bluetooth, FTP) menunjukkan status saat ini.

> Tidak yakin cara menghubungkan? Ketuk **ⓘ** di sebelah status koneksi di Beranda, atau di kanan atas setiap langkah di «Tambah kamera», untuk membuka panduan visual (masing-masing satu halaman untuk hotspot ponsel, Wi‑Fi yang sama, koneksi satu ketukan, USB, Bluetooth, dan FTP) dengan tangkapan layar untuk ponsel dan kamera, plus daftar centang pemecahan masalah di bagian akhir.

## Cara Memilih

| Apa yang Anda inginkan | Opsi terbaik |
|---|---|
| Menerima foto bahkan saat kamera dimatikan, bebas repot | **Bluetooth** (JPEG lebih kecil, gratis) |
| Di luar ruangan, tidak perlu hotspot, inginkan file asli, galeri, dan pemotretan jarak jauh | **Koneksi satu ketukan** (Pro) |
| Transfer otomatis instan tepat setelah setiap pemotretan, kecepatan nirkabel tercepat | **[Penerimaan FTP](08-ftp.md)** (Pro, memerlukan hotspot) |
| Koneksi paling andal, monitor video, sesi jarak jauh yang lama | **Kabel USB** (pilih & unduh manual gratis) |
| Di rumah atau di studio | **Wi‑Fi yang sama** (Pro) |

## Referensi Kecepatan (Diuji pada Nikon Zf + Pixel 10 Pro)

| Metode | Satu file RAW (sekitar 18 MB) |
|---|---|
| Penerimaan FTP | Sekitar 1 detik (sekitar 17 MB/s) |
| Unduhan galeri Wi‑Fi | Sekitar 1,3 detik (sekitar 13 MB/s) |
| USB | Biasanya lebih cepat daripada Wi‑Fi, tergantung kabel (sekitar 35 MB/s pada kabel USB 2.0) |
| Bluetooth | JPEG lebih kecil (sekitar 2 MB), 15–20 detik per foto |

## Lampu Status di Beranda
Ubin Wi‑Fi, USB, Bluetooth, dan FTP berubah warna berdasarkan status (abu-abu saat tidak terhubung):

| Warna | Arti |
|---|---|
| 🟢 Hijau | Terhubung atau siap (hijau pucat pada Bluetooth = siaga, siap untuk Kirim saat mati) |
| 🔵 Biru | Mentransfer |
| 🟠 Oranye | Menghubungkan (berkedip), atau perlu perhatian (izin, macet, galat) |
| 🔴 Merah | Wi‑Fi atau Bluetooth ponsel dimatikan |

---

## Bluetooth (Gratis, Menggantikan SnapBridge)

### Pasangan (Pairing)
1. Pada kamera: **MENU → Menu jaringan (Network menu) → Hubungkan ke smart dev (Connect to smart device) → Pairing (Bluetooth) → Mulai pairing (Start pairing)**.
2. Jika kamera Anda dipasangkan dengan SnapBridge, hapus pemasangan di SnapBridge terlebih dahulu dan lupakan kamera di pengaturan Bluetooth ponsel Anda (dua aplikasi tidak dapat dipasangkan ke kamera yang sama secara bersamaan).
3. Di AeroCam: Beranda «Bluetooth» → **Pasangkan kamera** → Mulai. Baik ponsel maupun kamera menunjukkan kode yang sama — konfirmasikan pada keduanya. Kamera menunjukkan ponsel Anda sebagai `AeroCam_<model ponsel>`.

📷 Tangkapan layar: Ubin Bluetooth

### Setelah Pasangan
Setelah dipasangkan, Bluetooth tetap aktif hingga Anda membatalkan pasangan (yang meminta konfirmasi terlebih dahulu).
- Biasanya, AeroCam hanya **mendengarkan** sinyal Bluetooth di latar belakang dan tidak akan membangunkan kamera yang sedang tidur.
- **Saat Anda menyalakan kamera**: AeroCam terhubung sebentar untuk menyinkronkan waktu dan lokasi GPS ponsel Anda (sehingga kamera menyematkan lokasi di foto baru), kemudian memutuskan sambungan.
- **Saat kamera memiliki foto untuk dikirim**: Aktifkan **Kirim saat mati** (Send while off) di menu «Connect to smart device» pada kamera. Kamera secara otomatis terhubung melalui Bluetooth untuk mengirim foto, bahkan setelah Anda mematikannya.
- Foto yang diterima adalah JPEG sekitar 2 MB yang dihasilkan oleh kamera (pemotretan RAW juga dikonversi ke JPEG oleh kamera terlebih dahulu), membutuhkan waktu sekitar 15–20 detik per foto. Gunakan Wi‑Fi, USB, atau FTP untuk file asli.
- Untuk menarik foto segera, ketuk **Terima sekarang** pada ubin Bluetooth.
- Layanan dilanjutkan secara otomatis setelah mengaktifkan/menonaktifkan Bluetooth, mem-boot ulang ponsel Anda, atau memperbarui aplikasi. Saat menunggu, Android mewajibkan pemberitahuan persisten berprioritas rendah, yang dapat Anda sembunyikan di pengaturan sistem.

### Status Ubin Bluetooth
🟢 Kamera di dekatnya · Menyala / 🟢 Hijau pucat: Siaga (Kirim saat mati siap) / ⚪ Kamera tidak terlihat (menunjukkan waktu terakhir terlihat) / 🔵 Mentransfer / 🟠 Mungkin macet / 🔴 Bluetooth ponsel mati.

Karena Bluetooth tidak tetap terhubung secara terus-menerus, ubin ini menunjukkan apakah kamera terdeteksi di sekitar dan apa yang sedang dilakukannya saat ini.

### Jika Transfer Macet
- Jika tidak ada data yang masuk selama 30 detik selama transfer, aplikasi akan memutuskan sambungan secara otomatis dan kamera akan mencoba lagi nanti; setelah 20 detik tidak ada aktivitas, ubin berubah menjadi kuning («Mungkin macet»).
- **Putuskan dan sambungkan kembali**: memutuskan hanya sesi transfer saat ini.
- **⋮ → Mulai ulang layanan Bluetooth**: memulai ulang seluruh layanan Bluetooth latar belakang sambil tetap mempertahankan pasangan Anda.
- Saat memotret RAW, kamera harus mengonversi setiap file ke JPEG sebelum mengirim; mengoperasikan kamera selama transfer (menengah-tekan tombol rana atau mengambil foto) akan membatalkan transfer. Cara terbaik adalah mematikan kamera setelah memotret dan biarkan ia mengirim di latar belakang.

---

## Wi‑Fi (Pro): Tiga Cara untuk Menghubungkan

| Metode | Cara kerjanya | Kapan menggunakannya |
|---|---|---|
| **Koneksi satu ketukan** (direkomendasikan) | Menggunakan Bluetooth untuk memberi tahu kamera agar menyalakan Wi‑Fi sendiri, lalu ponsel terhubung secara otomatis | Di luar ruangan, saat Anda tidak ingin menyalakan hotspot |
| **Hotspot ponsel** (direkomendasikan dalam panduan) | Kamera terhubung ke hotspot seluler ponsel Anda | Saat koneksi satu ketukan tidak stabil, atau saat menggunakan FTP atau memotret tanpa kartu |
| **Wi‑Fi yang sama** | Ponsel dan kamera terhubung ke router yang sama | Di rumah atau di studio |

### Koneksi Satu Ketukan
1. Selesaikan **pasangan Bluetooth** terlebih dahulu.
2. Di Beranda, ketuk Wi‑Fi → «Koneksi satu ketukan».
3. Pertama kali, masukkan **kata sandi** Wi‑Fi kamera Anda (nama jaringan, seperti `NIKON_…`, diisi secara otomatis). Ini hanya disimpan di ponsel Anda.
4. Ketika Android meminta izin untuk mengizinkan koneksi Wi‑Fi, ketuk Izinkan.
5. Setelah «Terhubung ke Wi‑Fi kamera» muncul, galeri, pemotretan jarak jauh, dan penerimaan otomatis semuanya menggunakan tautan ini. Ketuk «Putuskan» untuk kembali ke Wi‑Fi normal Anda.

Jika galeri atau pemotretan jarak jauh belum terhubung, Anda juga akan melihat tombol «Hubungkan melalui Wi‑Fi kamera» tepat di layar.

> - Saat terhubung ke Wi‑Fi kamera, ponsel Anda menggunakan data seluler untuk akses internet.
> - Koneksi satu ketukan **tidak dapat digunakan dengan FTP**, dan **tidak mendukung pemotretan tanpa kartu** (gunakan hotspot ponsel atau Wi‑Fi yang sama ketika tidak ada kartu di kamera).

📷 Tangkapan layar: Kartu koneksi satu ketukan dan status terhubung

### Hotspot Ponsel / Wi‑Fi yang Sama (Pasangan Pertama Kali)
1. Pada kamera: **MENU → Menu jaringan (Network menu) → Hubungkan ke komputer (Connect to PC)**, dan buat profil jaringan (menghubungkan ke hotspot ponsel atau Wi‑Fi rumah Anda).
   - Model baru (dengan «Tipe koneksi» di menu): atur «Connection type» ke **Transfer gambar** (Image transfer).
   - Model sebelumnya: cukup pilih **Hubungkan ke komputer** (Connect to PC).
2. Di AeroCam: **Beranda → «＋» Tambah kamera**, dan pilih metode koneksi (Wi‑Fi yang sama atau Hotspot ponsel). Aplikasi memeriksa jaringan Anda dan mencari kamera secara otomatis; Anda juga dapat memasukkan IP-nya secara manual.
3. Layar kamera menampilkan **PIN 4 digit**. Masukkan di ponsel Anda, lalu tekan OK pada kamera.
4. Setelah dipasangkan, ini disimpan sebagai profil kamera sehingga Anda dapat terhubung langsung lain kali. Anda dapat menyimpan beberapa kamera dan beberapa jaringan; Anda **tidak perlu memasangkan ulang** setelah pembaruan aplikasi, dan AeroCam menemukan kamera bahkan jika alamat IP-nya berubah.

> Jika kamera mengatakan «Sudah dipasangkan dengan perangkat lain», profil jaringan kamera tersebut digunakan oleh aplikasi lain. Buat profil baru pada kamera dan pasangkan lagi.

📷 Tangkapan layar: Wisaya tambah kamera dan masukkan PIN

### Pemeriksaan Pra-koneksi
- Saat Anda mengetuk «Mulai menerima» atau membuka Rol kamera / Jarak jauh, AeroCam memeriksa jaringan Anda terlebih dahulu. Jika profil menggunakan «Hotspot ponsel» sementara hotspot dimatikan, atau «Wi‑Fi yang sama» sementara ponsel Anda tidak terhubung dengannya, spanduk kuning akan muncul (misalnya, «Harap nyalakan hotspot ponsel Anda terlebih dahulu») dengan tombol cepat untuk «Pengaturan hotspot» dan «Pengaturan Wi‑Fi». Setelah diaktifkan, kembali ke AeroCam dan spanduk akan hilang.
- Jika kamera tidak dapat ditemukan di Wi‑Fi atau hotspot, Beranda menampilkan «Kamera tidak ditemukan di jaringan» (biasanya karena «Hubungkan ke komputer» tidak aktif di kamera) dengan tombol «Lihat panduan koneksi».

### «Connection type» (Tipe koneksi) Kamera
Pada model baru (Z9, Z8, Z6III, Zf, Z5II, Z50II…): **MENU → Menu jaringan (Network menu) → Hubungkan ke komputer (Connect to PC) → Tipe koneksi (Connection type)**
- **Transfer gambar** (Image transfer): untuk penerimaan otomatis dan menelusuri kartu SD kamera.
- **Kontrol kamera** (Camera control): untuk pemotretan jarak jauh dan pemotretan tanpa kartu.

Mengalihkan mode akan memutuskan sebentar Wi‑Fi kamera; AeroCam terhubung kembali secara otomatis tanpa memasangkan ulang. Jika Anda membuka Jarak Jauh saat kamera masih dalam «Image transfer», aplikasi akan menampilkan langkah-langkah untuk beralih.

---

## Kabel USB
Lebih cepat dan lebih andal daripada Wi‑Fi. **Tidak perlu pemasangan**, dan Anda tidak perlu menambahkan kamera terlebih dahulu.
1. Atur opsi USB kamera Anda ke **MTP/PTP** (bukan «iPhone» atau «UVC/UAC»).
2. Gunakan kabel USB‑C **yang mendukung data** (beberapa kabel hanya untuk mengisi daya). Kabel USB 3 berperingkat 5Gbps/10Gbps memberikan kecepatan terbaik.
3. Di Beranda, ubin USB menunjukkan «Z f terdeteksi · Izin akses diperlukan» → ketuk «Beri akses» dan konfirmasikan prompt Android sekali.

### Warna Ubin USB
| Warna | Arti |
|---|---|
| ⚪ Abu-abu | Tidak ada kamera yang terdeteksi (atau kabel hanya untuk mengisi daya) |
| 🟠 Oranye | Kamera terdeteksi; izin akses diperlukan |
| 🔴 Merah | Pengaturan USB kamera bukan MTP/PTP, izin ditolak, atau tes gagal (menunjukkan alasan) |
| 🟢 Hijau | Terhubung melalui USB |

### Saat Terhubung Melalui USB
- Rol kamera, Jarak jauh, dan penerimaan otomatis **secara otomatis beralih ke USB**; mencabut kabel akan beralih kembali ke Wi‑Fi. Menyolokkan saat pemotretan jarak jauh Wi‑Fi juga beralih ke USB dengan mulus (kecuali saat interval timer, bracketing, atau eksposur Bulb sedang berjalan).
- **Penerimaan USB** (Pro): Ketuk «Mulai menerima» pada ubin USB untuk menyimpan foto yang baru diambil dan foto yang dikirim melalui «Kirim ke PC» di kamera. Diaktifkan secara otomatis saat dicolokkan secara default (**Pengaturan → Pemotretan → «Mulai otomatis menerima saat kabel USB dicolokkan»**).
- **Sinkronisasi jam**: Menyinkronkan jam kamera saat dicolokkan (hanya menyesuaikan jika meleset lebih dari 2 detik; bertanya terlebih dahulu jika meleset lebih dari 1 hari).
- **Tetap bangun**: Mengirim sinyal tetap hidup kecil setiap 10 detik saat Rol kamera atau Jarak Jauh terbuka agar kamera tidak tidur; berhenti setelah 30 menit tidak aktif atau saat baterai kamera lemah.
- Ponsel Anda mungkin memasok daya ke kamera melalui USB — pertimbangkan untuk menggunakan bank daya untuk sesi yang lama.
- **Uji USB** (⋮ di kanan atas ubin USB): menguji koneksi, info kamera, kartu memori, kecepatan bingkai tampilan langsung, dan kecepatan baca.

📷 Tangkapan layar: Ubin USB

---

## FTP
Kamera mendorong foto langsung ke ponsel Anda segera setelah Anda memotret — lihat [Bab 8](08-ftp.md).
