a = None
b = None

#Solve the sum of params @a and @b
def solveMeFirst(a,b):
	if(a >= 1 and b <= 1000):
		sum = a+b
		return sum
	else:
		print('Variables provided are out of bounds')
		return 0

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)