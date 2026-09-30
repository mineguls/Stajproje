print("Görev tamamlandı ! skorlar belirlendi")

puanList = [
    ["arin", 85],
    ["boran", 120],
    ["ceyla", 95],
    ["mert", 110],
    ["ekin", 78]
]


gununBirincisi=max(puanList, key=lambda x: x[1])
print("\n Günün birincisi:")
print("-" * 40)
print( gununBirincisi)

skorOrt=float(sum(x[1] for x in puanList)/ len(puanList))
print("\n ORTALAMA SKOR")
print("-" * 40)
print(f"Ortalama : {skorOrt:.2f}")



print("-"*40)

skorSiralama=sorted(puanList, key=lambda x: x[1] ,reverse=True)


for sira, oyuncu in enumerate(skorSiralama, start=1):
    
    print(f"{sira}. {oyuncu[0]} → {oyuncu[1]} ")

ceylaSkor=puanList[2][1] + 20
print("ceyla skor: ",ceylaSkor)

newList=list(filter(lambda x: x[1]> 100,puanList)) 
print("\n 100 üzerinde alanlar:",newList)