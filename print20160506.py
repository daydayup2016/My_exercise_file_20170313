
#n=int(input('please enter a number for n:'))
def tuxing_print(n):
	for i in range(n):
		j=1;k=1
		while j <= n-1-i :
			j=j+1
			print(end=' ')
		while k <= 2*i+1 :
			k=k+1
			print('@',end='')
		print()
		

	for i in range(n):
		i=i+1
		j=1;k=1
		while j <= i :
			j=j+1
			print(end=' ')
		while k <= 2*(n-1-i)+1 :
			k=k+1
			print('*',end='')
		print()