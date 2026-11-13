# Laporan Tugas Personal 2 — Blockchain Level 6–9

- **Nama:** REZA TRI FEBRIANSYAH
- **NIM (4 digit terakhir):** 2119
- **Dibuat:** 2026-11-14 02:08  (waktu proses 0.0 detik)
- **Kode verifikasi:** `87162414C1CE`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 6 — Mining data pribadi dan jejak difficulty

Data yang ditambang: `REZA TRI FEBRIANSYAH|2119|2005-02-10`

| Difficulty | Nonce | Percobaan | Teori 16^d | Hash |
|---|---|---|---|---|
| 1 | 37 | 38 | 16 | `023cadeba0adc2f284e9…` |
| 2 | 253 | 254 | 256 | `00730b1ab680dbbf706a…` |
| 3 | 530 | 531 | 4.096 | `000cc96f9e530b309598…` |
| 4 | 5763 | 5.764 | 65.536 | `00009ef81434eafe7942…` |

- Difficulty awal (dari NIM): **4**, target waktu blok 10 detik
- Waktu blok simulasi (dari NIM + tanggal + bulan lahir): 8, 4, 4, 36, 4, 0, 0, 8 detik
- Jejak difficulty (Modifikasi 6): **4, 5, 6, 5, 6, 7, 8, 8**

## Level 7 — Kunci dan tanda tangan dari data pribadi

- Kunci publik (32 karakter awal): `e6e8cdc02d77ee15931a426863df1c8b…`
- Alamat Anda: `6da89cec12d6d93a5ff5828aa6e368c070b5d596`
- Transaksi: kirim **10** ke TEMAN_A
- Tanda tangan: `744d39f65aef052dd791b376d6bc9a322b00ca690124ef72…`
- Tanda tangan selalu sama saat diulang: True
- Transaksi sah: **True**; setelah amount diubah: **False**
- Penipu memakai alamat Anda: tanda tangannya valid dengan kuncinya = True, transaksinya sah = **False**

## Level 8 — Jaringan dan fork pribadi

- Jumlah node: **4**; blok pribadi tiap node: [3, 2, 2, 1]
- Panjang rantai saat fork: [5, 4, 4, 3]
- Setelah resolve_conflicts: [5, 5, 5, 5], sepakat = **True**
- Pemenang fork: **REZA-1**; blok terbuang (orphan): **5**
- Hash ujung rantai: `005f1f3870b201bad3c78e43…`

## Level 9 — Ekonomi dengan halving

- Hadiah awal: **39**, halving setiap **3** blok
- Hadiah blok 1–6 (Modifikasi 9): **39, 39, 39, 19, 19, 19**

| Alamat | Saldo |
|---|---|
| REZA TRI FEBRIANSYAH | 113.0 |
| TEMAN_A | 35.0 |
| TEMAN_B | 26.0 |

