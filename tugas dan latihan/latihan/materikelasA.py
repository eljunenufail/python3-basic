# kegabutan masa belajar
print("hello world")
x = 10 * 20
y = 20 / 100
#operator += (y = y + 10)
y += 10
#operator -= (x = x - 20)
x -= 20
print(x , y)
# input dari user 
nilaiUmur = input ("bberapa umur kamu? ")
print ("umurKamu" , nilaiUmur, "tahun")
#if - else statement
# if (jika terpenuhi) else (jika tidak terpeuhi)
# operator pembanding = ==, <, >, !=, 

if (nilaiUmur =="25"):
    print ("ketuaan lu bangsat")
elif (nilaiUmur == "15"):
    print ("terlalu muda lu dek")
else:
    print ("umur nya cukup aja") 

# operator != tidak sama dengan) 
kelasSyahid = "A"
statusKelasSyahid = "A" != kelasSyahid
print ("status kelas syahid:", statusKelasSyahid)
if ("kelas A") == True:
    print ("selamat datang di kelas A")
else: 
    print ("maaf kamu salah masuk kelas")








#opertor > (lebih besar) < (lebih kecil)
#sistem perinngkat A ( 90 - 100), B (80 - 89), C (70 - 79), D (selainnya)
nilaiUjian = 1030
print ("nilai ujian:", nilaiUjian)

if (nilaiUjian >= 90 and nilaiUjian <= 100):
    print ("nilai kamu lulus dengan peringkat A")
elif (nilaiUjian >= 80 and nilaiUjian < 89):
    print ("nilai kamu lulus dengan peringkat B")
else:
    print ("nilai kamu tidak lulus dengan perinngkat D")
# string indxing
kata = "belajar"
print("kata [0] ")


