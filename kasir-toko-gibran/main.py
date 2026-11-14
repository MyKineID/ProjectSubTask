manusia = input("Nama Pembeli: ")

total = 0
struk = []
nomor = 1

while True:
    print("\n8---------------+--------D")
    print("| Barang        | Harga  |")
    print("8---------------+--------D")
    print("| 1 | indomie   | 3500   |")
    print("| 2 | telur     | 2500   |")
    print("8---------------+--------D")
    print(f"Input barang ke-{nomor} (ketik 0 untuk berhenti)")
    
    nama_barang = input("Nama Barang : ").lower()
    if nama_barang == "0":
        break
    if nama_barang == "1":
        harga = 3500
    elif nama_barang == "2":
        harga = 2500
    else:
        print("Barangnya gada kocak, pilih 1 atau 2 lah.")
        continue

    total += harga
    struk.append((nama_barang, harga))
    nomor += 1

if total >= 100000:
    diskon = total * 0.1
elif total >= 50000:
    diskon = total * 0.05
else:
    diskon = 0

bayar = int(total - diskon)

print("\nSTRUK TOKO GIBRAN")
print(f"Pembeli : {manusia}")

print("8---------------+--------D")
print("- Indomie : 3.500")
print("- Telur   : 2.500")
print("8---------------+--------D")
print(f"Total   : Rp {total:,}")
print(f"Diskon  : Rp {diskon:,}")
print(f"Bayar   : Rp {bayar:,}")
