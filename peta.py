class Produk:
    def _init_(self, kode, nama, harga, kategori):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.kategori = kategori

def main():
    
    produk = {}
   
    produk["P001"] = Produk("P001", "Laptop", 5000000, "Elektronik")
    produk["P002"] = Produk("P002", "Smartphone", 3000000, "Elektronik")
    produk["P003"] = Produk("P003", "Sepatu", 200000, "Pakaian")

   
    kode_produk = input("Masukkan kode produk: ")
    if kode_produk in produk:
        produk_ditemukan = produk[kode_produk]
        print(f"Produk dengan kode {kode_produk}:")
        print(f"- Nama: {produk_ditemukan.nama}")
        print(f"- Harga: {produk_ditemukan.harga}")
        print(f"- Kategori: {produk_ditemukan.kategori}")
    else:
        print(f"Produk dengan kode {kode_produk} tidak ditemukan")

   
    nama_produk = input("Masukkan nama produk: ")
    produk_yang_cocok = []
    for produk_value in produk.values():
        if nama_produk.lower() in produk_value.nama.lower():
            produk_yang_cocok.append(produk_value)
    if produk_yang_cocok:
        print(f"Produk dengan nama yang mengandung '{nama_produk}':")
        for produk in produk_yang_cocok:
            print(f"- {produk.nama}")
    else:
        print(f"Produk dengan nama yang mengandung '{nama_produk}' tidak ditemukan")

    
    kategori = input("Masukkan kategori: ")
    produk_dalam_kategori = []
    for produk_value in produk.values():
        if kategori.lower() == produk_value.kategori.lower():
            produk_dalam_kategori.append(produk_value)
    if produk_dalam_kategori:
        print(f"Produk dalam kategori '{kategori}':")
        for produk in produk_dalam_kategori:
            print(f"- {produk.nama}")
    else:
        print(f"Produk dalam kategori '{kategori}' tidak ditemukan")

if _name_ == "_main_":
    main()
