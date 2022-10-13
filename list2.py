text = "PYTHON"
textList = list(text) # Metinden liste oluşturuldu.
print(textList)

arabalar = list() # Boş liste
arabalar.append("BMW") # Listeye ekleme yaptı
arabalar += ["Bugatti"] # 2. listeye ekleme yöntemi

# 1. kötü yol
arabalar[1] = 1500000
arabalar.append("Bugatti")
arabalar.append(10000000)
arabalar.append("Audi")
arabalar.append(5000000)
arabalar.append("Porsche")
arabalar.append(7000000)
# 1. kötü yol


arabalar.remove("Audi")
arabalar.remove(5000000)

arabalar[4] = "Renault"
arabalar[5] = 200000

print(arabalar)


# Renault değerini ve fiyatını bir değişkene atayarak listeden çkarınız.

marka = arabalar.pop(4) # Pop Index değerine göre listeden veriyi alır ve siler.
fiyat = arabalar.pop(4) # 4. Index çekilince 5. Index 4. ye kaymış oldu
print("{} markalı araba {} fiyatlı araba satıştan kaldırıldı.".format(marka,fiyat))

