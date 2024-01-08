print("============ Kantin UPB ============")
nama = input("Nama Kasir: ")

menu = {
    1: {"item": "Nasi Goreng", "harga": 13000},
    2: {"item": "Mie Goreng", "harga": 13000},
    3: {"item": "Ayam Goreng", "harga": 18000},
    4: {"item": "Es Teh", "harga": 2000},
    5: {"item": "Es Jeruk", "harga": 5000},
}

def tampilkan_menu():
    print("========== Daftar Menu ==========")
    for num, value in menu.items():
        print(f"{num}. {value['item']} \t: Rp {value['harga']}\t|")
    print("=================================")

def hitung_total(pesanan):
    total = 0
    for pilihan, jumlah in pesanan.items():
        total += menu[pilihan]["harga"] * jumlah
    return total

def main():
    pesanan = {}
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-5) atau 0 untuk mengakhiri pesanan: "))
            if pilihan == 0:
                break
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

        # Meminta input jumlah uang yang diberikan oleh pelanggan
        Bayar_input = input("Bayar\t: ")
        if Bayar_input.isdigit():
            Tunai = int(Bayar_input)
        else:
            print("Masukkan jumlah uang yang valid.")

        # Menghitung kembalian
        kembalian = Tunai - total_harga

        print("\n============ Struk Pembelian ============")
        for pilihan, jumlah in pesanan.items():
            print(f"{menu[pilihan]['item']} Sejumlah {jumlah} \t= Rp {menu[pilihan]['harga'] * jumlah}\t|")
        print("=========================================")
        print(f"Total Harga \t\t= Rp {total_harga}\t|")
        print(f"Tunai \t\t\t= Rp {Tunai}\t|")
        print(f"Kembalian \t\t= Rp {kembalian}\t|")
        print("=========================================")

if __name__ == "__main__":
    main()