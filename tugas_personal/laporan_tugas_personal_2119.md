# Laporan Tugas Personal Blockchain Level 1–5

- **Nama:** REZA TRI FEBRIANSYAH
- **NIM (4 digit terakhir):** 2119
- **Dibuat:** 2026-11-14 02:08  (waktu proses 1.9 detik)
- **Kode verifikasi:** `E4615DC90249`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 1 — Hash data pribadi

| Hasil | Nilai |
|---|---|
| SHA-256 nama | `320a2ea8c06391a32c41c8f25afc089766777933167c590b1f51d642b2979e02` |
| hash_dict profil | `da4764c9b1da99f2835ef4d710bf7234e945ef3a9b11a3acb087a14ca6c3334f` |
| hash_dict profil (urutan key dibalik) | `da4764c9b1da99f2835ef4d710bf7234e945ef3a9b11a3acb087a14ca6c3334f` |
| Bit berubah: tanggal lahir vs tanggal lahir + 1 hari | 53.12% |
| ID mahasiswa (Modifikasi 1) | `00237404` |

## Level 2 — Blockchain personal

- Proof genesis: **2119** (dari NIM)
- Proof blok 2, 3, 4: **97048, 21202, 24849**
- Pemilik setiap blok: `00237404`
- Rantai valid: True

## Level 3 — Pemalsuan data pribadi

- Posisi yang dipalsukan: **4**
- Data asli: `REZA TRI FEBRIANSYAH NIM akhir 2119`
- Data palsu: `REZA TRI FEBRIANSYAH NIM akhir 2119 (DIPALSUKAN)`
- Valid sebelum dipalsukan: True
- Tautan putus di indeks: **None**
- Valid setelah dipalsukan: **True**
- Valid setelah disambung ulang: **True**

## Level 4 — Transaksi dari data pribadi

| Blok | Pengirim | Penerima | Jumlah |
|---|---|---|---|
| 2 | REZA TRI FEBRIANSYAH | TEMAN_A | 10 |
| 2 | TEMAN_A | REZA TRI FEBRIANSYAH | 2 |
| 3 | REZA TRI FEBRIANSYAH | DOSEN | 20 |

- Ringkasan saldo (Modifikasi 4): masuk **2**, keluar **30**, bersih **-28**
- Kirim ke diri sendiri ditolak: True
- Amount 0 ditolak: True

## Level 5 — Proof of Work dengan nonce (deterministik)

| Blok | Nonce | Hash |
|---|---|---|
| 0 | 121266 | `00003db34ef90268a1fde81c…` |
| 1 | 77503 | `0000f8a8b0558612f4265b64…` |
| 2 | 67888 | `00008b87ef7d378bc348d829…` |
| 3 | 25759 | `00007a9a8a12f5ffdc094eb9…` |

- Valid: True → setelah blok 1 dipalsukan: **False**
- Percobaan hash untuk menambang ulang blok 1–3: **187.576**
- Valid setelah ditambang ulang: True

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 1.** Bandingkan SHA-256 nama Anda dengan milik seorang teman. Apakah ada pola yang mirip? Jelaskan juga mengapa dua hash profil Anda sama, dan mengapa hanya menambah 1 hari pada tanggal lahir mengubah 53.12% bit.

   _Jawaban:_
   - **Perbandingan dengan milik teman:** Nilai SHA-256 nama saya (`320a2ea8c06391a32c41c8f25afc089766777933167c590b1f51d642b2979e02`) sama sekali tidak menunjukkan pola kemiripan visual dengan nilai hash nama teman saya. Fungsi SHA-256 memetakan input teks ke ruang output secara merata (*pseudorandom uniform distribution*), sehingga kemiripan susunan huruf awal pada nama tidak memberikan korelasi apa pun terhadap hasil heksadesimalnya.
   - **Dua hash profil bernilai sama:** Nilai hash profil asli dan profil dengan urutan kunci terbalik bernilai identik (`da4764c9b1da...`) karena implementasi fungsi `hash_dict` menerapkan serialisasi kanonik menggunakan `json.dumps(data, sort_keys=True)`. Sebelum dilakukan proses hashing, semua kunci dalam dictionary diurutkan secara alfabetis terlebih dahulu, sehingga variasi urutan penulisan field dalam dictionary di memori tidak memengaruhi string JSON yang dihasilkan.
   - **Perubahan 1 hari mengubah 53.12% bit:** Fenomena ini merupakan karakteristik mendasar fungsi hash kriptografis yang disebut *Avalanche Effect* (efek longsoran salju). Mengubah hanya satu digit pada tanggal lahir (selisih 1 hari) merombak keadaan internal pada setiap putaran (*round*) kompresi SHA-256, menghasilkan pembalikan bit acak sebanyak 53.12% (136 dari 256 bit), yang sangat konsisten dengan probabilitas teoretis 50%.

