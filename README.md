# Hack Simulation

Proyek ini mensimulasikan berbagai teknik hacking seperti cracking password, eksploitasi jaringan, dan pemindaian kerentanannya. Proyek ini dirancang sebagai alat edukasi untuk memahami konsep dasar dalam keamanan siber dan ethical hacking.

## Gambaran Umum Proyek

Proyek ini terdiri dari komponen-komponen berikut:

1. **Komponen Utama**:
   - `network.py`: Mensimulasikan pemindaian jaringan dan eksploitasi kerentanan.
   - `cracker.py`: Mensimulasikan cracking password menggunakan berbagai teknik.
   - `exploit.py`: Mensimulasikan eksploitasi celah keamanan di sistem target.

2. **Modul**:
   - `scanner.py`: Mensimulasikan pemindaian port terbuka dan kerentanan.
   - `brute_force.py`: Mengimplementasikan serangan brute-force untuk cracking password.
   - `keylogger.py`: Mensimulasikan keylogger untuk tujuan edukasi.

3. **Target**:
   - `server.py`: Mewakili server yang rentan dan dapat dieksploitasi.
   - `device.py`: Mewakili perangkat yang dapat menjadi sasaran serangan.

4. **Utilitas**:
   - `logger.py`: Mencatat kemajuan dan peristiwa selama simulasi.
   - `encryption.py`: Mensimulasikan operasi enkripsi dan dekripsi.
   - `config.py`: Menyimpan variabel konfigurasi untuk simulasi.

5. **Pengujian**:
   - Tersedia pengujian unit untuk memverifikasi fungsionalitas komponen utama.

## Instalasi

Untuk menjalankan proyek ini, Anda memerlukan Python 3.x terinstal di mesin Anda. Ikuti langkah-langkah berikut:

1. **Clone repositori**:

   ```bash
   git clone https://github.com/username/hack_simulation.git
   cd hack_simulation



## Hasil Output

```yaml
simulation_output:
  - timestamp: "2024-12-29T12:00:00"
    message: "Simulasi dimulai"
  
  - timestamp: "2024-12-29T12:01:05"
    message: "Pemindaian kerentanannya dimulai..."
  
  - timestamp: "2024-12-29T12:01:10"
    message: "Memindai 192.168.1.1 untuk kerentanannya..."
    vulnerabilities_found: 
      - "Kerentanan 1"
      - "Kerentanan 2"
  
  - timestamp: "2024-12-29T12:01:15"
    message: "Kerentanannya ditemukan, mulai eksploitasi..."
  
  - timestamp: "2024-12-29T12:01:20"
    message: "Mengeksploitasi Kerentanan 1 di 192.168.1.1"
    exploit_success: true
  
  - timestamp: "2024-12-29T12:02:00"
    message: "Serangan brute-force dimulai pada pengguna 'admin' menggunakan passwords.txt"
  
  - timestamp: "2024-12-29T12:02:30"
    message: "Mencoba password: 'password1'"
  
  - timestamp: "2024-12-29T12:02:40"
    message: "Mencoba password: '123456'"
  
  - timestamp: "2024-12-29T12:02:50"
    message: "Mencoba password: 'admin'"
    password_found: "admin"
  
  - timestamp: "2024-12-29T12:03:00"
    message: "Simulasi selesai dengan sukses."
