menu = {
    1: {"item": "Nasi Goreng", "harga": 13000},
    2: {"item": "Mie Goreng", "harga": 13000},
    3: {"item": "Ayam Goreng", "harga": 15000},
    4: {"item": "Es Teh", "harga": 2000},
    5: {"item": "Es Jeruk", "harga": 5000}
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("========== Daftar Menu ==========")
    for num, value in menu.items():
        print(f"{num}. {value['item']} \t: Rp {value['harga']}\t|")
    print("=================================")

# Fungsi untuk menghitung total pembelian
def hitung_total(pesanan):
    total = 0
    for pilihan, jumlah in pesanan.items():
        total += menu[pilihan]["harga"] * jumlah
    return total

# Fungsi untuk membatalkan pesanan
def batalkan_pesanan(pesanan):
    try:
        print("=========== Pembatalan Pesanan ===========")
        for num, (pilihan, jumlah) in enumerate(pesanan.items(), start=1):
            print(f"{num}. {menu[pilihan]['item']} ({jumlah})")
        nomor_pesanan = int(input("Masukkan nomor pesanan yang ingin dibatalkan (0 untuk kembali)\t: "))
        if nomor_pesanan == 0:
            return
        elif 1 <= nomor_pesanan <= len(pesanan):
            pilihan_terpilih = list(pesanan.keys())[nomor_pesanan - 1]
            jumlah_hapus = int(input(f"Masukkan jumlah yang ingin dikurangi dari pesanan {menu[pilihan_terpilih]['item']}\t: "))
            if jumlah_hapus < pesanan[pilihan_terpilih]:
                pesanan[pilihan_terpilih] -= jumlah_hapus
                print(f"{menu[pilihan_terpilih]['item']} ({jumlah_hapus}) dikurangi dari pesanan.")
            elif jumlah_hapus == pesanan[pilihan_terpilih]:
                del pesanan[pilihan_terpilih]
                print(f"{menu[pilihan_terpilih]['item']} dibatalkan.")
            else:
                print("Jumlah yang ingin dikurangi melebihi pesanan yang ada.")
        else:
            print("Nomor pesanan tidak valid.")
    except ValueError:
        print("Masukkan nomor pesanan yang valid.")

# Fungsi utama
def main():
    print("============ Warung Arul ============")
    nama_kasir = input("Nama Kasir: ")

    pesanan = {}
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-5)\n0 untuk mengakhiri pesanan\ndan -1 untuk pembatalan/pengurangan pesanan\t: "))
            if pilihan == 0:
                break
            elif pilihan == -1:
                batalkan_pesanan(pesanan)
            elif pilihan not in menu:
                print("Pilihan tidak valid. Silakan masukkan nomor yang benar -_-")
            else:
                jumlah = int(input(f"Masukkan jumlah yang ingin dibeli\t\t: "))
                if pilihan in pesanan:
                    pesanan[pilihan] += jumlah
                else:
                    pesanan[pilihan] = jumlah
        except ValueError:
            print("Masukkan nomor atau jumlah yang valid.")

    if not pesanan:
        print("Anda belum memesan apapun.")
    else:
        total_harga = hitung_total(pesanan)
        print("Tagihan\t: Rp",total_harga)

        # Meminta input jumlah uang yang diberikan oleh pelanggan
        Bayar_input = input("Bayar\t: Rp ")
        if Bayar_input.isdigit():
            Tunai = int(Bayar_input)
        else:
            print("Masukkan jumlah uang yang valid.")

        # Menghitung kembalian
        kembalian = Tunai - total_harga

        # Menampilkan struk pembelian
        print("\n============ Struk Pembelian ============")
        print(f"Nama Kasir \t\t= {nama_kasir}\t\t|")
        print("=========================================")
        for pilihan, jumlah in pesanan.items():
            print(f"{menu[pilihan]['item']} Sejumlah {jumlah} \t= Rp {menu[pilihan]['harga'] * jumlah}\t|")
        print("=========================================")
        print(f"Total Harga \t\t= Rp {total_harga}\t|")
        print(f"Tunai \t\t\t= Rp {Tunai}\t|")
        print(f"Kembalian \t\t= Rp {kembalian}\t|")
        print("=========================================")

        return total_harga, Tunai, kembalian

if __name__ == "__main__":
    total_harga, tunai, kembalian = main()