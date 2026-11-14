<!-- translated from zh-TW at commit 968641f -->

# 6. Pengeditan Foto dan Gaya

## Editor Foto (Gratis)
Buka foto apa saja di **Foto ponsel** lalu ketuk **Edit**. Ada tiga tab di bagian bawah: **Potong**, **Sesuaikan**, dan **.np3**.

📷 Tangkapan layar: Editor foto (Potong, Sesuaikan, .np3)

### Potong
- Rasio aspek: Asli, Bebas, 1:1, 4:5, 3:2, 16:9, ditambah rasio sinema 1.66, 1.85, 2, 2.20, dan 2.39. Foto vertikal secara otomatis menggunakan orientasi potret.
- Seret di dalam bingkai untuk memindahkan; seret sudut mana saja untuk mengubah ukuran.
- Luruskan ±45° dan putar 90° berlawanan arah jarum jam (`↺`).

### Sesuaikan
Pilih alat dari baris untuk menyesuaikan dengan dial penggaris presisi, lalu ketuk **Selesai** untuk kembali (alat yang disesuaikan menunjukkan titik kecil):
- **Cahaya**: Pencahayaan, Kontras, Highlight, Bayangan, Putih, Hitam.
- **Warna**: Suhu, Warna (Tint), Saturasi, Vibrance.
- **Detail**: Kejernihan, Ketajaman, Vignette.

Dial penggaris: Menempel ke langkah bulat (0,1 EV untuk Pencahayaan, 1° untuk Luruskan, 1 untuk yang lain) dengan ketukan haptik halus. Tekan dan tahan salah satu ujung untuk melangkah terus menerus, ketuk nomor untuk mengetik nilai secara langsung, atau ketuk dua kali / ketuk `↺` untuk mengatur ulang ke nol.

### Kontrol Umum
- **↶ ↷** Urungkan / Ulangi.
- Tekan dan tahan **Asli** untuk mengintip sebelum pengeditan Anda.
- **◧ Bandingkan**: Penggeser layar terpisah yang membandingkan versi asli dan yang diedit; cubit untuk memperbesar tetap sinkron di kedua sisi.
- Ketuk **Histogram** di kanan langsung untuk memperluas histogram langsung.

### Menyimpan
- File asli kamera (masih di kartu memori Anda): **Menyimpan menggantikan salinan di ponsel Anda.** AeroCam menyimpan cadangan file asli selama 7 hari dengan opsi «Pulihkan asli» di penampil. Jika kamera tidak terhubung, aplikasi menanyakan apakah akan «Ganti» atau «Simpan sebagai salinan».
- Foto khusus ponsel (tangkapan tanpa kartu, panorama, gabungan Shake) selalu disimpan sebagai salinan baru yang berakhiran `_E`.
- Mempertahankan metadata EXIF pada kualitas JPEG 95. Jika penyimpanan terganggu, AeroCam menyelesaikannya secara otomatis saat Anda membuka aplikasi berikutnya.
- Filter berdasarkan **Dieedit** di Foto ponsel untuk menemukan gambar yang diedit (ditandai dengan `✎` kecil di kiri bawah).
- Mengedit salinan terkompresi (`JPEG.S`) mengingatkan Anda untuk mengedit file asli kamera sebagai gantinya untuk kualitas yang lebih baik.
- Video tidak dapat diedit.

---

## Edit RAW di Ponsel (Eksperimental)
File NEF terbuka di editor yang sama persis dan disimpan di sampingnya sebagai `DSC_xxxx_E.JPG` (penyimpanan berikutnya memperbarui file tersebut). **File RAW asli tidak pernah dimodifikasi**, dan metadata EXIF dipertahankan.
- **NEF terkompresi tanpa kehilangan (Lossless compressed)**: Dikembangkan langsung di ponsel Anda menggunakan white balance kamera.
- **NEF Efisiensi tinggi / Efisiensi tinggi★ (High efficiency / High efficiency★)**: Kompresi berpemilik ini tidak dapat didekode di ponsel, jadi AeroCam mengedit JPEG ukuran penuh yang disematkan di dalam NEF sebagai gantinya. Bar atas menampilkan «JPEG tersemat 8 bit» dan «Gaya kamera diterapkan: xxx».
- File dengan hanya pratinjau kecil dan tanpa JPEG ukuran penuh tidak dapat diedit (aplikasi menjelaskan alasannya).

