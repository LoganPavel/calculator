k3 = 0
k5 = 0

for i in range(1000):
	if i%3==0:
		k3+= i
	if i%5==0:
		k5+= i

print("Сумма всех чисел кратных 3 = "+str(k3))
print("Сумма всех чисел кратных 5 = "+str(k5))







