print("Введите 2 значения (через enter)")

a = input()
a = int(a)

b = input()
b = int(b)

if((a == b) & (a!=b)):
    print("невозможно")

if((a == b) | (a!=b) ): 
    print("ну, либо они равны, либо нет")

if(a>b):
    print("true")
else:
    print("false")



