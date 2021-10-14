def starRectangle():
	print('Star Rectangle')
	m=10
	for i in range(5):
		for k in range(0,m):
			print(end=" ")	
		for j in range(5):
			print("*",end=" ")
		print("\r")



def starpiramid():
	"""star pyramid in ascending order"""
	print('Star Pyramid')
	m=10
	for i in range(0,5):
		for k in range(0,m):
			print(end=" ")
		m-=1	
		for j in range(i+1):
			print("*",end=" ")
		print("\r")

def starpiramid_rev():
	"""star pyramid in reverse order"""
	print('Reverse Star Pyramid')
	m=6
	for i in range(5,0,-1):
		for k in range(0,m):
			print(end=" ")
		m+=1	
		for j in range(i,0,-1):
			print("*",end=" ")
		print("\r")


def pyramid():
	print("pyramid")
	m=10
	n=m
	for i in range(0,5):
		for k in range(0,m):
			print(end=" ")
		m-=1	
		for j in range(i+1):
			print("*",end=" ")
		print("\r")	
	m=(n//2)+2	
	for i in range(4,0,-1):
		for k in range(0,m):
			print(end=" ")
		m+=1	
		for j in range(i,0,-1):
			print("*",end=" ")
		print("\r")	

def number_pyramid():
	"""Number pyramid in ascending order"""
	print('Number Pyramid')
	m=10
	for i in range(0,5):
		for k in range(0,m):
			print(end=" ")
		m-=1	
		for j in range(1,i+2):
			print(j,end=" ")
		print("\r")



def number_pyramid1():
	"""Number pyramid in ascending order"""
	print('Number Pyramid')
	m=10
	for i in range(1,6):
		for k in range(0,m):
			print(end=" ")
		m-=1	
		for j in range(i):
			print(i,end=" ")
		print("\r")


def number_pyramid_rev():
	"""number pyramid in reverse order"""
	print('Reverse Number Pyramid')
	m=6
	for i in range(5,0,-1):
		for k in range(0,m):
			print(end=" ")
		m+=1	
		for j in range(i,0,-1):
			print(i,end=" ")
		print("\r")


starRectangle()
starpiramid()
starpiramid_rev()
pyramid()
number_pyramid()
number_pyramid1()
number_pyramid_rev()	
