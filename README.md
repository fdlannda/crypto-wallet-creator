# EVM Wallet Generator

EVM Wallet Generator adalah sebuah skrip Python untuk membuat wallet Ethereum Virtual Machine (EVM) secara otomatis. Wallet dapat dibuat menggunakan private key atau seed phrase, dan hasilnya dapat disimpan dalam file CSV.

---

## Fitur

- **Generate Wallet**:
  - Menggunakan **Private Key**
  - Menggunakan **Seed Phrase**
- **Simpan Wallet** ke file CSV.
- **Tampilkan Wallet** secara interaktif di terminal menggunakan Rich Table.

---

## Prasyarat

1. Python 3.x terinstal di komputer Anda.
2. Instalasi pustaka yang dibutuhkan:
   - `eth-account`
   - `rich`

Instal pustaka menggunakan perintah berikut:
```bash
pip install eth-account rich
```

---

## Cara Menggunakan

1. Jalankan skrip Python:
   ```bash
   python <nama_file_skrip>.py
   ```
2. Ikuti petunjuk di terminal untuk memilih metode pembuatan wallet:
   - Ketik **1** untuk membuat wallet dengan private key.
   - Ketik **2** untuk membuat wallet dengan seed phrase.
3. Masukkan jumlah wallet yang ingin dibuat.
4. Pilih apakah Anda ingin menyimpan hasilnya ke file CSV.
5. Jika ya, masukkan nama file yang diinginkan (contoh: `wallets.csv`).

---

## Struktur File CSV

File CSV yang dihasilkan akan memiliki kolom-kolom berikut:

### Jika menggunakan **Private Key**:
- **No**
- **Address** (Alamat Wallet)
- **Private Key**

### Jika menggunakan **Seed Phrase**:
- **No**
- **Address** (Alamat Wallet)
- **Seed Phrase**

---

## Contoh Output di Terminal

```plaintext
Selamat datang di EVM Wallet Generator!
Pilih metode pembuatan wallet:
[1] Dengan Private Key
[2] Dengan Seed Phrase
Masukkan pilihan Anda (1/2): 1
Masukkan jumlah wallet yang ingin dibuat: 3

+----+------------------------------------------+------------------------------------------+
| No | Address                                  | Private Key                              |
+----+------------------------------------------+------------------------------------------+
| 1  | 0x1234567890abcdef1234567890abcdef123456 | 0xabcdefabcdefabcdefabcdefabcdefabcdef |
| 2  | 0xabcdef1234567890abcdef1234567890abcdef | 0x123456123456123456123456123456123456 |
| 3  | 0xabcdefabcdefabcdefabcdefabcdefabcdef   | 0xabcdefabcdefabcdefabcdefabcdefabcdef |
+----+------------------------------------------+------------------------------------------+

Wallets berhasil disimpan ke file wallets.csv!
```

---

## Catatan Keamanan
- **Jangan bagikan file CSV** yang berisi private key atau seed phrase kepada orang lain.
- Pastikan file CSV disimpan di tempat yang aman.

---

## Lisensi
Proyek ini bersifat open-source dan berada di bawah lisensi [MIT License](https://opensource.org/licenses/MIT).
