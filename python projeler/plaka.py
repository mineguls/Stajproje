plaka=[
    [65,80],
    [55,90]
]
toplam=plaka[0][0]+plaka[0][1]+plaka[1][0]+plaka[1][1]
print("Toplam Savunma:", toplam)

zayif=min(plaka[0][0],plaka[0][1],plaka[1][0],plaka[1][1])
print("En zayıf nokta:",zayif)


guclu=max(plaka[0][0],plaka[0][1],plaka[1][0],plaka[1][1])
print("En güçlü nokta:",guclu)


transpoz=[
    [plaka[0][1],plaka[1][0]],
    [plaka[1][0],plaka[1][1]]
]
print("TRANSPOZ:-----------------------------------------------------------------")
print(transpoz[0])
print(transpoz[1])



plaka[1][0] = 75

print("Yeni plaka:([0][0] güncellendi)-------------------------------------------")
print(plaka)
