

from datetime import datetime

print("-----Doğum Günü Geri sayım uygulaması----")
gun=int(input("doğduğunuz günü girin:"))

ay=int(input("doğduğunuz ayı girin(sayı olarak):"))
bugun=datetime.today().date()

dogumgunu=datetime(bugun.year,ay,gun).date()
kalan_gun=(dogumgunu-bugun).days
print("------------------------------------------------------------")
if kalan_gun==0:
 print ("TEBRİKLER")

else:
 print(f"dogum gununuze {kalan_gun} gün kaldı")