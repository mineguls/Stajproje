# 5 adet sayı saklamak için boş bir liste oluşturuyoruz
sayilar = []

print("Lütfen 5 adet sayı giriniz:")

# Kullanıcıdan 5 kez sayı almak için döngü kuruyoruz
for i in range(5):
    sayi = float(input(f"{i + 1}. sayıyı girin: "))
    sayilar.append(sayi) # Girilen sayıyı listeye ekliyoruz

# Listede toplanan sayıların ortalamasını hesaplıyoruz
ortalama = sum(sayilar) / len(sayilar)

# Sonuçları ekrana yazdırıyoruz
print("\n--- SONUÇLAR ---")
print(f"Girdiğiniz sayılar: {sayilar}")
print(f"Sayıların ortalaması: {ortalama:.2f}")