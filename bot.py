import firebase_admin
from firebase_admin import credentials, firestore
import re

# 1. Firebase Bağlantısı
# Dosya adının klasördekiyle aynı olduğundan emin ol!
cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. Veri (Siteden kopyaladığın metni buraya koyuyoruz)
raw_data = """
11.05.2026
Pazartesi
🍽️
Etli nohut
285 Kalori
🍽️
Meyhane Pilavı
300 Kalori
🍽️
Turşu
10 Kalori
🍽️
Taş kadayıf
305 Kalori
Toplam: 900 Kalori
12.05.2026
Salı
🍽️
Kremalı Brokoli Çorbası
-
🍽️
Tavuk But
158 Kalori
🍽️
Soslu Makarna
337 Kalori
🍽️
Salata
90 Kalori
Toplam: 585 Kalori
13.05.2026
Çarşamba
🍽️
Hanımağa Çorbası
280 Kalori
🍽️
Patlıcan Musakka
145 Kalori
🍽️
Pirinç Pilavı
326 Kalori
🍽️
Cacık
45 Kalori
Toplam: 796 Kalori
14.05.2026
Perşembe
🍽️
Domates Çorbası
163 Kalori
🍽️
Kuru köfte+Cips
350 Kalori
🍽️
Bulgur Pilavı
291 Kalori
🍽️
Mevsim Meyvesi
90 Kalori
Toplam: 894 Kalori
15.05.2026
Cuma
🍽️
Mercimek Çorbası
184 Kalori
🍽️
Lahmacun
525 Kalori
🍽️
Salata
90 Kalori
🍽️
Şalgam
-
Toplam: 799 Kalori
18.05.2026
Pazartesi
🍽️
Tas Kebabı
348 Kalori
🍽️
Pirinç Pilavı
326 Kalori
🍽️
Yoğurt
122 Kalori
🍽️
Kemalpaşa tatlı
164 Kalori
Toplam: 960 Kalori
20.05.2026
Çarşamba
🍽️
Etli Sulu Patates
-
🍽️
Dövme Pilavı
178 Kalori
🍽️
Yoğurt
122 Kalori
🍽️
Mevsim Meyvesi
90 Kalori
Toplam: 390 Kalori
21.05.2026
Perşembe
🍽️
Kremalı mısır çorba
163 Kalori
🍽️
Tavuk Döner
150 Kalori
🍽️
Pirinç Pilavı
326 Kalori
🍽️
Salata
90 Kalori
Toplam: 729 Kalori
22.05.2026
Cuma
🍽️
Mercimek Çorbası
184 Kalori
🍽️
Karışık dolma
250 Kalori
🍽️
Yoğurt
122 Kalori
🍽️
Aşure
344 Kalori
Toplam: 900 Kalori
25.05.2026
Pazartesi
🍽️
Etli Bezelye
309 Kalori
🍽️
Mercimekli bulgur pilavı
291 Kalori
🍽️
Yoğurt
122 Kalori
🍽️
Tel Kadayıf
-
Toplam: 722 Kalori
"""

def process_and_upload(text):
    # Gün bazlı bölme
    days = re.split(r'(\d{2}\.\d{2}\.\d{4})', text)
    
    for i in range(1, len(days), 2):
        date_str = days[i].strip()
        content = days[i+1]
        
        # Yemekleri ve kalorileri ayıkla
        items = re.findall(r'🍽️\n(.*?)\n', content)
        calories = re.findall(r'([\d-]+)\s*Kalori', content)
        
        # Toplam kaloriyi bul
        total_cal_match = re.search(r'Toplam:\s*(\d+)', content)
        total_calorie = int(total_cal_match.group(1)) if total_cal_match else 0

        # Tarihi YYYY-MM-DD formatına çevir (Doküman ID'si için)
        d, m, y = date_str.split('.')
        doc_id = f"{y}-{m}-{d}"

        meal_data = {
            "date": date_str,
            "items": items,
            "calories": calories,
            "total_calorie": total_calorie
        }

        # Firestore'a Kaydet
        db.collection("meals").document(doc_id).set(meal_data)
        print(f"Başarıyla yüklendi: {date_str}")

# Fonksiyonu çalıştır
process_and_upload(raw_data)