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

# def starpiramid3():
# 	print('Star Pyramid')
# 	m=10
# 	for i in range(1,8):
# 		for k in range(0,m):
# 			print(end=" ")
# 		m-=1
		
# 		for j in range(1,i+1):
				
			
# 				if  j==1 or j==i:
# 					print("*",end=' ')
# 				else:
# 					print(" ",end=" ")	
					
			
# 		print("\r")



def pattern1():
	print('pattern1')
	m=10
	for i in range(5):
		for k in range(0,m):
			print(end=" ")	
		for j in range(5):
			if i==2 or j==2:
				print("* ",end=" ")
			else:
				print("o ",end=" ")	
		print("\r")	

def pattern2():
	print('pattern2')
	m=10
	for i in range(5):
		for k in range(0,m):
			print(end=" ")	
		for j in range(5):
			if i==2 or j==2:
				print("* ",end=" ")
			else:
				print("  ",end=" ")	
		print("\r")		

def pattern3():
	print('pattern3')
	m=10
	for i in range(5):
		for k in range(0,m):
			print(end=" ")	
		for j in range(5):
			if i==2 and j==2:
				print("o ",end=" ")
			else:
				print("* ",end=" ")	
		print("\r")		

def pattern4():
	print('pattern4')
	m=10
	for i in range(1,6):
		for k in range(0,m):
			print(end=" ")	
		for j in range(1,6):
			if i==j or i+j==6:
				print("* ",end=" ")
			else:
				print("o ",end=" ")	
		print("\r")		


def pattern5():
	print('pattern5')
	m=10
	for i in range(1,6):
		for k in range(0,m):
			print(end=" ")	
		for j in range(1,6):
			if i==j :
				print("* ",end=" ")
			else:
				print("o ",end=" ")	
		print("\r")	

def pattern6():
	print('pattern6')
	m=10
	for i in range(1,6):
		for k in range(0,m):
			print(end="  ")
		m-=1		
		for j in range(1,6):
				print("o ",end=" ")
			
		print("\r")

def pattern7():
	print('pattern7')
	m=10
	for i in range(1,7):
		if i%2 !=0:
			l=i+1
		else:
			l=i	
		for k in range(0,m):
			print(end=" ")		
		for j in range(1,l+1):
				print("* ",end=" ")
			
		print("\r")

# def pattern8():
# 	print('pattern8')
# 	m=10
# 	for i in range(1,7):
# 		if i%2 !=0:
# 			l=i+1
# 		else:
# 			l=i	
# 		for k in range(0,m):
# 			print(end=" ")		
# 		for j in range(1,7):
# 			if 7-j<=l:
# 				print("* ",end=" ")
# 			else:
# 				print("  ",end=" ")	
			
# 		print("\r")		


def pattern8():
	print('pattern8')
	m=10
	for i in range(1,7):
		if i%2 !=0:
			l=i+1
		else:
			l=i	
		for k in range(0,m):
			print(end=" ")
		for y in range(6,l,-1):
			print("  ",end=" ")			
		for j in range(0,l):
			print("* ",end=" ")	
		print("\r")		


def pattern9():
	print('pattern9')
	m=10
	for i in range(6,0,-1):
		if i%2 !=0:
			l=i+1
		else:
			l=i	
		for k in range(0,m):
			print(end=" ")		
		for j in range(0,l):
			print("* ",end=" ")	
		print("\r")

def pattern10():
	print('pattern10')
	m=10
	for i in range(6,0,-1):
		if i%2 !=0:
			l=i+1
		else:
			l=i	
		for k in range(0,m):
			print(end=" ")
		for y in range(6,l,-1):
			print("  ",end=" ")			
		for j in range(0,l):
			print("* ",end=" ")	
		print("\r")		


def pattern12():
	print('pattern12')
	m=10
	for i in range(1,7):
		for k in range(0,m):
			print(end=" ")		
		for j in range(1,7):
			if i==1 or i==6 or j==1 or j==6:  
				print("* ",end=" ")
			else:
				print("o ",end=" ")		
		print("\r")		


def pattern13():
	print('pattern13')
	m=10
	for i in range(1,7):
		for k in range(0,m):
			print(end=" ")		
		for j in range(1,7):
			if i==1 or i==6 or j==1 or j==6:  
				print("* ",end=" ")
			else:
				print("  ",end=" ")		
		print("\r")	

def pattern14():
	print('pattern14')
	m=10
	for i in range(1,8):
		for k in range(0,m):
			print(end=" ")		
		for j in range(1,8):
			if i==1 or i==7 or j==1 or j==7 or i==j or i+j==8:  
				print("* ",end=" ")
			else:
				print("  ",end=" ")		
		print("\r")				



starRectangle()
starpiramid()
starpiramid_rev()
pyramid()
number_pyramid()
number_pyramid1()
number_pyramid_rev()
# starpiramid3()
pattern1()	
pattern2()
pattern3()
pattern4()
pattern5()
pattern6()
pattern7()
pattern8()
pattern9()
pattern10()
pattern12()
pattern13()
pattern14()


