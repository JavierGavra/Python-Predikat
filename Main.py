# @Copyright by JARGON

print("====================")
print("      Predikat")
print("====================")

while True:
    nilai = int(input("\nMasukkan nilai mu = "))
    if (nilai <= 100 and nilai >= 90):
        print("Predikat A")
    elif (nilai <= 89 and nilai >= 74):
        print("Predikat B")
    elif (nilai <= 73 and nilai >= 60):
        print("Predikat C")
    elif (nilai <= 59 and nilai >= 0):
        print("Predikat D")
    else:
        print("Masukkan nilai yang benar!!!")
        continue
    
    print("\nIngin mengulangi program?")
    ulang = str(input("(y/n) = "))
    if ulang == 'y':
        continue
    elif ulang == 'n':
        break
    else:
        print("Lain kali kalo ditanya yg bener!!!")
        break



print("\n#Program selesai")