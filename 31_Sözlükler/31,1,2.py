telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz" : "0533 533 33 33",
                   "eda ala"  : "0212 212 12 12"}


kişi=input("Telefon numarasını öğrenmek istediğiniz kişinin adını girin: ")
cevap="{} adlı kişinin telefon numarası: {}"

if kişi in telefon_defteri:
    print(cevap.format(kişi,telefon_defteri[kişi]))
else:
    print("Aradığınız kişi yok")