### RAW yang Dapat Diedit di Ponsel (Alihkan Kompresi RAW Kamera)
Untuk membuat pemotretan NEF di masa mendatang dapat dikembangkan langsung di ponsel Anda, Anda dapat mengalihkan kamera Anda ke «Kompresi lossless» langsung dari AeroCam:
- Akses melalui «Ambil RAW lossless lain waktu» pada spanduk Efisiensi Tinggi editor, atau ketuk lencana kualitas gambar di kanan atas kartu Kartu memori di Beranda (aktif kapan pun kamera diatur untuk memotret RAW).
- Selalu meminta konfirmasi terlebih dahulu, menulis ke kamera, membaca kembali untuk memverifikasi, dan menunjukkan perubahan pada sisa jepretan (file lossless lebih besar, sehingga jumlah yang tersisa turun sedikit).
- AeroCam mengingat pengaturan kamera Anda sebelumnya sehingga Anda dapat memulihkannya nanti, dan tidak akan menimpanya jika Anda sudah mengubahnya di kamera.

---

## Pratinjau Gaya .np3 (Gratis)
Di bawah tab **.np3** di editor, terapkan file Nikon Picture Control (`.np3`, `.ncp`) untuk mempratinjau tampilannya di ponsel Anda.
- Ketuk gaya apa saja untuk menerapkannya, sesuaikan kekuatan dari 0–100%, dan sesuaikan lebih lanjut di **Sesuaikan**.
- Geser ke kiri/kanan pada foto untuk memutar gaya, atau tekan dan tahan untuk melihat file asli. Filter cepat untuk `★` Favorit dan Terbaru muncul di bawah.
- Ketuk **Semua N ▴** untuk memperluas pustaka Gaya lengkap (lihat di bawah) dengan pencarian dan filter.
- Mensimulasikan kurva dan saturasi: file dengan kurva kustom menggunakan kurva tersematnya, sementara file yang dibangun dengan penggeser Flexible Color («Tono penggeser») dikonversi ke kurva berdasarkan pengukuran NX Studio. **Color Blender dan Color Grading belum disimulasikan**, sehingga hasilnya adalah perkiraan.
- Berfungsi paling baik pada file NEF. Jika JPEG sudah memiliki Picture Control yang disematkan saat penangkapan, efeknya bertumpuk (aplikasi memperingatkan Anda).

📷 Tangkapan layar: Tab .np3 di editor

---

## Gaya Kamera C1–C9 (Pro)
Kelola slot Picture Control kustom C1–C9 pada kamera Anda dari ponsel Anda. Ketuk kartu **Gaya kamera** di Beranda (memerlukan koneksi Wi‑Fi atau USB).
- Setiap slot menunjukkan pratinjau, nama, dan lencana untuk status aktif, kurva kustom, atau Flexible Color.
- **Ketuk slot** untuk memilih gaya dari pustaka Anda dan menulisnya ke kamera. AeroCam membacanya kembali untuk memverifikasi dan menunjukkan `✓` hanya saat cocok. **Tekan lama** atau ketuk `⋮` untuk mengosongkan slot. Jika foto sedang ditransfer, penulisan menunggu hingga file tersebut selesai.
- Kamera hanya dikueri saat Anda membuka layar ini, ketuk `↻`, tulis, atau bersihkan; Beranda menunjukkan nilai terakhir dibaca dan stempel waktu.
- Di bawah C1–C9, 9 resep Nikon Imaging Cloud dicantumkan hanya-baca (tambahkan melalui Nikon Imaging Cloud).