2. **Level 2.** Kode Anda dan teman sama persis, tetapi proof Anda (97048, 21202, 24849) berbeda. Jelaskan penyebabnya.

   _Jawaban:_
   - Perbedaan ini terjadi karena **proof blok genesis** diinisialisasi secara personal menggunakan 4 digit terakhir NIM masing-masing (`int(nim4)`). Pada blockchain saya, proof genesis bernilai `2119` (dari NIM 202355202119), sedangkan teman-teman lain memiliki nilai awal yang berbeda.
   - Pada mekanisme Proof of Work Level 2, pencarian angka pembuktian kerja baru dihitung berdasarkan relasi `proof**2 - previous_proof**2`. Karena blok ke-2 menggunakan `previous_proof = 2119`, nilai `proof` yang menghasilkan hash valid dengan awalan nol sesuai difficulty adalah `97048`.
   - Selanjutnya, blok ke-3 menjadikan `97048` sebagai input dan menghasilkan `21202`, kemudian blok ke-4 menghasilkan `24849`. Akibat perbedaan benih awal (*seed*) pada genesis, seluruh rantai nilai proof berikutnya menjadi unik dan berbeda untuk setiap mahasiswa.

3. **Level 3.** Anda memalsukan posisi 4 dan tidak ada tautan putus yang terdeteksi (None), sedangkan valid setelah dipalsukan = True. Jelaskan hasil ini, lalu bandingkan dengan teman yang posisi pemalsuannya berbeda.

   _Jawaban:_
   - **Penyebab Tidak Ada Tautan Putus (None) dan Valid = True:**
     Posisi pemalsuan dihitung dari formula `1 + int(nim4) % 4`. Untuk NIM `2119`, `2119 % 4 = 3`, sehingga posisi yang dipalsukan adalah indeks `1 + 3 = 4`. Blok indeks 4 adalah **blok terakhir** di dalam rantai (panjang rantai adalah 5 blok, dari indeks 0 sampai 4). Fungsi `cari_tautan_putus` bekerja dengan memeriksa apakah pointer `previous_hash` pada blok $i$ cocok dengan hash blok $i-1$. Karena blok 4 adalah ujung rantai dan tidak memiliki blok penerus ($i=5$) yang menyimpan pointer ke arahnya, maka tidak ada pointer `previous_hash` yang rusak. Oleh karena itu, pemeriksaan integritas tautan antarblok mengembalikan `None` dan status validitas struktural tetap `True`.
   - **Perbandingan dengan Teman:**
     Teman-teman yang memalsukan data pada blok perantara (posisi 1, 2, atau 3) langsung mendeteksi kerusakan tautan pada blok penerusnya ($k+1$) dan status validitas rantai mereka langsung menjadi `False`. Kasus pada data saya ini mengungkap **kelemahan penting validasi tautan sederhana**: memvalidasi rantai hanya dengan mengecek pointer blok penerus tidak cukup untuk melindungi blok paling ujung jika isi datanya diubah.

4. **Level 4.** Jelaskan dari mana angka masuk 2, keluar 30, dan bersih -28 berasal. Mengapa transaksi ke diri sendiri perlu ditolak?

   _Jawaban:_
   - **Asal Usul Angka Saldo:**
     1. Transaksi 1: `REZA TRI FEBRIANSYAH` mengirim ke `TEMAN_A` sebesar tanggal lahir saya (10 Februari), yaitu **10** koin $\rightarrow$ keluar 10 koin.
     2. Transaksi 2: `TEMAN_A` mengirim ke `REZA TRI FEBRIANSYAH` sebesar bulan lahir saya (bulan 2 / Februari), yaitu **2** koin $\rightarrow$ masuk 2 koin.
     3. Transaksi 3: `REZA TRI FEBRIANSYAH` mengirim ke `DOSEN` sebesar `(int(nim4) % 50) + 1` = `(2119 % 50) + 1` = `19 + 1` = **20** koin $\rightarrow$ keluar 20 koin.
     - **Total Masuk:** 2 koin.
     - **Total Keluar:** $10 + 20 = 30$ koin.
     - **Saldo Bersih:** $2 - 30 = -28$ koin.
   - **Alasan Transaksi ke Diri Sendiri Harus Ditolak:**
     1. *Mencegah Pemborosan Block Space:* Transaksi ke diri sendiri tidak mengubah status kekayaan atau kepemilikan aset, namun tetap membebani ukuran blok dan kapasitas penyimpanan node jaringan.
     2. *Mencegah Manipulasi Transaksi (Wash Trading):* Mencegah upaya menciptakan ilusi aktivitas perdagangan atau likuiditas palsu di jaringan.
     3. *Optimalisasi Kinerja Validator:* Menghemat beban komputasi validator jaringan dari memproses transaksi nir-manfaat.

