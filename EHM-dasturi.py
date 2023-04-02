
"""
EHM dasturi 


>> Tayyorlangan yangi qoziqli barabandan olingn tahlil natijalar:
"""
#Paxtaning namligini  quyidagi formula yordamida topamiz:
    
a_natija = int(input("Namunaning quritishdan oldingi massasi kiriting ? \n>>> "))
# a bu ixtiyoriy o'zgaruvchi 
b_natija = float(input("Birinchi namunaning quritishdan keyingi massasini kiriting ?\n>>> "))

ikki_natija = float(input("Ikkinchi namunaning quritishdan keyingi massasini kiriting ?\n>>> "))

uch_natija = float(input("Uchinchi namunaning quritishdan keyingi massasini kiriting ?\n>>> "))
# b bu ham ixtiyoriy o'zgaruvchi 
hisob = a_natija-b_natija

hisob2 = a_natija-ikki_natija

hisob3 = a_natija-uch_natija

w_bolinmasi = hisob/b_natija

w2_bolinmasi = hisob2/ikki_natija

w3_bolinmasi = hisob3/uch_natija

W1_qiymati = w_bolinmasi*100-0.6

W2_qiymat = w2_bolinmasi*100-0.6

W3_qiymat = w3_bolinmasi*100-0.6

middle = W1_qiymati+W2_qiymat+W3_qiymat

natijaW = middle/3

# check = (f"Birinchini namunaning qiymat {W1_qiymati} % ga teng \n"
#        f"Ikkinchi namunaning qiymat {W2_qiymat} % ga teng \n"
#       f"Uchinchini namunaning qiymat {W3_qiymat} % ga teng \n"
#        )
check1 = (f"O'rtacha namlik: W = {natijaW} % teng")   

check = check1

print(check) 



