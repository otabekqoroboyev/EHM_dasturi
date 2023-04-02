"""Paxtaning iflosligini aniqlaymiz:"""
answer = float(input("Paxta namunasining vazni kiriting ? \n>>> "))

answer_small = float(input("Birinchi namuna uchun ajratilgan mayda ifloslik vazni kiriting ? \n>>> "))

answer_big = float(input("Birinchi namuna uchun ajiratilgan yirik ifloslikni vazni kiriting ? \n>>> "))

answer_small1 = float(input("Ikkinchi namuna uchun ajratilgan mayda ifloslik vazni kiriting ? \n>>> "))

answer_big1 = float(input("Ikkinchi namuna uchun ajiratilgan yirik ifloslikni vazni kiriting ? \n>>> "))

answer_small2 = float(input("Uchinchi namuna uchun ajratilgan mayda ifloslik vazni kiriting ? \n>>> "))

answer_big2 = float(input("Uchinchi namuna uchun ajiratilgan yirik ifloslikni vazni kiriting ? \n>>> "))


K_1 = 1.0
k_2 = 0.98
#natija birinchi namuna uchun
result_small = (answer_small*100*K_1*k_2)/answer
result_big = (answer_big*100*k_2)/answer
plus = result_small+result_big

#natija ikkinchi namuna uchun
result_small1 = (answer_small1*100*K_1*k_2)/answer
result_big1 = (answer_big*100*k_2)/answer
plus1 = result_small1+result_big1

#natija uchinchi namuna uchun
result_small2 = (answer_small2*100*K_1*k_2)/answer
result_big2 = (answer_big*100*k_2)/answer
plus2 = result_small2+result_big2

#umumiy natija 
mayda_if = (result_small+result_small1+result_small2)/3
yirik_if = (result_big+result_big1+result_big2)/3
Umumiy_if = (plus+plus1+plus2)/3


print(f'Namuna - 1: mayda ifloslik natijasi: {result_small} % \n'
      f'Namuna - 1: yirik ifloslik natijasi: {result_big} % \n'
      f'Namuna - 1: umumiy ifloslik natijasi: {plus} % \n')
if plus>=14:
    print(f'Umumiy ifloslik darajasi yuqori bu ikkinchi   sortga kiradi')      
print("O'rtacha umumiy massasi \n"
      f"Mayda ifloslik: I = {mayda_if} % \n"
      f"Yirik ifloslik: I = {yirik_if} % \n"
      f"Umumiy ifloslik: I = {Umumiy_if} % ")