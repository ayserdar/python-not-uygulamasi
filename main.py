import os

dosya_adi = "kullanici.txt"

# Eğer kayıt yoksa ilk kayıt oluştur
if not os.path.exists(dosya_adi):
    print("İlk kayıt oluşturuluyor.")
    yeni_kullanici = input("Yeni kullanıcı adını gir: ")
    yeni_sifre = input("Yeni şifreni gir: ")

    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write(yeni_kullanici + "\n")
        dosya.write(yeni_sifre)

    print("Kayıt başarıyla oluşturuldu!")
else:
    print("Kayıt bulundu, giriş yap.")

# Kayıtlı bilgileri oku
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()
    kayitli_kullanici = satirlar[0].strip()
    kayitli_sifre = satirlar[1].strip()

# Giriş yap
while True:
    kullanici = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")

    if kullanici == kayitli_kullanici and sifre == kayitli_sifre:
        print("Giriş başarılı!")
        break
    else:
        print("Hatalı, tekrar dene")