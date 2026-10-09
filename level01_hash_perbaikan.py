"""
LEVEL 1 — Fungsi Hash SHA-256 (LATIHAN)
Versi perbaikan: semua fungsi TODO telah dilengkapi.
"""
import hashlib
import json


def sha256_hex(teks: str) -> str:
    """Kembalikan hash SHA-256 teks (UTF-8) dalam bentuk heksadesimal."""
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()


def hash_dict(data: dict) -> str:
    """Hash dict secara kanonik agar urutan key tidak memengaruhi hasil."""
    teks_json = json.dumps(data, sort_keys=True)
    return sha256_hex(teks_json)


def bit_berbeda(hash_a: str, hash_b: str) -> int:
    """Hitung jumlah bit yang berbeda antara dua hash heksadesimal."""
    return (int(hash_a, 16) ^ int(hash_b, 16)).bit_count()


def persen_bit_berbeda(teks_a: str, teks_b: str) -> float:
    """Persentase bit berbeda antara hash SHA-256 dari dua teks."""
    return bit_berbeda(sha256_hex(teks_a), sha256_hex(teks_b)) / 256 * 100


if __name__ == "__main__":
    a, b = "Teknologi Blockchain", "teknologi Blockchain"
    print(f"SHA256('{a}') = {sha256_hex(a)}")
    print(f"SHA256('{b}') = {sha256_hex(b)}")
    print(f"Bit berbeda: {persen_bit_berbeda(a, b):.1f}%  (efek avalanche)")
    print("Hash dict urutan berbeda sama?",
          hash_dict({"nama": "Ani", "nilai": 5}) == hash_dict({"nilai": 5, "nama": "Ani"}))
