# # # # #?? ---CLASS 14.1-----
# # # # #
# # # # # for loop
# # # # #
# # # # fruits = ['apple' , 'orange' , 'frange' , 'arange' , 'krange']
# # # # for fruit in fruits: # akane ja hoise, for likhe variable er short name nite hobe terpor in diye variable dite hobe
# # # #     print(f'{fruit} I want to eat') # akane print hobe [apple i want to eat, ai vabe sobgulo print hobe]
# # # #
# # # # break and continue er baboher
# # # #  ??? (continue er baboher)
# # #
# # # # fruits = ['apple' , 'orange' , 'frange' , 'arange' , 'krange']
# # # # for fruit in fruits:
# # # #     if fruit == 'orange': # akane jadi cai orange bad diye baki sob print hok tahole ai vabe lekhte hobe
# # # #         continue
# # # #     print(f'{fruit} I want to eat') # akane orange bad diye baki sob print hobe
# # # #
# # # #  ??? (break er baboher)
# # # fruits = ['apple' , 'orange' , 'frange' , 'arange' , 'krange']
# # # for fruit in fruits:
# # #     if fruit == 'frange':
# # #         break   # space gulo tik mato dite come
# # #     print(f'{fruit} I want to eat') # ami cassi frange porjonto print hok tahole (break) baboher korte hobe
# #
#
# # ??  r akti for er example
# # numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20,233,46645,625645,67]
# #
# # !! for n in numbers:  je sonka ke vag korle kon vagses takena take (even number bole) jetai vagses thake take (odd number bole)
# # !!    if n % 2 == 0:    (akahe cassi numbers er je sonka evan and odd number ta ber korte)
# #         print(f'{n} is a even number')
# # #    else:
# # #       print(f'{n} is a odd number')
#
# # !! ami cassi (numbers a koita evan and odd number ta ber korte)
#
# numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20,233,46645,625645,67]
# even = 0
# odd = 0
# for n in numbers:
#     if n % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print(f' total {even} even number and {odd} odd number')

# # !! ami cassi 0 to 6 porjonto print hote but 3 and 6 print hobe na (ata korbo while loop diye)
# i = 0
# while i <= 6:
#     if (i == 3 or i == 6):
#         i += 1
#         continue
#     print(i)
#     i += 1

# !! ami cassi 13 and 16 print hobe na (ata korbo for loop diye)
# ?? (for loop diye kora sahoj)
numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20,233,46645,625645,67]
for n in numbers:
    if (n == 13 or n == 16):
        continue
    print(n)


    #!!!! odaharon diya halo