- Total suplai: **174.0**
- Belanja melebihi saldo ditolak: True
- Validasi ekonomi: **True**; setelah hadiah blok 1 dicurangi: **False**

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 6.** Bandingkan kolom Percobaan dengan Teori 16^d pada tabel Anda. Mengapa bisa berbeda jauh? Lalu jelaskan jejak difficulty Anda (4, 5, 6, 5, 6, 7, 8, 8): pada langkah mana difficulty naik, tetap, dan turun, dan mengapa?

   _Jawaban:_
   - **Perbandingan Percobaan vs Teori $16^d$:**
     Nilai Teori $16^d$ merupakan nilai harapan rata-rata matematis (*expected attempts*) dari proses Bernoulli berbasis fungsi hash SHA-256. Setiap digit heksadesimal memiliki 16 kemungkinan (0-f), sehingga peluang mendapatkan karakter '0' di depan adalah $(1/16)^d$. Pada penambangan blok tunggal secara individual, proses penemuan nonce adalah fenomena probabilistik murni:
     - Difficulty 1: Teori = 16, Percobaan = 38 (sedikit di atas rata-rata).
     - Difficulty 2: Teori = 256, Percobaan = 254 (sangat akurat mendekati ekspektasi teoretis 256).
     - Difficulty 3: Teori = 4.096, Percobaan = 531 (penambangan sangat beruntung, menemukan nonce valid jauh lebih cepat dari rata-rata).
     - Difficulty 4: Teori = 65.536, Percobaan = 5.764 (sangat cepat, hanya membutuhkan ~8.8% dari beban kerja rata-rata).
     Secara agregat, jika penambangan diulang dalam ribuan kali percobaan, nilai rata-rata empiris akan selalu konvergen menuju $16^d$.
   - **Jejak Difficulty (4, 5, 6, 5, 6, 7, 8, 8):**
     Aturan penyesuaian difficulty dengan target waktu blok 10 detik adalah:
     - Waktu aktual < 5 detik (target / 2) $\rightarrow$ Difficulty naik (+1) karena blok ditambang terlalu cepat.
     - Waktu aktual > 20 detik (target * 2) $\rightarrow$ Difficulty turun (-1) karena penambangan terlalu lambat.
     - Waktu aktual antara 5 hingga 20 detik $\rightarrow$ Difficulty tetap.
     Dengan deret waktu simulasi pribadi saya `[8, 4, 4, 36, 4, 0, 0, 8]` detik dan difficulty awal 4:
     1. Langkah 1 (waktu 8s): Di antara 5s dan 20s $\rightarrow$ **Tetap di 4**.
     2. Langkah 2 (waktu 4s): $4 < 5$s (terlalu cepat) $\rightarrow$ **Naik menjadi 5**.
     3. Langkah 3 (waktu 4s): $4 < 5$s (terlalu cepat) $\rightarrow$ **Naik menjadi 6**.
     4. Langkah 4 (waktu 36s): $36 > 20$s (terlalu lambat) $\rightarrow$ **Turun menjadi 5**.
     5. Langkah 5 (waktu 4s): $4 < 5$s (terlalu cepat) $\rightarrow$ **Naik menjadi 6**.
     6. Langkah 6 (waktu 0s): $0 < 5$s (terlalu cepat) $\rightarrow$ **Naik menjadi 7**.
     7. Langkah 7 (waktu 0s): $0 < 5$s (terlalu cepat) $\rightarrow$ **Naik menjadi 8**.
     8. Langkah 8 (waktu 8s): Di antara 5s dan 20s $\rightarrow$ **Tetap di 8**.

2. **Level 7.** Mengapa tanda tangan Anda selalu sama setiap kali program dijalankan, padahal di Level 7 asli berubah-ubah? Mengapa transaksi penipu tidak sah walaupun tanda tangannya valid?

   _Jawaban:_
   - **Mengapa Tanda Tangan Selalu Sama:**
     Pada implementasi ECDSA standar di Level 7 asli, algoritma menggunakan generator bilangan acak sistem untuk memilih nilai rahasia sementara (*ephemeral key* $k$). Hal ini membuat tanda tangan selalu menghasilkan pasangan $(r, s)$ yang berbeda di setiap penjalanan. Namun pada Modifikasi 7, digunakan standar **RFC 6979** melalui fungsi `sign_deterministic`. Standar ini menurunkan nilai $k$ secara deterministik dari HMAC hash pesan transaksi dan kunci privat. Karena kunci privat dan data transaksi saya selalu sama di setiap eksekusi, nilai $k$ dan hasil tanda tangan digital heksadesimalnya selalu identik 100%.
   - **Mengapa Transaksi Penipu Tidak Sah:**
     Tanda tangan penipu secara matematis valid terhadap kunci publiknya sendiri (`verifikasi == True`) karena penipu memang menandatangani transaksi tersebut menggunakan kunci privat miliknya. Namun, fungsi konsensus `transaksi_sah` menerapkan verifikasi kepemilikan alamat:
     `alamat_dari_kunci_publik(kunci_publik) == tx["sender"]`
     Penipu mencantumkan alamat saya di kolom `sender`, tetapi menggunakan kunci publik miliknya. Karena penurunan kunci publik penipu menghasilkan alamat penipu dan bukan alamat saya yang tertera pada `sender`, transaksi ditolak sebagai **TIDAK SAH** (`False`).

3. **Keamanan kunci.** Kunci privat Anda dibuat dari nama, NIM, dan tanggal lahir. Mengapa cara ini SANGAT BERBAHAYA di dunia nyata? Siapa saja yang bisa mencuri dana alamat Anda? (Cari tahu istilah *brain wallet*.)

   _Jawaban:_
   - **Bahaya Brain Wallet dan Entropi Rendah:**
     Pembuatan kunci privat dari teks atau informasi yang mudah ditebak dikenal sebagai **Brain Wallet**. Cara ini sangat berbahaya karena ruang pencarian (*keyspace*) dari data identitas pribadi memiliki entropi yang sangat rendah. Kunci privat kriptografi seharusnya memiliki entropi 256 bit murni ($2^{256}$ kemungkinan acak tak tertebak).
   - **Pihak yang Berpotensi Mencuri Dana:**
     1. Siapa pun yang mengetahui data pribadi mahasiswa (teman sekelas, dosen, staf akademik kampus) atau yang mengakses basis data publik mahasiswa seperti PDDikti.
     2. Program otomatis peretas di blockchain publik (*sweeper bots*) yang menjalankan serangan kamus (*dictionary attacks*) berisi kombinasi nama umum, tanggal lahir, dan nomor induk untuk menguras saldo alamat mana pun yang cocok secara otomatis.

