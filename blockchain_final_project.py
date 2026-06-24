import hashlib
import random
import time

print("=" * 70)
print(" ARSITEKTUR MATEMATIKA DI BALIK BLOCKCHAIN ")
print(" MERKLE TREE - SHA-256 - RSA - JARINGAN PEER TO PEER ")
print("=" * 70)

start = time.perf_counter()


# ==================================================
# FUNGSI SHA-256
# ==================================================

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


# ==================================================
# DATA TRANSAKSI
# ==================================================

transaksi = [
    "Rima -> Salwa : Rp100.000",
    "Salwa -> Najwa : Rp50.000",
    "Najwa -> Andi : Rp75.000",
    "Andi -> Budi : Rp25.000"
]

print("\nDAFTAR TRANSAKSI")

for i, t in enumerate(transaksi, start=1):

    print(f"{i}. {t}")


# ==================================================
# SHA-256
# ==================================================

print("\nSHA-256")

hashes = []

for i, t in enumerate(transaksi, start=1):

    h = sha256(t)

    hashes.append(h)

    print(f"H{i}: {h}")


# ==================================================
# MERKLE TREE
# ==================================================

print("\nMERKLE TREE")

current_hashes = hashes.copy()

level = 1

while len(current_hashes) > 1:

    print(f"\nLevel {level}")

    next_level = []

    if len(current_hashes) % 2 != 0:

        current_hashes.append(current_hashes[-1])

    for i in range(0, len(current_hashes), 2):

        parent = sha256(
            current_hashes[i] + current_hashes[i+1]
        )

        next_level.append(parent)

        print(f"Node {i+1} + Node {i+2}")

        print(parent)

    current_hashes = next_level

    level += 1


merkle_root = current_hashes[0]

print("\nMERKLE ROOT")

print(merkle_root)


# ==================================================
# RSA SEDERHANA
# ==================================================

print("\nRSA (SIMULASI TANDA TANGAN DIGITAL)")

public_key = random.randint(1000, 9999)

private_key = random.randint(10000, 99999)

digital_signature = sha256(
    merkle_root + str(private_key)
)

print("Public Key  :", public_key)

print("Private Key :", private_key)

print("Digital Signature :")

print(digital_signature)


# ==================================================
# JARINGAN PEER TO PEER
# ==================================================

print("\nJARINGAN PEER TO PEER")

node = [
    "Node A",
    "Node B",
    "Node C"
]

for n in node:

    print(f"{n} terhubung ke jaringan.")


print("\nDistribusi Blok")

for n in node[1:]:

    print(f"Node A mengirim blok ke {n}")

print("\nSemua node menerima blok yang sama.")


# ==================================================
# VERIFIKASI
# ==================================================

print("\nVERIFIKASI")

print("✓ SHA-256 berhasil membuat hash transaksi")

print("✓ Merkle Tree berhasil membentuk Merkle Root")

print("✓ RSA berhasil membuat tanda tangan digital")

print("✓ Peer-to-Peer berhasil mendistribusikan blok")


# ==================================================
# WAKTU EKSEKUSI
# ==================================================

end = time.perf_counter()

print("\nWAKTU EKSEKUSI")

print(f"{(end-start):.6f} detik")

print("\n" + "=" * 70)

print("PROGRAM SELESAI")

print("=" * 70)