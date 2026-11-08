from time import sleep

a = int(input("Введіть швидкість першого поїзда: "))
b = int(input("Введіть швидкість другого поїзда: "))
length = 400

time = length / (a+b)

print("Чекайте, виконую обчислення.......")
sleep(2.5)
print("Це займе: ", round(time, 2), 'годин')