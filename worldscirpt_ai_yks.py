import tkinter as tk
from tkinter import messagebox
import json
import os

DOSYA_ADI = "worldscirpt_yks_veri.json"


class WorldscirptAIYKS:
    def __init__(self, root):
        self.root = root
        self.root.title("Worldscirpt AI YKS Asistanı")
        self.root.geometry("1200x760")
        self.root.config(bg="#101820")
        self.root.resizable(False, False)

        self.veriler = []
        self.verileri_yukle()
        self.arayuzu_olustur()
        self.listeyi_guncelle()
        self.analizi_guncelle()

    def arayuzu_olustur(self):
        # Başlık
        baslik = tk.Label(
            self.root,
            text="Worldscirpt AI YKS Asistanı",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#101820"
        )
        baslik.pack(pady=15)

        # Ana alan
        ana_frame = tk.Frame(self.root, bg="#101820")
        ana_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Sol panel
        sol_panel = tk.Frame(ana_frame, bg="#17232e", bd=0, relief="flat")
        sol_panel.pack(side="left", fill="y", padx=(0, 15))

        # Sağ panel
        sag_panel = tk.Frame(ana_frame, bg="#17232e", bd=0, relief="flat")
        sag_panel.pack(side="right", fill="both", expand=True)

        # SOL PANEL BAŞLANGIÇ
        form_baslik = tk.Label(
            sol_panel,
            text="Kayıt Ekle",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#17232e"
        )
        form_baslik.pack(pady=(20, 15))

        self.kutu_etiket(sol_panel, "Ders Adı")
        self.ders_entry = self.giris_kutusu(sol_panel)

        self.kutu_etiket(sol_panel, "Doğru Sayısı")
        self.dogru_entry = self.giris_kutusu(sol_panel)

        self.kutu_etiket(sol_panel, "Yanlış Sayısı")
        self.yanlis_entry = self.giris_kutusu(sol_panel)

        self.kutu_etiket(sol_panel, "Konu (İsteğe Bağlı)")
        self.konu_entry = self.giris_kutusu(sol_panel)

        self.net_sonuc_label = tk.Label(
            sol_panel,
            text="Net: 0.00",
            font=("Arial", 14, "bold"),
            fg="#00d084",
            bg="#17232e"
        )
        self.net_sonuc_label.pack(pady=10)

        self.buton_olustur(sol_panel, "Net Hesapla", self.net_hesapla, "#1f6feb")
        self.buton_olustur(sol_panel, "Kaydı Ekle", self.kayit_ekle, "#00b894")
        self.buton_olustur(sol_panel, "Alanları Temizle", self.alanlari_temizle, "#fdcb6e")
        self.buton_olustur(sol_panel, "Seçili Kaydı Sil", self.secili_kaydi_sil, "#e17055")
        self.buton_olustur(sol_panel, "Tüm Kayıtları Sil", self.tum_kayitlari_sil, "#d63031")
        self.buton_olustur(sol_panel, "Bugün Ne Çalışayım?", self.oneri_uret, "#6c5ce7")

        # SAĞ PANEL BAŞLANGIÇ
        liste_baslik = tk.Label(
            sag_panel,
            text="Kayıtlar",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#17232e"
        )
        liste_baslik.pack(pady=(20, 10))

        liste_frame = tk.Frame(sag_panel, bg="#17232e")
        liste_frame.pack(fill="x", padx=20)

        self.listebox = tk.Listbox(
            liste_frame,
            width=90,
            height=17,
            font=("Consolas", 11),
            bg="#0d1117",
            fg="white",
            selectbackground="#1f6feb",
            selectforeground="white",
            bd=0,
            highlightthickness=0
        )
        self.listebox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(liste_frame, command=self.listebox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listebox.config(yscrollcommand=scrollbar.set)

        analiz_baslik = tk.Label(
            sag_panel,
            text="Analiz Paneli",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#17232e"
        )
        analiz_baslik.pack(pady=(20, 10))

        self.analiz_text = tk.Text(
            sag_panel,
            width=90,
            height=12,
            font=("Consolas", 11),
            bg="#0d1117",
            fg="#dfe6e9",
            bd=0,
            highlightthickness=0,
            wrap="word"
        )
        self.analiz_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def kutu_etiket(self, parent, text):
        label = tk.Label(
            parent,
            text=text,
            font=("Arial", 11, "bold"),
            fg="white",
            bg="#17232e"
        )
        label.pack(anchor="w", padx=20, pady=(8, 4))

    def giris_kutusu(self, parent):
        entry = tk.Entry(
            parent,
            font=("Arial", 12),
            width=28,
            bg="#0d1117",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        entry.pack(padx=20, pady=(0, 6), ipady=6)
        return entry

    def buton_olustur(self, parent, text, command, renk):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            bg=renk,
            fg="white",
            activebackground=renk,
            activeforeground="white",
            relief="flat",
            width=24,
            height=1,
            cursor="hand2"
        )
        btn.pack(pady=6, padx=20)

    def verileri_yukle(self):
        if os.path.exists(DOSYA_ADI):
            try:
                with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
                    self.veriler = json.load(dosya)
            except (json.JSONDecodeError, FileNotFoundError):
                self.veriler = []
        else:
            self.veriler = []

    def verileri_kaydet(self):
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            json.dump(self.veriler, dosya, ensure_ascii=False, indent=4)

    def net_hesapla_deger(self, dogru, yanlis):
        return dogru - (yanlis / 4)

    def net_hesapla(self):
        try:
            dogru = int(self.dogru_entry.get().strip())
            yanlis = int(self.yanlis_entry.get().strip())
            net = self.net_hesapla_deger(dogru, yanlis)
            self.net_sonuc_label.config(text=f"Net: {net:.2f}")
        except ValueError:
            messagebox.showerror("Hata", "Doğru ve yanlış alanlarına sayı gir.")

    def kayit_ekle(self):
        ders = self.ders_entry.get().strip()
        konu = self.konu_entry.get().strip()

        if not ders:
            messagebox.showwarning("Uyarı", "Ders adı boş olamaz.")
            return

        try:
            dogru = int(self.dogru_entry.get().strip())
            yanlis = int(self.yanlis_entry.get().strip())
        except ValueError:
            messagebox.showerror("Hata", "Doğru ve yanlış alanlarına sayı gir.")
            return

        if dogru < 0 or yanlis < 0:
            messagebox.showerror("Hata", "Negatif değer girilemez.")
            return

        net = self.net_hesapla_deger(dogru, yanlis)

        kayit = {
            "ders": ders,
            "konu": konu if konu else "-",
            "dogru": dogru,
            "yanlis": yanlis,
            "net": round(net, 2)
        }

        self.veriler.append(kayit)
        self.verileri_kaydet()
        self.listeyi_guncelle()
        self.analizi_guncelle()
        self.net_sonuc_label.config(text=f"Net: {net:.2f}")
        self.alanlari_temizle()
        messagebox.showinfo("Başarılı", "Kayıt eklendi.")

    def listeyi_guncelle(self):
        self.listebox.delete(0, tk.END)

        if not self.veriler:
            self.listebox.insert(tk.END, "Henüz kayıt yok.")
            return

        for i, kayit in enumerate(self.veriler, start=1):
            satir = (
                f"{i}. Ders: {kayit['ders']} | Konu: {kayit['konu']} | "
                f"Doğru: {kayit['dogru']} | Yanlış: {kayit['yanlis']} | Net: {kayit['net']:.2f}"
            )
            self.listebox.insert(tk.END, satir)

    def alanlari_temizle(self):
        self.ders_entry.delete(0, tk.END)
        self.dogru_entry.delete(0, tk.END)
        self.yanlis_entry.delete(0, tk.END)
        self.konu_entry.delete(0, tk.END)

    def secili_kaydi_sil(self):
        if not self.veriler:
            messagebox.showwarning("Uyarı", "Silinecek kayıt yok.")
            return

        secim = self.listebox.curselection()
        if not secim:
            messagebox.showwarning("Uyarı", "Listeden bir kayıt seç.")
            return

        index = secim[0]

        if index >= len(self.veriler):
            return

        silinen = self.veriler.pop(index)
        self.verileri_kaydet()
        self.listeyi_guncelle()
        self.analizi_guncelle()

        messagebox.showinfo(
            "Silindi",
            f"Silinen kayıt:\n{silinen['ders']} - Net: {silinen['net']:.2f}"
        )

    def tum_kayitlari_sil(self):
        if not self.veriler:
            messagebox.showwarning("Uyarı", "Zaten kayıt yok.")
            return

        cevap = messagebox.askyesno("Onay", "Tüm kayıtları silmek istediğine emin misin?")
        if cevap:
            self.veriler = []
            self.verileri_kaydet()
            self.listeyi_guncelle()
            self.analizi_guncelle()
            messagebox.showinfo("Temizlendi", "Tüm kayıtlar silindi.")

    def ders_bazli_istatistik(self):
        istatistik = {}

        for kayit in self.veriler:
            ders = kayit["ders"]

            if ders not in istatistik:
                istatistik[ders] = {
                    "dogru": 0,
                    "yanlis": 0,
                    "net_toplam": 0,
                    "adet": 0
                }

            istatistik[ders]["dogru"] += kayit["dogru"]
            istatistik[ders]["yanlis"] += kayit["yanlis"]
            istatistik[ders]["net_toplam"] += kayit["net"]
            istatistik[ders]["adet"] += 1

        return istatistik

    def analizi_guncelle(self):
        self.analiz_text.delete("1.0", tk.END)

        if not self.veriler:
            self.analiz_text.insert(tk.END, "Henüz analiz yapılacak veri yok.")
            return

        toplam_dogru = sum(k["dogru"] for k in self.veriler)
        toplam_yanlis = sum(k["yanlis"] for k in self.veriler)
        toplam_net = sum(k["net"] for k in self.veriler)

        en_iyi = max(self.veriler, key=lambda x: x["net"])
        en_zayif = min(self.veriler, key=lambda x: x["net"])

        istatistik = self.ders_bazli_istatistik()

        self.analiz_text.insert(tk.END, "GENEL ÖZET\n")
        self.analiz_text.insert(tk.END, "-" * 60 + "\n")
        self.analiz_text.insert(tk.END, f"Toplam Kayıt Sayısı : {len(self.veriler)}\n")
        self.analiz_text.insert(tk.END, f"Toplam Doğru       : {toplam_dogru}\n")
        self.analiz_text.insert(tk.END, f"Toplam Yanlış      : {toplam_yanlis}\n")
        self.analiz_text.insert(tk.END, f"Toplam Net         : {toplam_net:.2f}\n\n")

        self.analiz_text.insert(tk.END, "EN İYİ PERFORMANS\n")
        self.analiz_text.insert(
            tk.END,
            f"{en_iyi['ders']} | Konu: {en_iyi['konu']} | Net: {en_iyi['net']:.2f}\n\n"
        )

        self.analiz_text.insert(tk.END, "EN ZAYIF PERFORMANS\n")
        self.analiz_text.insert(
            tk.END,
            f"{en_zayif['ders']} | Konu: {en_zayif['konu']} | Net: {en_zayif['net']:.2f}\n\n"
        )

        self.analiz_text.insert(tk.END, "DERS BAZLI ORTALAMALAR\n")
        self.analiz_text.insert(tk.END, "-" * 60 + "\n")

        for ders, bilgi in istatistik.items():
            ortalama_net = bilgi["net_toplam"] / bilgi["adet"]
            self.analiz_text.insert(
                tk.END,
                f"{ders:<15} | Kayıt: {bilgi['adet']:<2} | "
                f"Toplam Doğru: {bilgi['dogru']:<3} | "
                f"Toplam Yanlış: {bilgi['yanlis']:<3} | "
                f"Ortalama Net: {ortalama_net:.2f}\n"
            )

    def oneri_uret(self):
        if not self.veriler:
            messagebox.showwarning("Uyarı", "Öneri için önce kayıt ekle.")
            return

        istatistik = self.ders_bazli_istatistik()

        ortalamalar = []
        for ders, bilgi in istatistik.items():
            ortalama_net = bilgi["net_toplam"] / bilgi["adet"]
            ortalamalar.append((ders, ortalama_net))

        ortalamalar.sort(key=lambda x: x[1])

        en_zayif_ders = ortalamalar[0][0]
        en_iyi_ders = ortalamalar[-1][0]

        oneri = ""

        if en_zayif_ders.lower() == "matematik":
            oneri = (
                "Bugün odağı Matematik yap.\n"
                "- Problem çöz\n"
                "- Temel işlem hatalarını kontrol et\n"
                "- 20-30 soru tekrar at\n"
            )
        elif en_zayif_ders.lower() == "türkçe":
            oneri = (
                "Bugün odağı Türkçe yap.\n"
                "- Paragraf çöz\n"
                "- Dil bilgisi tekrar et\n"
                "- Hız + dikkat çalış\n"
            )
        elif en_zayif_ders.lower() == "fizik":
            oneri = (
                "Bugün odağı Fizik yap.\n"
                "- Konu özeti çıkar\n"
                "- Formülleri tekrar et\n"
                "- Kolay-orta seviye soru çöz\n"
            )
        elif en_zayif_ders.lower() == "kimya":
            oneri = (
                "Bugün odağı Kimya yap.\n"
                "- Kavram eksiğini kapat\n"
                "- Ezber noktaları not al\n"
                "- 20 soru çöz\n"
            )
        elif en_zayif_ders.lower() == "biyoloji":
            oneri = (
                "Bugün odağı Biyoloji yap.\n"
                "- Konuyu okuyup kendine anlat\n"
                "- Şema çıkar\n"
                "- Kısa testlerle pekiştir\n"
            )
        else:
            oneri = (
                f"Bugün odağı {en_zayif_ders} yap.\n"
                "- Eksik konuya dön\n"
                "- Önce konu tekrarı\n"
                "- Sonra orta seviye soru çöz\n"
            )

        mesaj = (
            f"Worldscirpt AI Önerisi\n\n"
            f"En zayıf dersin: {en_zayif_ders}\n"
            f"En iyi dersin: {en_iyi_ders}\n\n"
            f"{oneri}\n"
            f"Bugün ana saldırı dersin: {en_zayif_ders}"
        )

        messagebox.showinfo("Bugün Ne Çalışayım?", mesaj)


if __name__ == "__main__":
    root = tk.Tk()
    app = WorldscirptAIYKS(root)
    root.mainloop()