<!-- translated from zh-TW at commit 968641f -->

# 7. Referensi Pengaturan

**Pengaturan** diorganisasikan ke dalam lima kategori. Opsi yang tidak tersedia pada tingkat Gratis disembunyikan. Punya saran atau berpikir bahwa nilai default harus diubah? Beri tahu kami melalui [Laporkan Masalah](12-report.md).

## Penerimaan & Pemberitahuan

### Penerimaan
| Pengaturan | Opsi | Default | Detail |
|---|---|---|---|
| Tipe file yang diterima | Semua file / Hanya JPG / JPG + RAW / Foto + video / Kustom; plus Simpan JPEG saja dari RAW, Simpan JPEG terkompresi, Ganti salinan terkompresi saat file asli tiba (Pro) | Semua file | Lihat [Bab 3](03-receive.md#tipe-file-yang-diterima) |
| Folder penyimpanan | Berdasarkan kamera / Berdasarkan tanggal / Berdasarkan kamera dan tanggal / Berdasarkan tipe file | Berdasarkan kamera dan tanggal | Struktur subfolder di bawah `Pictures/AeroCam` dan `Movies/AeroCam` |
| Penamaan file | Nama kamera asli / Awalan tanggal / Awalan tanggal & waktu | Nama kamera asli | Berlaku untuk file masa depan saja; deteksi duplikat masih menggunakan nama kamera asli |
| Mode penerimaan (Pro) | Berkelanjutan / File tunggal | Berkelanjutan | File tunggal berhenti setelah menerima satu file |
| Lewati video besar (Pro) | Ukuran dalam MB | 1024 MB | Video yang lebih besar dicatat sebagai «Disaring» untuk unduhan manual |
| Batas waktu pencarian Wi‑Fi | 30 dtk / 1 / 2 / 3 / 5 / 10 mnt / Tidak terbatas | 3 mnt | Menghentikan penerimaan otomatis setelah batas waktu sehingga tidak terus mencoba dan menguras baterai |
| Penghentian otomatis menganggur FTP | Tidak pernah / 5 / 10 / 30 mnt | Tidak pernah | Menghitung dari foto terakhir yang diterima; tidak pernah berhenti di tengah transfer |
| Foto yang sudah diterima melalui Bluetooth | Ganti dengan aslinya saat diterima melalui Wi‑Fi / Jangan unduh lagi melalui Wi‑Fi / Simpan kedua salinan | Ganti dengan aslinya | Bluetooth menerima salinan yang lebih kecil sekitar 2 MB |

### Lokasi Foto
| Pengaturan | Default | Detail |
|---|---|---|
| Kirim lokasi ke kamera (Bluetooth) | Aktif | Mengirim GPS ponsel ke kamera pada saat dinyalakan atau transfer Bluetooth sehingga kamera menyematkannya |
| Tambahkan lokasi ke JPEG yang diterima (ponsel) | Nonaktif (bertanya saat penerimaan pertama) | Menyematkan lokasi ponsel berdasarkan waktu pengambilan ke JPEG yang diterima melalui Wi‑Fi, USB, atau FTP; file RAW tidak tersentuh |

Lihat [Bab 3 Lokasi Foto](03-receive.md#lokasi-foto-gps) untuk detailnya.

### Galeri
| Pengaturan | Opsi | Default | Detail |
|---|---|---|---|
| Kualitas JPEG terkompresi (Pro) | 60 / 70 / 80 / 90% | 80% | Kualitas untuk JPEG yang dikompresi ulang di ponsel Anda (~3–4 MB pada 24 MP) |
| Pilihan setelah unduh/hapus | Tanya setiap saat / Selalu simpan / Selalu bersihkan | Tanya setiap saat | Membantu mencegah secara tidak sengaja mengetuk «Hapus dari kamera» |
| Hitung mundur prompt | 3 / 5 / 8 / 10 dtk | 5 dtk | Membersihkan pilihan secara otomatis jika tidak dijawab saat «Tanya setiap saat» dipilih |
| Penghentian otomatis berbagi kode QR | 15 / 30 / 60 mnt | 30 mnt | Tautan kedaluwarsa secara otomatis setelah durasi ini |

### Pemberitahuan
| Pengaturan | Default | Detail |
|---|---|---|
| Jangan Ganggu | Nonaktif | Membisukan semua pemberitahuan AeroCam (pemberitahuan «Menerima» yang sedang berjalan tetap ada sebagaimana diwajibkan oleh Android) |
| Transfer dimulai | Nonaktif | |
| Foto diterima | Aktif | |
| Masalah transfer | Aktif | Transfer macet, dibatalkan oleh kamera, atau penyimpanan ponsel sedikit |
| Sembunyikan pemberitahuan yang sedang berjalan | — | Membuka pengaturan pemberitahuan Android sehingga Anda dapat menyembunyikannya sambil tetap menjaga penerimaan berjalan |
| Peringatan baterai kamera lemah | Aktif, 15% | Opsi ambang batas: 10 / 15 / 20 / 30%; diperiksa saat terhubung ke kamera |

## Pemotretan

### Tujuan Penyimpanan
| Pengaturan | Opsi | Detail |
|---|---|---|
| Tujuan penyimpanan | Kartu memori / Kartu + ponsel (Pro) | Digunakan saat kartu memori dimasukkan; beralih secara otomatis ke Ponsel saja saat tidak ada kartu yang dimasukkan (Pro). Menunjukkan status kartu saat ini saat terhubung. Lihat [Bab 3](03-receive.md#tujuan-penyimpanan-dan-pemotretan-tanpa-kartu) |

### Pemotretan Jarak Jauh
| Pengaturan | Opsi | Default | Detail |
|---|---|---|---|
| Diaktifkan secara default di Jarak Jauh | Fokus sebelum memotret, Histogram, Peringatan pencahayaan berlebih, Fokus peaking, Pengukur pencahayaan | Fokus sebelum memotret, Pengukur pencahayaan | Masih dapat dialihkan kapan saja saat memotret |
| Warna pengukur pencahayaan | Otomatis / Putih / Hitam | Otomatis | Otomatis beradaptasi dengan kecerahan latar belakang |
| Warna fokus peaking | Merah / Kuning / Biru / Putih | Merah | Ubah warna saat memotret subjek merah |
| Tetap nyalakan layar selama Jarak Jauh | Aktif / Nonaktif | Aktif | Mencegah tidur layar selama pemotretan interval atau eksposur panjang |
| Mode tangan kiri | Aktif / Nonaktif | Nonaktif | Memindahkan tombol rana ke kiri bawah dalam lanskap |

### Koneksi Kabel (USB‑C)
| Pengaturan | Opsi | Default | Detail |
|---|---|---|---|
| Kecepatan bingkai tampilan langsung USB | 30 / 60 fps / Tidak terbatas | 30 fps | 30 fps menghemat baterai dan berjalan lebih dingin; 60 fps lebih halus |
| Tampilan langsung USB resolusi tinggi | Aktif / Nonaktif | Aktif | Pratinjau yang lebih tajam dengan fps sedikit lebih rendah; kembali secara otomatis jika tidak didukung |
| Mulai otomatis menerima saat kabel USB dicolokkan (Pro) | Aktif / Nonaktif | Aktif | Memulai penerimaan USB saat dicolokkan |
| Sinkronkan jam kamera saat terhubung | Aktif / Nonaktif | Aktif | Menyesuaikan hanya jika meleset >2 dtk; bertanya terlebih dahulu jika meleset >1 hari |
| Tetap bangunkan kamera melalui USB | Aktif / Nonaktif | Aktif | Mengirim sinyal tetap hidup kecil setiap 10 dtk; berhenti setelah 30 mnt menganggur atau baterai lemah |

## Tampilan dan Bahasa
| Pengaturan | Opsi | Default |
|---|---|---|
| Tema | Ikuti sistem / Terang / Gelap / Malam (cahaya merah) | Ikuti sistem |
| Kecerahan layar aplikasi minimum | Aktif / Nonaktif (dalam mode Malam) | Nonaktif |
| Bahasa | Ikuti sistem / 繁中 / 简中 / 日本語 / English / 한국어 / Deutsch / Français / Español / Tiếng Việt / ไทย / Bahasa Indonesia | Ikuti sistem |

## Penyimpanan & Baterai
| Item | Detail |
|---|---|
| Singgahan gambar mini (Thumbnail cache) | Menunjukkan ukuran cache dengan tombol hapus (dibuat ulang dari kamera sesuai kebutuhan) |
| File temp unduhan tidak lengkap | Menunjukkan ukuran dengan tombol hapus |
| Pindai ulang foto ponsel | Menemukan foto yang dipulihkan ke ponsel Anda (misalnya, dari Sampah atau disimpan sebelum menginstal ulang) |
| Pengoptimalan baterai | Disarankan untuk dinonaktifkan (menunjukkan «Tidak dioptimalkan ✓») sehingga transfer latar belakang tidak dimatikan |

## Dukungan
| Item | Detail |
|---|---|
| Salin info diagnostik | Tempel saat melaporkan masalah: versi aplikasi, status ponsel & jaringan, kemampuan kamera, log perintah terbaru, danjejak kerusakan terakhir. Hanya 4 digit terakhir nomor seri kamera yang disertakan |
| Bersihkan log | Menghapus log sesi saat ini dan sebelumnya serta catatan kerusakan |
| Periksa pembaruan | Memeriksa versi baru secara manual; menunjukkan versi saat ini di bawah |
| Kunci uji | «Dapatkan kunci gratis» membuka AeroCam-Releases; «Masukkan kunci uji» memungkinkan Anda menempelkannya; menunjukkan tingkat dan tanggal kedaluwarsa saat ini |
| Lisensi sumber terbuka | Pustaka pihak ketiga yang digunakan (seperti LibRaw untuk pengembangan RAW) |
| Kirim statistik penggunaan anonim | Sakelar tunggal, aktif secara default. Lihat [Privasi dan Statistik Anonim](10-privacy.md) |
