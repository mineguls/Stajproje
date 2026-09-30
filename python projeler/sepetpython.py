sepet = [
    {"ad": "ayakkabi", "fiyat": "250"},
    {"ad": "corap", "fiyat": "30"},
    {"ad": "tisort", "fiyat": "90"},
    {"ad": "ceket", "fiyat": "400"},
    {"ad": "sapka", "fiyat": "75"},
    {"ad": "pantolon", "fiyat": "150"}
]

filtrelenmis_urunler = filter(lambda urun: float(urun["fiyat"]) > 100, sepet)

kdvli_sepet = map(lambda urun: {
    "ad": urun["ad"],
    "fiyat": round(float(urun["fiyat"]) * 1.1, 2)
}, filtrelenmis_urunler)

print("100tl uzeri urunler")
for urun in kdvli_sepet:
    print(f"urun:{urun['ad']} kdv dahil fiyat: {urun['fiyat']}TL")