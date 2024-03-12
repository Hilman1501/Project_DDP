import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class BiayaProduksi:
    def __init__(self, harga_kain, jumlah_kain, harga_resleting, jumlah_resleting, harga_kancing, jumlah_kancing, harga_gaji_perpegawai, jumlah_pegawai, overhead):
        self.harga_kain = harga_kain
        self.jumlah_kain = jumlah_kain
        self.harga_resleting = harga_resleting
        self.jumlah_resleting = jumlah_resleting
        self.harga_kancing = harga_kancing
        self.jumlah_kancing = jumlah_kancing
        self.harga_gaji_perpegawai = harga_gaji_perpegawai
        self.jumlah_pegawai = jumlah_pegawai
        self.overhead = overhead

    def hitung_total_biaya_bahan_baku(self):
        total_kain = self.harga_kain * self.jumlah_kain
        total_resleting = self.harga_resleting * self.jumlah_resleting
        total_kancing = self.harga_kancing * self.jumlah_kancing
        return total_kain + total_resleting + total_kancing

    def hitung_total_biaya_tenaga_kerja(self):
        return self.harga_gaji_perpegawai * self.jumlah_pegawai

    def hitung_total_biaya(self):
        total_bahan_baku = self.hitung_total_biaya_bahan_baku()
        total_tenaga_kerja = self.hitung_total_biaya_tenaga_kerja()
        return total_bahan_baku + total_tenaga_kerja + self.overhead

def konversi_mata_uang(jumlah, kurs):
    return jumlah * kurs

def hitung_biaya_produksi():
    # Harga dan jumlah bahan baku
    harga_kain = float(entries["Harga Kain per Meter (Rp):"].get())
    jumlah_kain = float(entries["Jumlah Meter Kain:"].get())
    harga_resleting = float(entries["Harga Resleting per Unit (Rp):"].get())
    jumlah_resleting = float(entries["Jumlah Unit Resleting:"].get())
    harga_kancing = float(entries["Harga Kancing per Unit (Rp):"].get())
    jumlah_kancing = float(entries["Jumlah Unit Kancing:"].get())

    # Biaya tenaga kerja
    harga_gaji_perpegawai = float(entries["Harga Gaji Pegawai per Orang (Rp):"].get())
    jumlah_pegawai = float(entries["Jumlah Pegawai:"].get())
    overhead_local = float(entries["Biaya Overhead (Rp):"].get())

    biaya_produksi = BiayaProduksi(
        harga_kain, jumlah_kain, 
        harga_resleting, jumlah_resleting, 
        harga_kancing, jumlah_kancing, 
        harga_gaji_perpegawai, jumlah_pegawai, 
        overhead_local
    )

    total_biaya_bahan_baku = biaya_produksi.hitung_total_biaya_bahan_baku()
    total_biaya_tenaga_kerja = biaya_produksi.hitung_total_biaya_tenaga_kerja()
    total_biaya_local = biaya_produksi.hitung_total_biaya()
    total_biaya_usd = konversi_mata_uang(total_biaya_local, float(entries_kurs["Kurs USD:"].get()))
    total_biaya_eur = konversi_mata_uang(total_biaya_local, float(entries_kurs["Kurs EUR:"].get()))

    # Label hasil perhitungan
    label_biaya_bahan_baku.config(text=f'Total Biaya Bahan Baku: {total_biaya_bahan_baku:.2f} IDR')
    label_biaya_tenaga_kerja.config(text=f'Total Biaya Tenaga Kerja: {total_biaya_tenaga_kerja:.2f} IDR')
    label_biaya_produksi_local.config(text=f'Total Biaya Produksi: {total_biaya_local:.2f} IDR')
    label_biaya_produksi_usd.config(text=f'Total Biaya Produksi (USD): {total_biaya_usd:.2f} USD')
    label_biaya_produksi_eur.config(text=f'Total Biaya Produksi (EUR): {total_biaya_eur:.2f} EUR')


# Kurs konversi mata uang
kurs_usd = 0.012 
kurs_eur = 0.01  

# GUI
root = tk.Tk()
root.title("Kalkulator Biaya Produksi")

style = Style(theme='cosmo')
root.configure(bg='#90E0EF') 

# Frame input
input_frame = ttk.Frame(root, padding="50", borderwidth=5, relief="solid")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600 
window_height = 700 

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

labels = ["Harga Kain per Meter (Rp):", "Jumlah Meter Kain:", "Harga Resleting per Unit (Rp):", "Jumlah Unit Resleting:",
          "Harga Kancing per Unit (Rp):", "Jumlah Unit Kancing:", "Harga Gaji Pegawai per Orang (Rp):", "Jumlah Pegawai:", "Biaya Overhead (Rp):"]

entries = {}  

for i, label_text in enumerate(labels):
    label = ttk.Label(input_frame, text=label_text)
    label.grid(column=0, row=i, sticky=tk.W)
    entry = ttk.Entry(input_frame)
    entry.grid(column=1, row=i)
    entries[label_text] = entry

# Button buat ngehitung
hitung_button = ttk.Button(input_frame, text="Hitung Biaya Produksi", command=hitung_biaya_produksi)
hitung_button.grid(column=0, row=9, columnspan=2, pady=(10,0))

# Frame output
output_frame = ttk.Frame(root, padding="10", borderwidth=2, relief="solid")
output_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label hasil perhitungan
label_biaya_bahan_baku = ttk.Label(output_frame, text="")
label_biaya_bahan_baku.grid(column=0, row=0, sticky=tk.W)

label_biaya_tenaga_kerja = ttk.Label(output_frame, text="")
label_biaya_tenaga_kerja.grid(column=0, row=1, sticky=tk.W)

label_biaya_produksi_local = ttk.Label(output_frame, text="")
label_biaya_produksi_local.grid(column=0, row=2, sticky=tk.W)

label_biaya_produksi_usd = ttk.Label(output_frame, text="")
label_biaya_produksi_usd.grid(column=0, row=3, sticky=tk.W)

label_biaya_produksi_eur = ttk.Label(output_frame, text="")
label_biaya_produksi_eur.grid(column=0, row=4, sticky=tk.W)


kurs_frame = ttk.Frame(output_frame)
kurs_frame.grid(column=0, row=5, columnspan=2, pady=(10,0))

labels_kurs = ["Kurs USD:", "Kurs EUR:"]
entries_kurs = {}
for i, label_text in enumerate(labels_kurs):
    label = ttk.Label(kurs_frame, text=label_text)
    label.grid(column=0, row=i, sticky=tk.W)
    entry = ttk.Entry(kurs_frame)
    entry.grid(column=1, row=i)
    entries_kurs[label_text] = entry  
    entry.insert(0, kurs_usd if i == 0 else kurs_eur)

root.mainloop()