4. **Level 8.** Jaringan Anda punya 4 node dan pemenangnya REZA-1 dengan 5 blok terbuang. Jelaskan mengapa node itu menang. Cari teman yang jaringannya sempat tidak sepakat: apa penyebabnya dan bagaimana diselesaikan?

   _Jawaban:_
   - **Mengapa REZA-1 Menang:**
     Pada jaringan simulasi fork, terdapat 4 node yang menambang blok privat. Node REZA-1 menambang 3 blok (panjang 5), REZA-2 menambang 2 blok (panjang 4), REZA-3 menambang 2 blok (panjang 4), dan REZA-4 menambang 1 blok (panjang 3). Berdasarkan aturan konsensus Nakamoto (*Longest Chain Rule*), setiap node wajib mengadopsi rantai terpanjang yang valid. Karena REZA-1 memiliki rantai terpanjang (panjang 5), node REZA-2, REZA-3, dan REZA-4 membuang cabang privat mereka dan mengadopsi rantai REZA-1. Blok pribadi milik REZA-2 (2 blok), REZA-3 (2 blok), dan REZA-4 (1 blok) gugur menjadi **blok yatim (*orphan blocks*)**, yaitu total $2 + 2 + 1 = 5$ blok yang terbuang.
   - **Kasus Jaringan Teman yang Sempat Tidak Sepakat:**
     Pada teman yang memiliki kombinasi digit NIM dan tanggal lahir tertentu (seperti Fahri), terjadi kondisi di mana dua node menghasilkan panjang rantai privat yang sama panjang (misalnya Node 1 dan Node 3 sama-sama mencapai panjang 5). Saat `resolve_conflicts` dijalankan, tidak ada cabang yang lebih panjang dari yang lain sehingga jaringan mengalami kondisi seri (*tie / network split*) dan `sepakat` bernilai `False`. Kondisi ini diselesaikan di blockchain dengan menambang satu blok baru (*tie-breaker*) pada salah satu cabang sehingga panjangnya bertambah (misalnya menjadi 6) dan memaksa seluruh node lain beralih mengadopsinya, memulihkan konsensus 100%.