### Apa yang Ditulis ke Kamera
Slot kamera kustom menerima **Picture Control dasar + penggeser penyesuaian**, bukan file `.np3` mentah:
- Ketuk **＋ Gaya baru** di pustaka untuk memilih dasar (Standard, Flat, Creative Picture Control…) dan atur Ketajaman, Kejernihan, Kontras, Kecerahan, Saturasi, dan Rona (Hue).
- **Menulis `.np3` / `.ncp` ke kamera (perkiraan)**: File dengan kurva — serta file «Tono penggeser» yang dikonversi ke kurva — menulis **Nama + Kurva + Penajaman (Ketajaman, Penajaman rentang menengah, Kejernihan)** ke dalam slot C menggunakan dasar yang Anda pilih. **Saturasi, Color Blender, dan Color Grading tidak dapat ditulis melalui koneksi**; AeroCam mencantumkan semua nilai dalam file dan secara jelas menandai apa yang tidak akan ditransfer sebelum menulis.
- Untuk kesetiaan penuh, salin `.np3` ke kartu memori dan impor melalui menu kamera.

### Pustaka Gaya
- Menampung hingga 256 gaya (`.np3` dan `.ncp`).
- Bilah pencarian `🔍`, chip filter (Semua, `★`, Terbaru, Dengan kurva, Di kamera, Dapat ditulis), dan **＋ Baru**.
- Setiap gaya menampilkan gambar mini pratinjau menggunakan foto referensi impor Anda sendiri (`＋ → «Pratinjau foto referensi…»`), atau bagan contoh warna hingga Anda mengimpornya.

📷 Tangkapan layar: Gaya kamera C1–C9 dan Pustaka gaya

---

## Pemrosesan Gambar: Penyambungan Panorama dan Penggabungan Pengurangan Derau (Pro)
Pilih beberapa foto di **Foto ponsel** dan **geser ke atas** bilah tindakan bawah (atau ketuk gagangnya) untuk membuka «Pemrosesan gambar».

### Stitch (Panorama)
- Memilih di dalam tumpukan «Panorama» menyambung bingkai sesuai dengan posisi kisi yang ditangkap dan menyimpan hasilnya kembali ke tumpukan tersebut yang diberi label «Panorama».
- Memilih foto yang tumpang tindih di galeri reguler memungkinkan AeroCam mendeteksi secara otomatis bagaimana mereka terhubung dan menyimpan hasilnya sebagai tumpukan baru.
- Foto yang tidak cocok tidak akan menggagalkan seluruh batch: AeroCam menyambung grup terhubung terbesar dan mencantumkan nama file yang dilewati. Panorama kisi memerlukan setiap ubin untuk hadir sehingga keluaran tidak memiliki lubang.
- Sapuan 360° penuh mengekspor panorama 360°. Hasil diratakan secara otomatis menggunakan data level kamera yang direkam, bebas hantu, dan mempertahankan metadata EXIF.
- Lihat [Bab 5 Panorama](05-remote.md#panorama-penyambungan) untuk instruksi pemotretan.

### Penggabungan Pengurangan Derau (Shake)
- Menyelaraskan dan merata-rata bingkai yang dipilih untuk mengurangi derau sambil mempertahankan detail; area bergerak menggunakan satu bingkai tunggal untuk menghindari bayangan.
- Memilih di dalam tumpukan «Shake» menyimpan hasil yang digabungkan kembali ke tumpukan tersebut (diberi label «Digabungkan»), atau Anda dapat mengetuk **Gabungkan** / **Gabungkan ulang** di atas tumpukan.
- Lihat [Bab 5 Shake](05-remote.md#shake-penggabungan-pengurangan-derau) untuk instruksi pemotretan.

> Hanya satu pekerjaan jahitan atau penggabungan yang berjalan dalam satu waktu. Kemajuan muncul di layar, dan Anda dapat mengetuk spanduk untuk membuka hasilnya saat selesai.
