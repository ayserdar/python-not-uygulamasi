def not_ekle():
    not_yazisi = input("Notunu yaz: ")
    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(not_yazisi + "\n")
    print("Not kaydedildi.")


def notlari_goster():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()

        if len(notlar) == 0:
            print("Hiç not yok.")
        else:
            print("\n--- NOTLAR ---")
            for i, not_ in enumerate(notlar, 1):
                print(f"{i}- {not_.strip()}")

    except FileNotFoundError:
        print("Henüz not yok.")


def not_sil():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()

        if len(notlar) == 0:
            print("Silinecek not yok.")
            return

        print("\n--- NOTLAR ---")
        for i, not_ in enumerate(notlar, 1):
            print(f"{i}- {not_.strip()}")

        sil = input("Silmek istediğin numara: ")

        if not sil.isdigit():
            print("Lütfen sayı gir.")
            return

        sil = int(sil)

        if 1 <= sil <= len(notlar):
            notlar.pop(sil - 1)

            with open("notlar.txt", "w", encoding="utf-8") as dosya:
                dosya.writelines(notlar)

            print("Not silindi.")
        else:
            print("Geçersiz numara!")

    except FileNotFoundError:
        print("Hiç not yok.")


while True:
    print("\n--- NOT SİSTEMİ ---")
    print("1- Not ekle")
    print("2- Notları göster")
    print("3- Not sil")
    print("4- Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        not_ekle()

    elif secim == "2":
        notlari_goster()

    elif secim == "3":
        not_sil()

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim!")