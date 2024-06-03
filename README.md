Proyek ini memanfaatkan YOLOv8n-seg untuk melakukan deteksi objek dan segmentasi instance pada file video. Proyek ini membaca video, memproses setiap frame untuk mendeteksi dan melacak objek, lalu menghasilkan video dengan segmentasi yang dianotasi.

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk implementasi.
- **OpenCV**: Perpustakaan untuk pemrosesan gambar dan video.
- **Ultralytics YOLO**: Perpustakaan yang menyediakan implementasi YOLO (You Only Look Once) untuk deteksi objek.
- **collections**: Modul Python yang menyediakan tipe data kontainer khusus seperti `defaultdict`.

## Instalasi

Untuk menjalankan proyek ini, pastikan Anda telah menginstal pustaka-pustaka berikut:

```bash
pip install opencv-python-headless ultralytics
```
Langkah-langkah Penggunaan
1. Clone repositori

```bash
git clone https://github.com/yourusername/instance-segmentation-object-tracking.git
cd instance-segmentation-object-tracking
```

2. Letakkan file video input Anda di direktori proyek dan beri nama mobil.mp4 atau ubah skrip untuk menggunakan file video yang Anda inginkan.
3. Jalankan skrip

```bash
python main.py
```

## Referensi
## Dokumentasi Ultralytics YOLO
## Dokumentasi OpenCV
