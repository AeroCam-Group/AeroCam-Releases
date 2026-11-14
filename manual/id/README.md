<!-- translated from zh-TW at commit 968641f -->

# Panduan Pengguna AeroCam (Bahasa Indonesia)

> Sesuai dengan **Beta 92.04.08.10** (diperbarui 15-11-2026). Baris yang ditandai 📷 adalah tempat penampung untuk tangkapan layar yang akan ditambahkan nanti.

AeroCam mengirimkan foto dari kamera Anda langsung ke ponsel Android Anda. Anda juga dapat mengontrol kamera dari ponsel, mengedit foto di ponsel, dan menuliskan profil gaya ke dalam kamera. Saat ini **seri Nikon Z** didukung, dengan lebih banyak merek yang akan segera hadir.

AeroCam adalah aplikasi pihak ketiga yang dikembangkan secara independen, tidak berafiliasi dengan atau disetujui oleh Nikon atau produsen kamera lainnya.

## Daftar Isi

1. [Instalasi dan Memulai](01-install.md): instalasi, izin, tur layar, kunci uji, pembaruan, bahasa
2. [Menghubungkan Kamera Anda](02-connect.md): Bluetooth, Wi‑Fi (Koneksi satu ketukan / hotspot ponsel / Wi‑Fi yang sama), kabel USB, cara memilih, panduan koneksi
3. [Penerimaan Otomatis dan Penyimpanan](03-receive.md): mulai/jeda penerimaan, aturan penerimaan, folder dan nama file, pemotretan tanpa kartu, lokasi foto, dasbor kamera, riwayat
4. [Galeri](04-gallery.md): kartu memori kamera, foto ponsel, unduh dan hapus, peringkat bintang, cadangan kartu memori, berbagi kode QR
5. [Pemotretan Jarak Jauh dan Kontrol](05-remote.md): pemotretan jarak jauh Wi‑Fi/USB, metode pemotretan, alat bantu pemotretan, remote Bluetooth, monitor video, mode langit malam
6. [Pengeditan Foto dan Gaya](06-edit.md): editor, pratinjau gaya .np3, mengedit RAW di ponsel, gaya kamera C1–C9, penyambungan panorama, penggabungan pengurangan derau (Shake)
7. [Referensi Pengaturan](07-settings.md)
8. [Penerimaan FTP](08-ftp.md): kamera mengirim foto langsung ke ponsel secara otomatis setelah pemotretan
9. [Gratis / Pro / Cine](09-tiers.md)
10. [Privasi dan Statistik Anonim](10-privacy.md)
11. [FAQ dan Pemecahan Masalah](11-faq.md)
12. [Laporkan Masalah](12-report.md)

## Kamera yang Didukung

| Model | Penerimaan otomatis, galeri kamera | Pemotretan jarak jauh | Status |
|---|---|---|---|
| Z9, Z8, Z6III, Zf, Z5II, Z50II, ZR dan model lain dengan «Connection type» (Tipe koneksi) di menu | ✅ | ✅ | Telක්ෂdiuji pada Zf; laporan untuk model lain sangat disambut |
| Z6, Z7, Z6II, Z7II, Z5, Z50, Zfc, Z30 dan model sebelumnya | ✅ | ❌ (tidak didukung oleh protokol koneksi model-model ini) | Laporan disambut |
| Canon, Sony, Fujifilm | Segera hadir | Segera hadir | |

Jika Anda telah menguji AeroCam dengan model kamera lain, beri tahu kami fitur apa yang berfungsi dan yang tidak melalui [Laporan kamera](https://github.com/AeroCam-Group/AeroCam-Releases/issues/new/choose).

## Persyaratan
- Ponsel Android yang menjalankan Android 10 atau lebih baru.
- Kamera seri Nikon Z.

## Istilah yang Digunakan dalam Panduan Ini
| Istilah dalam Panduan | Arti |
|---|---|
| Galeri kamera / kartu memori kamera | Foto pada kartu memori kamera, ditelusuri dari ponsel Anda melalui koneksi |
| Foto ponsel / galeri ponsel | Foto yang sudah disimpan di ponsel Anda |
| RAW | File NEF Nikon |
| JPEG.S | JPEG terkompresi (JPEG yang diekstrak dari RAW, JPEG yang dikompresi ulang di ponsel, atau salinan kecil yang dikirim melalui Bluetooth), diakhiri dengan `_S.JPG` |
| Picture Control | Profil warna kamera seperti Standard atau Flat; profil kustom disimpan di C1–C9 |
| Pro / Cine | Tingkatan berbayar; selama versi Beta, masukkan kunci uji gratis untuk membuka semuanya — lihat [Bab 9](09-tiers.md) |
