import matplotlib.pyplot as plt
p1 = (input('Введите кол-во проверенных плат Блавачинским:'))
f = open("data1.txt")
s1 = 0
for i in f:
    s1 += int(i)
f.close()
sum1 = int(p1) + int(s1)
lines = [p1]
with open("data1.txt", "a") as file:
    file.writelines("%s\n" % line for line in lines)


p2 = (input('Введите кол-во проверенных плат Петровым:'))
f = open("data2.txt")
s2 = 0
for i in f:
    s2 += int(i)
f.close()
sum2 = int(p2) + int(s2)
lines = [p2]
with open("data2.txt", "a") as file:
    file.writelines("%s\n" % line for line in lines)


p3 = (input('Введите кол-во проверенных плат Ивановой:'))
f = open("data3.txt")
s3 = 0
for i in f:
    s3 += int(i)
f.close()
sum3 = int(p3) + int(s3)
lines = [p3]
with open("data3.txt", "a") as file:
    file.writelines("%s\n" % line for line in lines)


p4 = (input('Введите кол-во проверенных плат Добровым:'))
f = open("data4.txt")
s4 = 0
for i in f:
    s4 += int(i)
f.close()
sum4 = int(p4) + int(s4)
lines = [p4]
with open("data4.txt", "a") as file:
    file.writelines("%s\n" % line for line in lines)


p5 = (input('Введите кол-во проверенных плат Федоровым:'))
f = open("data5.txt")
s5 = 0
for i in f:
    s5 += int(i)
f.close()
sum5 = int(p5) + int(s5)
lines = [p5]
with open("data5.txt", "a") as file:
    file.writelines("%s\n" % line for line in lines)


#Алгоритм для сохранения и открытия, чтобы можно было отдельно в каждом в файле подсчитывать и сохранять в памяти кол-во за все время 1го рабочего



#Далее должен быть алгоритм для подсчета суммы прошлого и только что записанного значения
#p1 потом идет отдельно в построение одного из столбца


x = ['Блавачинский', 'Петров', 'Иванова', 'Добров','Федоров']
y = [int(sum1), int(sum2), int(sum3), int(sum4), int(sum5)]

plt.bar(x, y, label='Платы интерфейсные') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Фамилии рабочих')
plt.ylabel('Количество')
plt.title('Эффективность рабочих')
plt.legend()
plt.show()

input()