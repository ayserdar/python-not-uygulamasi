import tkinter as tk
from tkinter import messagebox


def not_ekle():
    not_yazisi = entry.get().strip()

    if not_yazisi == "":
        messagebox.showwarning("Uyarı", "Boş not ekleyemezsin.")
        return

    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(not_yazisi + "\n")

    entry.delete(0, tk.END)
    messagebox.showinfo("Başarılı", "Not kaydedildi.")
    notlari_goster()


def notlari_goster():
    text_alani.delete("1.0", tk.END)

    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()

        if len(notlar) == 0:
            text_alani.insert(tk.END, "Henüz not yok.\n")
        else:
            text_alani.insert(tk.END, "---- NOTLAR ----\n\n")
            for i, not_ in enumerate(notlar, 1):
                text_alani.insert(tk.END, f"{i}- {not_.strip()}\n")

    except FileNotFoundError:
        text_alani.insert(tk.END, "Henüz not yok.\n")


def not_sil():
    silinecek = entry.get().strip()

    if silinecek == "":
        messagebox.showwarning("Uyarı", "Silmek için not numarası gir.")
        return

    if not silinecek.isdigit():
        messagebox.showwarning("Uyarı", "Lütfen sayı gir.")
        return

    silinecek = int(silinecek)

    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()

        if len(notlar) == 0:
            messagebox.showinfo("Bilgi", "Silinecek not yok.")
            return

        if 1 <= silinecek <= len(notlar):
            notlar.pop(silinecek - 1)

            with open("notlar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(notlar)

            entry.delete(0, tk.END)
            messagebox.showinfo("Başarılı", "Not silindi.")
            notlari_goster()
        else:
            messagebox.showwarning("Uyarı", "Geçersiz not numarası.")

    except FileNotFoundError:
        messagebox.showinfo("Bilgi", "Henüz not dosyası yok.")


def temizle():
    entry.delete(0, tk.END)
    text_alani.delete("1.0", tk.END)


pencere = tk.Tk()
pencere.title("Not Uygulaması")
pencere.geometry("520x520")
pencere.configure(bg="#1e1e1e")
pencere.resizable(False, False)

baslik = tk.Label(
    pencere,
    text="NOT UYGULAMASI",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
baslik.pack(pady=15)

aciklama = tk.Label(
    pencere,
    text="Not eklemek için yazı gir. Silmek için not numarası gir.",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="lightgray"
)
aciklama.pack()

entry = tk.Entry(
    pencere,
    width=38,
    font=("Arial", 12)
)
entry.pack(pady=10, ipady=6)

buton_frame = tk.Frame(pencere, bg="#1e1e1e")
buton_frame.pack(pady=10)

ekle_btn = tk.Button(
    buton_frame,
    text="Not Ekle",
    font=("Arial", 11, "bold"),
    width=12,
    command=not_ekle
)
ekle_btn.grid(row=0, column=0, padx=5, pady=5)

goster_btn = tk.Button(
    buton_frame,
    text="Notları Göster",
    font=("Arial", 11, "bold"),
    width=12,
    command=notlari_goster
)
goster_btn.grid(row=0, column=1, padx=5, pady=5)

sil_btn = tk.Button(
    buton_frame,
    text="Not Sil",
    font=("Arial", 11, "bold"),
    width=12,
    command=not_sil
)
sil_btn.grid(row=0, column=2, padx=5, pady=5)

temizle_btn = tk.Button(
    buton_frame,
    text="Temizle",
    font=("Arial", 11, "bold"),
    width=12,
    command=temizle
)
temizle_btn.grid(row=1, column=1, padx=5, pady=5)

text_alani = tk.Text(
    pencere,
    width=52,
    height=18,
    font=("Consolas", 11)
)
text_alani.pack(pady=15)

pencere.mainloop()