5. **Level 5.** Penyerang butuh 187.576 percobaan hash untuk memalsukan rantai Anda. Mengapa nonce Anda selalu sama setiap kali program dijalankan, padahal di demo Level 5 asli nonce berubah-ubah?

   _Jawaban:_
   - Pada simulasi Modifikasi 5, penambangan Proof of Work dijalankan secara **deterministik**: pencarian dimulai dari angka tetap `nonce = 0` dan bertambah secara sekuensial (`nonce += 1`). Karena seluruh data blok (indeks, transaksi, previous_hash, dan timestamp yang diseragamkan) bernilai tetap di setiap pengujian, fungsi SHA-256 yang bersifat deterministik murni akan selalu menemukan kombinasi hash yang memenuhi awalan `'0000'` pada angka nonce yang persis sama di setiap penjalanan.
   - Pada demo Level 5 asli, timestamp diambil dari jam riil sistem secara dinamis (`time.time()`), sehingga detik dan fraksi mikrodetik selalu berubah di setiap run, menyebabkan hash blok berubah dan angka nonce yang ditemukan selalu bervariasi.

6. **Etika data.** Anda baru saja menyimpan nama dan tanggal lahir di dalam blockchain. Jika ini blockchain publik, apa risikonya? Kaitkan dengan sifat immutability dan UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, terutama hak untuk menghapus data.

   _Jawaban:_
   - **Risiko Privasi:**
     Blockchain publik dapat diakses dan diinspeksi oleh siapa saja secara global. Menyimpan Personally Identifiable Information (PII) seperti nama lengkap, NIM, dan tanggal lahir secara terbuka membuka celah eksploitasi pencurian identitas, profiling data tanpa izin, dan kejahatan siber berbasis rekayasa sosial.
   - **Benturan dengan UU PDP No. 27 Tahun 2022:**
     Sifat *immutability* (data permanen dan tidak dapat dihapus/diubah) bertentangan langsung dengan Pasal 43 UU PDP yang memberikan hak kepada pemilik data untuk meminta penghapusan atau pemusnahan data pribadi miliknya (*Right to Erasure / Right to be Forgotten*). Sekali data pribadi masuk ke blok yang tertambang, data tersebut secara teknis tidak mungkin dihapus tanpa merusak seluruh integritas blockchain.
   - **Solusi Rekayasa:**
     Data sensitif harus disimpan di luar rantai (*off-chain*) dalam media penyimpanan terenkripsi, sementara blockchain hanya digunakan untuk menyimpan bukti kriptografis berupa nilai hash atau komitmen identitas.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "profil": {
    "nama": "REZA TRI FEBRIANSYAH",
    "nim4": "2119",
    "tanggal_lahir": "2005-02-10",
    "kota_asal": "Sorong",
    "hobi": "Mancing"
  },
  "level1": {
    "hash_nama": "320a2ea8c06391a32c41c8f25afc089766777933167c590b1f51d642b2979e02",
    "hash_profil": "da4764c9b1da99f2835ef4d710bf7234e945ef3a9b11a3acb087a14ca6c3334f",
    "hash_profil_urutan_terbalik": "da4764c9b1da99f2835ef4d710bf7234e945ef3a9b11a3acb087a14ca6c3334f",
    "avalanche_tanggal_persen": 53.12,
    "id_mahasiswa": "00237404"
  },
  "level2": {
    "proof_genesis": 2119,
    "proof_blok": [
      97048,
      21202,
      24849
    ],
    "pemilik_semua_blok": [
      "00237404"
    ],
    "valid": true
  },
  "level3": {
    "posisi_dipalsukan": 4,
    "data_asli": "REZA TRI FEBRIANSYAH NIM akhir 2119",
    "data_palsu": "REZA TRI FEBRIANSYAH NIM akhir 2119 (DIPALSUKAN)",
    "valid_asli": true,
    "tautan_putus_di": null,
    "valid_setelah_dipalsukan": true,
    "valid_setelah_disambung_ulang": true
  },
  "level4": {
    "riwayat": [
      [
        2,
        {
          "sender": "REZA TRI FEBRIANSYAH",
          "recipient": "TEMAN_A",
          "amount": 10
        }
      ],
      [
        2,
        {
          "sender": "TEMAN_A",
          "recipient": "REZA TRI FEBRIANSYAH",
          "amount": 2
        }
      ],
      [
        3,
        {
          "sender": "REZA TRI FEBRIANSYAH",
          "recipient": "DOSEN",
          "amount": 20
        }
      ]
    ],
    "ringkasan_saldo": {
      "masuk": 2,
      "keluar": 30,
      "bersih": -28
    },
    "kirim_ke_diri_sendiri_ditolak": true,
    "amount_nol_ditolak": true,
    "jumlah_blok": 3
  },
  "level5": {
    "nonce": [
      121266,
      77503,
      67888,
      25759
    ],
    "hash": [
      "00003db34ef90268a1fde81c1be0cdcf041a74ce9c51aeddd1f4d475fb0fc890",
      "0000f8a8b0558612f4265b64d3337c6ca62966edf6beff7635c0903c80706eaf",
      "00008b87ef7d378bc348d8292d9d96150142988458b4388bdd889462e5d79a72",
      "00007a9a8a12f5ffdc094eb9b8a0280c3993fd9a37a96288635b3e518f8af552"
    ],
    "valid": true,
    "valid_setelah_dipalsukan": false,
    "percobaan_tambang_ulang": 187576,
    "valid_setelah_tambang_ulang": true
  },
  "kode_verifikasi": "E4615DC90249"
}
```
