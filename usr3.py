print("Введите число в цельсиях")
a = input()
a = int(a)

print ("выберите конечный результат, введите 1(или F) для перевода в фаренгейт или введите 2(или K) для перевода в кельвин")

config = input()


if((config == "1") | (config == "F")):
    result = (a*1.8)+32
    print(result)

if((config == "2") | (config == "K") | (config == "К")):
    print(a + 274)


#конец
