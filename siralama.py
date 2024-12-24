def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        # Son i eleman zaten sıralı olduğu için iç döngüyü buna göre kısaltıyoruz
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Elemanları yer değiştir
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# Örnek kullanım
sayilar = [64, 34, 25, 12, 22, 11, 90]
print("Sıralanmamış Liste:", sayilar)

sirali_liste = bubble_sort(sayilar)
print("Sıralanmış Liste:", sirali_liste)
