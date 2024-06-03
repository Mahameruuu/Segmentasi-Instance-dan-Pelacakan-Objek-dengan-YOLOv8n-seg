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
