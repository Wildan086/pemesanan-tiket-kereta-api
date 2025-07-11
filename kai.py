import csv
import os

JADWAL_FILE = "jadwal.csv"
RIWAYAT_FILE = "riwayat.csv"


def load_jadwal():
    jadwal = []
    with open(JADWAL_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            jadwal.append(row)
    return jadwal


def tampilkan_jadwal(jadwal):
    print("\n=== DAFTAR JADWAL KERETA ===")
    for i, j in enumerate(jadwal):
        print(f"{i+1}. {j['Kereta']} | {j['Asal']} → {j['Tujuan']} | {j['Tanggal']} | Rp{j['Harga']}")


def beli_tiket(jadwal):
    tampilkan_jadwal(jadwal)
    try:
        pilih = int(input("Pilih nomor kereta: ")) - 1
        nama = input("Nama Pemesan: ")
        jumlah = int(input("Jumlah Tiket: "))
        data = jadwal[pilih]
        total = int(data["Harga"]) * jumlah

        with open(RIWAYAT_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nama, data['Kereta'], data['Asal'], data['Tujuan'], data['Tanggal'], jumlah, total])
            print("✅ Tiket berhasil dipesan!")
    except:
        print("❌ Terjadi kesalahan saat pemesanan!")


def lihat_riwayat():
    print("\n=== RIWAYAT PEMBELIAN TIKET KERETA ===")
    try:
        with open(RIWAYAT_FILE, mode='r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                print(f"{i+1}. Nama: {row[0]}, {row[1]} {row[2]} → {row[3]} | {row[4]} | {row[5]} tiket | Total: Rp{row[6]}")
    except FileNotFoundError:
        print("❌ Belum ada riwayat pembelian.")


def edit_riwayat():
    lihat_riwayat()
    idx = int(input("Pilih nomor riwayat yang ingin diedit: ")) - 1
    rows = []

    with open(RIWAYAT_FILE, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if 0 <= idx < len(rows):
        nama = input("Nama baru: ")
        jumlah = int(input("Jumlah tiket baru: "))
        harga_per_tiket = int(rows[idx][6]) // int(rows[idx][5])
        total = harga_per_tiket * jumlah
        rows[idx][0] = nama
        rows[idx][5] = jumlah
        rows[idx][6] = total

        with open(RIWAYAT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("✅ Riwayat berhasil diperbarui!")
    else:
        print("❌ Data tidak ditemukan.")


def hapus_riwayat():
    lihat_riwayat()
    idx = int(input("Pilih nomor yang ingin dihapus: ")) - 1
    rows = []

    with open(RIWAYAT_FILE, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if 0 <= idx < len(rows):
        del rows[idx]
        with open(RIWAYAT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("✅ Riwayat berhasil dihapus!")
    else:
        print("❌ Data tidak ditemukan.")


def main():
    if not os.path.exists(RIWAYAT_FILE):
        with open(RIWAYAT_FILE, mode='w', newline='') as file:
            pass

    jadwal = load_jadwal()

    while True:
        print("\n=== MENU PEMESANAN TIKET KERETA ===")
        print("1. Lihat Jadwal Kereta")
        print("2. Beli Tiket")
        print("3. Lihat Riwayat Pembelian")
        print("4. Edit Pemesanan")
        print("5. Hapus Riwayat Pembelian")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_jadwal(jadwal)
        elif pilih == "2":
            beli_tiket(jadwal)
        elif pilih == "3":
            lihat_riwayat()
        elif pilih == "4":
            edit_riwayat()
        elif pilih == "5":
            hapus_riwayat()
        elif pilih == "0":
            break
        else:
            print("❌ Pilihan tidak valid.")


if __name__ == "__main__":
    main()