5. **Level 9.** Dengan hadiah awal 39 dan halving setiap 3 blok, berapa batas total suplai jika mining berjalan selamanya? Tunjukkan perhitungannya, lalu kaitkan dengan batas 21 juta Bitcoin.

   _Jawaban:_
   - **Perhitungan Batas Total Suplai:**
     Dengan hadiah awal $H_0 = 39$ dan interval halving $I = 3$ blok menggunakan pembagian bilangan bulat (*integer division* `//`):
     - Periode 0 (Blok 1–3)  : Hadiah = 39 $\rightarrow 3 \times 39 = 117$ koin
     - Periode 1 (Blok 4–6)  : Hadiah = 19 ($39 // 2 = 19$) $\rightarrow 3 \times 19 = 57$ koin
     - Periode 2 (Blok 7–9)  : Hadiah = 9  ($19 // 2 = 9$)  $\rightarrow 3 \times 9 = 27$ koin
     - Periode 3 (Blok 10–12): Hadiah = 4  ($9 // 2 = 4$)   $\rightarrow 3 \times 4 = 12$ koin
     - Periode 4 (Blok 13–15): Hadiah = 2  ($4 // 2 = 2$)   $\rightarrow 3 \times 2 = 6$ koin
     - Periode 5 (Blok 16–18): Hadiah = 1  ($2 // 2 = 1$)   $\rightarrow 3 \times 1 = 3$ koin
     - Periode 6 (Blok 19–dst): Hadiah = 0  ($1 // 2 = 0$)   $\rightarrow$ Emisi koin berhenti selamanya.
     - **Total Suplai Riil Sistem:**
       $$\text{Total Suplai} = 117 + 57 + 27 + 12 + 6 + 3 = 222 \text{ koin}$$
     - **Secara Teoretis Deret Geometri Tak Hingga:**
       $$\text{Suplai Teoretis} = I \times H_0 \times \sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^k = 3 \times 39 \times 2 = 234 \text{ koin}$$
       (Perbedaan 12 koin terjadi akibat pemotongan desimal bilangan bulat pada nilai ganjil).
   - **Kaitannya dengan Batas 21 Juta Bitcoin:**
     Prinsip ini mencerminkan mekanisme moneter Bitcoin yang menerapkan hadiah awal 50 BTC dengan interval halving setiap 210.000 blok. Melalui formula deret geometri $210.000 \times 50 \times 2 = 21.000.000$ BTC, Bitcoin menjamin kelangkaan terprogram (*digital scarcity*) dan mencegah devaluasi inflasioner.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "tugas": "personal-2 (Level 6-9)",
  "profil": {
    "nama": "REZA TRI FEBRIANSYAH",
    "nim4": "2119",
    "tanggal_lahir": "2005-02-10",
    "kota_asal": "Sorong",
    "hobi": "Mancing"
  },
  "level6": {
    "data_ditambang": "REZA TRI FEBRIANSYAH|2119|2005-02-10",
    "mining": [
      {
        "difficulty": 1,
        "nonce": 37,
        "hash": "023cadeba0adc2f284e9ee61462348adecb3d5e9fc24bf1480a4b0e0d324b2e7",
        "percobaan": 38,
        "teori": 16
      },
      {
        "difficulty": 2,
        "nonce": 253,
        "hash": "00730b1ab680dbbf706aa847a1eb24f07fe3e0c6b2a5bc717730e453c6cc23f7",
        "percobaan": 254,
        "teori": 256
      },
      {
        "difficulty": 3,
        "nonce": 530,
        "hash": "000cc96f9e530b309598e3475613bbfa79634b45c9176997979c98ea556569d1",
        "percobaan": 531,
        "teori": 4096
      },
      {
        "difficulty": 4,
        "nonce": 5763,
        "hash": "00009ef81434eafe7942cbe01c52692bc187019f586a76f47365063c51f36dac",
        "percobaan": 5764,
        "teori": 65536
      }
    ],
    "difficulty_awal": 4,
    "daftar_waktu_detik": [
      8,
      4,
      4,
      36,
      4,
      0,
      0,
      8
    ],
    "target_detik": 10,
    "jejak_difficulty": [
      4,
      5,
      6,
      5,
      6,
      7,
      8,
      8
    ]
  },
  "level7": {
    "kunci_publik_awal": "e6e8cdc02d77ee15931a426863df1c8b",
    "alamat": "6da89cec12d6d93a5ff5828aa6e368c070b5d596",
    "transaksi": {
      "sender": "6da89cec12d6d93a5ff5828aa6e368c070b5d596",
      "recipient": "TEMAN_A",
      "amount": 10
    },
    "tanda_tangan": "744d39f65aef052dd791b376d6bc9a322b00ca690124ef72d7b996f074963e388145a95998751a07f64f481e7b66d1924b6d68e09e8ddd52d3f921f60ceb882d",
    "tanda_tangan_selalu_sama": true,
    "sah": true,
    "sah_setelah_amount_diubah": false,
    "ttd_penipu_valid_dengan_kuncinya": true,
    "transaksi_penipu_sah": false
  },
  "level8": {
    "jumlah_node": 4,
    "blok_pribadi_per_node": [
      3,
      2,
      2,
      1
    ],
    "panjang_saat_fork": [
      5,
      4,
      4,
      3
    ],
    "panjang_setelah_resolve": [
      5,
      5,
      5,
      5
    ],
    "sepakat_setelah_resolve": true,
    "perlu_pemecah_seri": false,
    "pemenang_fork": "REZA-1",
    "blok_terbuang": 5,
    "hash_ujung": "005f1f3870b201bad3c78e435411fae0e1703ea75a3f05a86265ba8d43758bca"
  },
  "level9": {
    "hadiah_awal": 39,
    "interval_halving": 3,
    "hadiah_per_blok": [
      39,
      39,
      39,
      19,
      19,
      19
    ],
    "saldo": {
      "REZA TRI FEBRIANSYAH": 113.0,
      "TEMAN_A": 35.0,
      "TEMAN_B": 26.0
    },
    "total_suplai": 174.0,
    "belanja_melebihi_saldo_ditolak": true,
    "validasi_ekonomi": true,
    "hash_ujung": "0058384283748e3b0ba67b4f1209b97f52450537cc99fd032883e47ab17e215e",
    "validasi_setelah_hadiah_dicurangi": false
  },
  "kode_verifikasi": "87162414C1CE"
}
```
