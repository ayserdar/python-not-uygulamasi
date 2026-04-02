while True:
    print("\n--- YKS TAKİP SİSTEMİ ---")
    print("1- Çalışma ekle")
    print("2- Kayıtları göster")
    print("3- Kayıt sil")
    print("4- Toplam soru ve saat göster")
    print("5- Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        ders = input("Ders adı: ")
        soru = input("Kaç soru çözdün: ")
        sure = input("Kaç saat çalıştın: ")

        with open("yks_kayitlari.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{ders},{soru},{sure}\n")

        print("Kayıt eklendi.")

    elif secim == "2":
        try:
            with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
                kayitlar = dosya.readlines()

            if len(kayitlar) == 0:
                print("Henüz kayıt yok.")
            else:
                print("\n--- KAYITLAR ---")
                for i, kayit in enumerate(kayitlar, 1):
                    ders, soru, sure = kayit.strip().split(",")
                    print(f"{i}- Ders: {ders} | Soru: {soru} | Süre: {sure} saat")

        except FileNotFoundError:
            print("Henüz kayıt dosyası oluşmamış.")

    elif secim == "3":
        try:
            with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
                kayitlar = dosya.readlines()

            if len(kayitlar) == 0:
                print("Silinecek kayıt yok.")
            else:
                print("\n--- KAYITLAR ---")
                for i, kayit in enumerate(kayitlar, 1):
                    ders, soru, sure = kayit.strip().split(",")
                    print(f"{i}- Ders: {ders} | Soru: {soru} | Süre: {sure} saat")

                sil = input("Silmek istediğin kayıt numarası: ")

                if sil.isdigit():
                    sil = int(sil)

                    if 1 <= sil <= len(kayitlar):
                        kayitlar.pop(sil - 1)

                        with open("yks_kayitlari.txt", "w", encoding="utf-8") as dosya:
                            dosya.writelines(kayitlar)

                        print("Kayıt silindi.")
                    else:
                        print("Geçersiz numara.")
                else:
                    print("Lütfen sayı gir.")

        except FileNotFoundError:
            print("Henüz kayıt yok.")

    elif secim == "4":
        try:
            with open("yks_kayitlari.txt", "r", encoding="utf-8") as dosya:
                kayitlar = dosya.readlines()

            toplam_soru = 0
            toplam_sure = 0

            for kayit in kayitlar:
                ders, soru, sure = kayit.strip().split(",")
                toplam_soru += int(soru)
                toplam_sure += float(sure)

            print(f"Toplam soru: {toplam_soru}")
            print(f"Toplam süre: {toplam_sure} saat")

        except FileNotFoundError:
            print("Henüz kayıt yok.")

    elif secim == "5":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim!")