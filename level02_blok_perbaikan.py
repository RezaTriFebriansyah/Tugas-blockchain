"""
LEVEL 2 — Blockchain Dasar ala GeeksforGeeks, tanpa Flask
Versi perbaikan: semua fungsi TODO telah dilengkapi.
"""
import datetime
import hashlib
import json


class Blockchain:
    def __init__(self, difficulty: int = 4):
        if not isinstance(difficulty, int) or difficulty < 1 or difficulty > 6:
            raise ValueError("difficulty harus berupa bilangan bulat 1 sampai 6 untuk latihan ini")
        self.difficulty = difficulty
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof: int, previous_hash: str) -> dict:
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.chain.append(block)
        return block

    def last_block(self) -> dict:
        return self.chain[-1]

    def hash(self, block: dict) -> str:
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()

    def valid_proof(self, previous_proof: int, proof: int) -> bool:
        guess = f"{proof**2 - previous_proof**2}".encode("utf-8")
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash.startswith("0" * self.difficulty)

    def proof_of_work(self, previous_proof: int) -> int:
        new_proof = 1
        while not self.valid_proof(previous_proof, new_proof):
            new_proof += 1
        return new_proof

    def mine_block(self) -> dict:
        previous_block = self.last_block()
        proof = self.proof_of_work(previous_block["proof"])
        previous_hash = self.hash(previous_block)
        return self.create_block(proof, previous_hash)

    def chain_valid(self, chain: list) -> bool:
        if not isinstance(chain, list) or len(chain) == 0:
            return False
        # Validasi tautan hash dan Proof of Work untuk setiap blok setelah genesis.
        for i in range(1, len(chain)):
            if chain[i].get("previous_hash") != self.hash(chain[i - 1]):
                return False
            if not self.valid_proof(chain[i - 1].get("proof"), chain[i].get("proof")):
                return False
        return True


if __name__ == "__main__":
    bc = Blockchain(difficulty=4)
    for _ in range(4):
        b = bc.mine_block()
        print(f"Blok #{b['index']} ditambang, proof={b['proof']}")
    print(json.dumps(bc.chain, indent=2))
    print("Rantai valid?", bc.chain_valid(bc.chain))
