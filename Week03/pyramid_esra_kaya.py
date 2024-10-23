def calculate_pyramid_height(kup_sayisi):
    if kup_sayisi <= 0:
        return "Küp sayısı sıfırdan büyük olmalıdır."
    
    toplam_kup = 0
    yukseklik = 0
    
    while toplam_kup < kup_sayisi:
        yukseklik += 1
        toplam_kup += yukseklik
        
        if toplam_kup == kup_sayisi:
            return yukseklik
    
    # Eğer toplam_kup, kup_sayisi'ni aşarsa bu piramit oluşturulamaz.
    return "Bu küp sayısıyla bir piramit oluşturulamaz."
