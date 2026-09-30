from datetime import datetime, timedelta

def kutuphane_hesaplama():
    print("--- Kütüphane Kitap Teslim ve Ceza Hesaplama Sistemi ---")
    
    kullanici_adi = input("Kullanıcı Adı: ")
    kitap_adi = input("Kitap Adı: ")
    alim_tarihi_str = input("Kitap Alım Tarihi (GG.AA.YYYY formatında giriniz): ")
    
    try:
        alim_tarihi = datetime.strptime(alim_tarihi_str.strip(), "%d.%m.%Y")
    except ValueError:
        print("Hatalı tarih formatı! Lütfen GG.AA.YYYY şeklinde tekrar deneyin.")
        return

    teslim_suresi_gun = 14
    teslim_tarihi = alim_tarihi + timedelta(days=teslim_suresi_gun)
    
    # bugun değişkeni burada açıkça tanımlanıyor
    bugun = datetime.now()
    
    print("\n--- Sonuçlar ---")
    print(f"Kullanıcı: {kullanici_adi}")
    print(f"Kitap: {kitap_adi}")
    print(f"Kitap Alım Tarihi: {alim_tarihi.strftime('%d.%m.%Y')}")
    print(f"Normal Teslim Tarihi: {teslim_tarihi.strftime('%d.%m.%Y')}")
    
    if bugun > teslim_tarihi:
        gecen_gun = (bugun - teslim_tarihi).days
        ceza = gecen_gun * 2.50
        print(f"\nDurum: Teslim süresi {gecen_gun} gün geçmiş!")
        print(f"Uygulanan Toplam Ceza Tutarı: {ceza:.2f} TL")
    else:
        kalan_gun = (teslim_tarihi - bugun).days
        print(f"\nDurum: Kitabın teslimine {kalan_gun} gün kaldı.")
        print("Ceza Yok (0.00 TL)")

if __name__ == "__main__":
    kutuphane_hesaplama()