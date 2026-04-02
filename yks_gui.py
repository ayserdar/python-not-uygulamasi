import tkinter as tk
from tkinter import messagebox


def kayit_ekle():
    ders = ders_entry.get().strip()
    soru = soru_entry.get().strip()
    sure = sure_entry.get().strip()

    if ders == "" or soru == "" or sure == "":
        messagebox.showwarning("Uyarı", "Tüm alanları doldur.")
        return

    if not soru.isdigit():
        messagebox.showwarning("Uyarı", "Soru sayısı sayı olmalı.")
        return

    try:
        float(sure)
    except ValueError:
        messagebox.showwarning("Uyarı", "Süre sayı olmalı. Örnek: 1.5")
        return

    with open("yks_kayitlari.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{ders},{soru},{sure}\n")

    ders_entry.delete(0, tk.END)
    soru_entry.delete(0, tk.END)
    sure_entry.delete(0, tk.END)

    messagebox.showinfo("Başarılı", "Kayıt eklendi.")
    kayitlari_goster()


def kayitlari_goster():
    text_alani.delete("1.0", tk.END)

    try:
        with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
            kayitlar = dosya.readlines()

        if len(kayitlar) == 0:
            text_alani.insert(tk.END, "Henüz kayıt yok.\n")
        else:
            text_alani.insert(tk.END, "---- YKS KAYITLARI ----\n\n")
            for i, kayit in enumerate(kayitlar, 1):
                ders, soru, sure = kayit.strip().split(",")
                text_alani.insert(
                    tk.END,
                    f"{i}- Ders: {ders} | Soru: {soru} | Süre: {sure} saat\n"
                )

    except FileNotFoundError:
        text_alani.insert(tk.END, "Henüz kayıt yok.\n")


