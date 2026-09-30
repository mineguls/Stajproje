# Yemek listesi (Sözlük yapısı kullanarak indeks kargaşasını önledik)
yemekler = [
    {"ad": "İskender", "kalori": 850, "fiyat": 280.00},
    {"ad": "Mercimek Çorbası", "kalori": 180, "fiyat": 70.00},
    {"ad": "Tavuklu Pilav", "kalori": 650, "fiyat": 150.00},
    {"ad": "Salata", "kalori": 120, "fiyat": 90.00},
    {"ad": "Mantı", "kalori": 750, "fiyat": 220.00},
    {"ad": "Lahmacun", "kalori": 450, "fiyat": 80.00}
]

# 1. Normal (Tüm) Yemek Listesi
print("--- TÜM YEMEKLER LİSTESİ ---")
for yemek in yemekler:
    print(f"Yemek: {yemek['ad']:<15} | Kalori: {yemek['kalori']:>4} kcal | Fiyat: {yemek['fiyat']:>6.2f} TL")

# 2. 600 kaloriden fazla olanları filtrele ve fiyata göre sırala
filtrelenmis = sorted([y for y in yemekler if y["kalori"] > 600], key=lambda y: y["fiyat"])

# 3. Filtrelenmiş ve uyarılı liste
print("\n--- 600 KALORİDEN FAZLA OLANLAR (Fiyata Göre Sıralı) ---")
for yemek in filtrelenmis:
    print(f"Yemek: {yemek['ad']:<15} | Kalori: {yemek['kalori']:>4} kcal | Fiyat: {yemek['fiyat']:>6.2f} TL ⚠️ [YÜKSEK KALORİ]")