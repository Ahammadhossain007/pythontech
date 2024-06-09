# # # # #Funtion niye alocona
# # # # def ami_tumi(number):          # !! first a (def nite hobe)# terpor (Funtion) name diye hobe
# # # #     if number % 2 == 0:
# # # #         return (f'{number} is an even number')  ! akahe return likhe ki dekhabe ta ta bole dite hoi
# # # #     else:
# # # #         return (f'{number} is an odd number')
# # # # numbers = ami_tumi(77) ! akahen naton vaiable(numbers) niye opro er (ami_tumi(77)) variable a ki thakbe jemon (77) bole diaci
# # # #                          ! opor er ami tumi variable niye main kaj
# # # # print(numbers)
# # # #
# # # # !!! aro odaharo!!
# # # #
# # # # নিশ্চয়ই! আপনি যে কোড স্নিপেটটি দিয়েছেন তা একটি পাইথন ফাংশন ডেফিনিশনের শুরু।
# # # # এখানে def হল পাইথনের একটি কীওয়ার্ড যা একটি ফাংশন ডেফিন করার জন্য ব্যবহৃত হয়।
# # # # ami_tumi হল ফাংশনের নাম, এবং number হল একটি প্যারামিটার যা ফাংশনের মধ্যে ব্যবহার করা হবে।
# # # #
# # # # এই ফাংশনটি কি করে তা বুঝতে গেলে আমাদের ফাংশনের বডি দেখতে হবে,
# # # # যা কোলন (:) চিহ্নের পরে আসে। তবে আপনি শুধু ফাংশন হেডারটি দিয়েছেন,
# # # # ফাংশন বডি নয়। একটি সম্পূর্ণ ফাংশন ডেফিনিশনের জন্য আমাদের ফাংশন বডি প্রয়োজন,
# # # # যেখানে আমরা কোড লিখব যা ফাংশনটি কল করা হলে কার্যকর হবে।
# # # #
# # # # এখানে একটি সম্পূর্ণ ফাংশনের উদাহরণ দেওয়া হল:
# # # #
# # # # # একটি সহজ ফাংশন ডেফিনিশন
# # # # def ami_tumi(number):
# # # # return number * 2  # ইনপুট নাম্বারটিকে দ্বিগুণ করে
# # # #
# # # # # ফাংশন কল করা
# # # # result = ami_tumi(5)
# # # # print(result)  # এটি প্রিন্ট করবে: 10
# # # #
# # # # এই উদাহরণে, ami_tumi ফাংশনটি একটি প্যারামিটার number নেয় এবং এটিকে দ্বিগুণ করে ফলাফল হিসেবে রিটার্ন করে।
# # # #
# # # # !! aro akti use
# # # def message_dibo(first_name, last_name):
# !    msg = f'Hello, {first_name} {last_name} ami tomake valobashi' ! (msg) akti bariable ja niche (return) a diacci,
# # #     return msg     !! (msg) ai variable na niye (return) er por direct [f'Hello, {first_name} {last_name} ami tomake valobashi'] ata diya jabe
# # # mess1 = message_dibo(first_name= 'Ahammad' , last_name= 'Hossain')
# # # mess2 = message_dibo(first_name= 'Sujona' , last_name= 'Hossain')
# # # print(mess1)
# # # !! Output ja dekhabe: Hello, Ahammad Hossain ami tomake valobashi
# #
# #
# # # !! aro akti baboher (ami cassi duita sunka jog korte)
# def number_jog(first_number, second_number):
#     jog_karo = first_number + second_number
#     return jog_karo
# number1 = number_jog(first_number=20, second_number=30)
# number2 = number_jog(first_number=50, second_number=40)
# print(number1)
# ## Output ja dekhabe: 50
#
# #
# # #!!  aro akti baboher
# # def bio(name, sex, age):
# #     # !!suro   (ai colun er vitor  ja ase take bole [Docstring], 3 ta (colon) dile ata ase, akhane bistarito bonnona kore
# #     """
# #     :param name:
# #     :param sex:
# #     :param age:
# #     :return:
# #     """
# #     # !! Ses
# #     if sex == 'male':
# #         gender = 'He'
# #     else:
# #         gender = 'She'
# #     ja_dehabe = f'{name} is a actor. {gender} is {age} years old'
# #     return ja_dehabe
# # bio1 = bio(name='Sharukh khan', age= 25, sex='male')
# # bio2 = bio(name='karina khan', age= 30, sex='female')
# # print(bio2)
# # Output ja dekhabe: karina khan is a actor. She is 30 years old
#
#
# # # !! aro akti baboher
