def bubble_sort(liste, siralama="artan"):
    n = len(liste)
    for i in range(n):
        # Erken çıkış optimizasyonu
        degisim = False
        for j in range(0, n - i - 1):
            # Sıralama yönüne göre karşılaştırma
            if (siralama == "artan" and liste[j] > liste[j + 1]) or (siralama == "azalan" and liste[j] < liste[j + 1]):
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                degisim = True
        # Eğer hiçbir değişiklik olmadıysa, döngüyü erken bitir
        if not degisim:
            break
    return liste

# Örnek kullanım
sayilar = [64, 34, 25, 12, 22, 11, 90]
print("Sıralanmamış Liste:", sayilar)

# Artan sıralama
sirali_liste_artan = bubble_sort(sayilar, siralama="artan")
print("Artan Sıralı Liste:", sirali_liste_artan)

# Azalan sıralama
sirali_liste_azalan = bubble_sort(sayilar, siralama="azalan")
print("Azalan Sıralı Liste:", sirali_liste_azalan)