def kayit_sil():
    sil_no = sil_entry.get().strip()

    if sil_no == "":
        messagebox.showwarning("Uyarı", "Silmek için kayıt numarası gir.")
        return

    if not sil_no.isdigit():
        messagebox.showwarning("Uyarı", "Kayıt numarası sayı olmalı.")
        return

    sil_no = int(sil_no)

    try:
        with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
            kayitlar = dosya.readlines()

        if len(kayitlar) == 0:
            messagebox.showinfo("Bilgi", "Silinecek kayıt yok.")
            return

        if 1 <= sil_no <= len(kayitlar):
            kayitlar.pop(sil_no - 1)

            with open("yks_kayitlari.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(kayitlar)

            sil_entry.delete(0, tk.END)
            messagebox.showinfo("Başarılı", "Kayıt silindi.")
            kayitlari_goster()
        else:
            messagebox.showwarning("Uyarı", "Geçersiz kayıt numarası.")

    except FileNotFoundError:
        messagebox.showinfo("Bilgi", "Henüz kayıt dosyası yok.")


def toplam_goster():
    try:
        with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
            kayitlar = dosya.readlines()

        toplam_soru = 0
        toplam_sure = 0.0

        for kayit in kayitlar:
            ders, soru, sure = kayit.strip().split(",")
            toplam_soru += int(soru)
            toplam_sure += float(sure)

        messagebox.showinfo(
            "Toplam Bilgi",
            f"Toplam soru: {toplam_soru}\nToplam süre: {toplam_sure} saat"
        )

    except FileNotFoundError:
        messagebox.showinfo("Bilgi", "Henüz kayıt yok.")


def hedef_kontrol():
    hedef = hedef_entry.get().strip()

    if hedef == "":
        messagebox.showwarning("Uyarı", "Lütfen günlük hedef gir.")
        return

    if not hedef.isdigit():
        messagebox.showwarning("Uyarı", "Hedef sayı olmalı.")
        return

    hedef = int(hedef)

    try:
        with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
            kayitlar = dosya.readlines()

        toplam_soru = 0

        for kayit in kayitlar:
            ders, soru, sure = kayit.strip().split(",")
            toplam_soru += int(soru)

        if toplam_soru >= hedef:
            messagebox.showinfo(
                "Hedef Durumu",
                f"Helal! Hedef tamamlandı 💪\nToplam soru: {toplam_soru}/{hedef}"
            )
        else:
            kalan = hedef - toplam_soru
            messagebox.showinfo(
                "Hedef Durumu",
                f"Devam et 🔥\nToplam soru: {toplam_soru}/{hedef}\nKalan: {kalan}"
            )

    except FileNotFoundError:
        messagebox.showinfo("Bilgi", "Henüz kayıt yok.")


def temizle():
    ders_entry.delete(0, tk.END)
    soru_entry.delete(0, tk.END)
    sure_entry.delete(0, tk.END)
    hedef_entry.delete(0, tk.END)
    sil_entry.delete(0, tk.END)
    text_alani.delete("1.0", tk.END)


pencere = tk.Tk()
pencere.title("SERDAR YKS PRO")
pencere.geometry("720x700")
pencere.configure(bg="#1e1e1e")
pencere.resizable(False, False)

baslik = tk.Label(
    pencere,
    text="SERDAR YKS PRO",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
baslik.pack(pady=15)

form_frame = tk.Frame(pencere, bg="#1e1e1e")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Ders:", font=("Arial", 11), bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
ders_entry = tk.Entry(form_frame, width=25, font=("Arial", 11))
ders_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Soru:", font=("Arial", 11), bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
soru_entry = tk.Entry(form_frame, width=25, font=("Arial", 11))
soru_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Süre (saat):", font=("Arial", 11), bg="#1e1e1e", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
sure_entry = tk.Entry(form_frame, width=25, font=("Arial", 11))
sure_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Günlük hedef:", font=("Arial", 11), bg="#1e1e1e", fg="white").grid(row=3, column=0, padx=5, pady=5, sticky="e")
hedef_entry = tk.Entry(form_frame, width=25, font=("Arial", 11))
hedef_entry.grid(row=3, column=1, padx=5, pady=5)

buton_frame = tk.Frame(pencere, bg="#1e1e1e")
buton_frame.pack(pady=15)

ekle_btn = tk.Button(
    buton_frame,
    text="Kaydet",
    font=("Arial", 11, "bold"),
    width=14,
    command=kayit_ekle
)
ekle_btn.grid(row=0, column=0, padx=5, pady=5)

goster_btn = tk.Button(
    buton_frame,
    text="Kayıtları Göster",
    font=("Arial", 11, "bold"),
    width=14,
    command=kayitlari_goster
)
goster_btn.grid(row=0, column=1, padx=5, pady=5)

toplam_btn = tk.Button(
    buton_frame,
    text="Toplamı Göster",
    font=("Arial", 11, "bold"),
    width=14,
    command=toplam_goster
)
toplam_btn.grid(row=0, column=2, padx=5, pady=5)

hedef_btn = tk.Button(
    buton_frame,
    text="Hedef Kontrol",
    font=("Arial", 11, "bold"),
    width=14,
    command=hedef_kontrol
)
hedef_btn.grid(row=1, column=0, padx=5, pady=5)

sil_frame = tk.Frame(pencere, bg="#1e1e1e")
sil_frame.pack(pady=10)

tk.Label(sil_frame, text="Silinecek kayıt no:", font=("Arial", 11), bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=5, pady=5)
sil_entry = tk.Entry(sil_frame, width=10, font=("Arial", 11))
sil_entry.grid(row=0, column=1, padx=5, pady=5)

sil_btn = tk.Button(
    sil_frame,
    text="Kayıt Sil",
    font=("Arial", 11, "bold"),
    width=12,
    command=kayit_sil
)
sil_btn.grid(row=0, column=2, padx=5, pady=5)

temizle_btn = tk.Button(
    pencere,
    text="Temizle",
    font=("Arial", 11, "bold"),
    width=12,
    command=temizle
)
temizle_btn.pack(pady=10)

text_alani = tk.Text(
    pencere,
    width=75,
    height=18,
    font=("Consolas", 11)
)
text_alani.pack(pady=15)

pencere.mainloop()