print("Введите 2 значения (через enter)")

a = input()


b = input()


if((a == b) & (a!=b)):
    print("невозможно")

if((a == b) | (a!=b) ): #строки сравниваются по их длине
    print("ну, либо они равны, либо нет")

if(a>b):
    print("true")
else:
    print("false")



