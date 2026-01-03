# 📘 PYTHON — 2-DARS
# Mavzu: O‘zgaruvchilar


# O'zgaruvchi nima?
# Pythonda o'zgaruvchi - bu xotirada ma'lumot saqlash uchun ishlatiladigan nom
# Unga xar qanday turdagi ma'lumot (raqam, matn, rost, yolg'on, ro'yxat, touple)
# saqlanishi mumkin
yosh = 20            # int (integer) butun son
ism = "Ali"          # str (string) matn
ball = 87.5          # float o'nlik son
haqiqat = True       # boolean (True/False)
# bu tayinlash operatori ya'ni o'zgaruvchiga qiymat beradi
# print() bilan yosh ni chiqarsak oynaga 20 chiqadi, ismni chaqirsak Ali
# int, str, float va boolean shunga o'xshash ma'lumot turlarini keyingi dars o'tamiz


# O‘zgaruvchi nomlari
# Python-da o‘zgaruvchi nomi quyidagi qoidalarga amal qilishi kerak:
# Harf (a–z, A–Z), raqam (0–9), yoki _ dan iborat bo‘lishi mumkin.
# Raqam bilan boshlanmaydi.
# Bo‘sh joy va maxsus belgilar (!@#$%) ishlatilmaydi.
# True, False, None, class kabi Python keywords ishlatilmaydi.
ism = "Ali"          # to'g'ri
yosh_1 = 20          # to'g'ri
_yosh = 30           # to'g'ri
# 1yosh = 25           # ❌ xato
# my-name = "Ali"      # ❌ xato
# Iloji boricha manoli o'zgaruvchi ishlatishga xarakat qiling


# O'zgaruvchilar turlari (Data types)       Misollar
# int - butun son                           20
# float - kasir son                         87.5
# str - matn                                "Ali"
# bool - rost/yolg'pn qiymat                True/False
# list - ro'yxat                            [1,2,3]
# tuple - o'zgarmas ro'yxat                 (1,2,3)
# dict - lug'at, key-value juftligi         {"ism":"Ali"}


# Qiymat chiqarish
ism = "Ali"
print(ism)              # Ali
# Qiymat yabgilash
yoshim = 20
print(yoshim)           # 20
yoshim = 25
print(yoshim)           # 25
# Qiymat 25ga o'zgardi


# Bir nechta o'zgaruvchi bir vaqtning o'zida chiqarish
a, b, c = 1, 2, 3
print(a, b, c)          # 1 2 3


# Qiymatni boshqa o‘zgaruvchiga berish
x = 10
y = x
print(y)                # 10


# O'zgaruvchini malumot turini tekshirish
q = 10
print(type(q))          # int

w = 2.1
print(type(w))          # float

e = "Ali"
print(type(e))          # str

r = False
print(type(r))          # bool
# print(type()) ushbu kod yordamida malumot turini tekshirishimiz mumkin


# F-string bilan chiqarish
# F-string yordamida o‘zgaruvchi qiymatini matnga qo‘shib chiqarish mumkin
ism = "Ali"
yosh = 20
print(f"Mening ismim {ism} va yoshim {yosh}")  
# natija - Mening ismim Ali va yoshim 20


# Vazifa 1:
# Foydalanuvchidan ism va yoshni so‘rab, quyidagicha chiqaring:
# Salom, menning ismim [ism] va men [yosh] yoshdaman.
ism = input("Ismingizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")
print(f"Salom, mening ismim {ism} va men {yosh} yoshdaman.")


a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
natija = a + b
print(f"{a} + {b} = {natija}")


# input() - foydalanuvchidan ma'lumot kiritishni so'rash uchun ishlatiladi funksiya
# Foydalanuvchi ma'lumot kiritsa Python uni string (matn) shaklida qabul qiladi
ism = input("Ismingizni kiriting: ")
print("Salom", ism)
# "Ismingizni kiriting: " – bu foydalanuvchiga ko‘rsatiladigan matn (prompt).
# ism – foydalanuvchi kiritgan qiymat string sifatida saqlanadi.


# input() har doim string qaytaradi. Agar raqam bilan ishlash kerak bo‘lsa,
# uni int() yoki float() ga o‘zgartirish kerak.
yosh = input("Yoshingizni kiriting: ")
print(type(yosh))  # <class 'str'>

# Agar raqam sifatida ishlatmoqchi bo'lsak
yosh = int(input("Yoshingizni kiriting: "))
print(type(yosh))  # <class 'int'>


# Misol 1: Ism va yoshni chiqarish
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
print(f"Salom {ism}, siz {yosh} yoshdasiz")

# Misol 2: Ikki sonni qo‘shish
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
print(f"{a} + {b} = {a + b}")


# Ballni bahoga aylantirish
ball = int(input("Ballingizni kiriting: "))

if ball >= 90:
    print("Siz 5-baxoga o'tdingiz")
elif ball >= 70:
    print("Siz 4-baxoga o'tdingiz")
elif ball >= 60:
    print("Siz 3-baxoga o'tdingiz")
else:
    print("Siz yiqildingiz")

# if, elif, else keyingi darslarda yaxshiroq tushunib olasiz
    
# Muhim eslatmalar
# Har doim input() string qaytaradi.
# Raqam kiritadigan bo‘lsangiz, int() yoki float() bilan o‘zgartiring.
# input() bilan olingan qiymatni o‘zgaruvchiga saqlash shart.