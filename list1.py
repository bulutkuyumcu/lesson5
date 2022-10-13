ornekListe = [2,4,7,5.5,"Python"] # String, float veya int gibi farklı tipleri ekeyebilirz.
print(ornekListe)

# başlangıç index : biriş index . atlama değeri :
# Indexler 0 1 2 3 veya -1 -2 -3
print(ornekListe[2])
print(ornekListe[2:4])
print(ornekListe[0:5:4])
print(ornekListe[2:])
print(ornekListe[::])
print(ornekListe[::-1])

for i in ornekListe:
    if str == type(i):
        print("bu eleman stringdir",i)
    elif int == type(i):
        print("bu eleman inttir",i)
    else:
        print("bu eleman floattır",i)

# arabalar = []
# arabalar = list()